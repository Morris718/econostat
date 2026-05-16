import pandas as pd
import numpy as np
from scipy import stats
from sklearn.impute import SimpleImputer, IterativeImputer
import warnings
warnings.filterwarnings('ignore')


class DataCleaner:
    """Smart data cleaner for handling missing values, outliers, and inconsistencies."""
    
    def __init__(self, df):
        self.df = df.copy()
        self.original_df = df.copy()
        self.cleaning_report = {}
    
    def detect_missing_values(self):
        """Detect and report missing values."""
        missing = self.df.isnull().sum()
        missing_pct = (missing / len(self.df)) * 100
        
        report = pd.DataFrame({
            'Column': missing.index,
            'Missing_Count': missing.values,
            'Missing_Percentage': missing_pct.values
        })
        
        report = report[report['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)
        self.cleaning_report['missing_values'] = report
        return report
    
    def detect_outliers(self, method='iqr', columns=None):
        """Detect outliers using IQR or Z-score method."""
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        outliers = pd.DataFrame()
        
        for col in columns:
            if col in self.df.columns and self.df[col].dtype in [np.float64, np.int64]:
                if method == 'iqr':
                    Q1 = self.df[col].quantile(0.25)
                    Q3 = self.df[col].quantile(0.75)
                    IQR = Q3 - Q1
                    lower_bound = Q1 - 1.5 * IQR
                    upper_bound = Q3 + 1.5 * IQR
                    outlier_rows = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)]
                
                elif method == 'zscore':
                    z_scores = np.abs(stats.zscore(self.df[col].dropna()))
                    threshold = 3
                    outlier_rows = self.df[np.abs(stats.zscore(self.df[col].fillna(self.df[col].mean()))) > threshold]
                
                if len(outlier_rows) > 0:
                    outliers = pd.concat([outliers, pd.DataFrame({
                        'Column': col,
                        'Outlier_Count': len(outlier_rows),
                        'Lower_Bound': lower_bound if method == 'iqr' else None,
                        'Upper_Bound': upper_bound if method == 'iqr' else None
                    }, index=[0])])
        
        self.cleaning_report['outliers'] = outliers
        return outliers
    
    def detect_duplicates(self):
        """Detect duplicate rows."""
        dup_count = self.df.duplicated().sum()
        self.cleaning_report['duplicates'] = dup_count
        return dup_count
    
    def detect_inconsistencies(self):
        """Detect data type inconsistencies."""
        inconsistencies = []
        
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                # Check for case variations
                unique_vals = self.df[col].unique()
                if len(unique_vals) > 1:
                    # Check if values differ only by case
                    lower_vals = set(str(v).lower() for v in unique_vals if pd.notna(v))
                    if len(lower_vals) < len(unique_vals):
                        inconsistencies.append({
                            'Column': col,
                            'Issue': 'Case variations detected',
                            'Examples': str(unique_vals[:3])
                        })
        
        inconsistencies_df = pd.DataFrame(inconsistencies)
        self.cleaning_report['inconsistencies'] = inconsistencies_df
        return inconsistencies_df
    
    def impute_missing_values(self, method='mean', columns=None):
        """Impute missing values using specified method."""
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        df_clean = self.df.copy()
        
        if method == 'mean':
            imputer = SimpleImputer(strategy='mean')
        elif method == 'median':
            imputer = SimpleImputer(strategy='median')
        elif method == 'mode':
            imputer = SimpleImputer(strategy='most_frequent')
        elif method == 'forward_fill':
            df_clean = df_clean.fillna(method='ffill')
            return df_clean
        elif method == 'mice':
            imputer = IterativeImputer(max_iter=10, random_state=42)
        else:
            return df_clean
        
        numeric_cols = df_clean[columns].select_dtypes(include=[np.number]).columns
        df_clean[numeric_cols] = imputer.fit_transform(df_clean[numeric_cols])
        
        self.df = df_clean
        return df_clean
    
    def remove_duplicates(self):
        """Remove duplicate rows."""
        self.df = self.df.drop_duplicates()
        return self.df
    
    def cap_outliers(self, method='iqr', columns=None):
        """Cap outliers instead of removing them."""
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        df_capped = self.df.copy()
        
        for col in columns:
            if col in df_capped.columns and df_capped[col].dtype in [np.float64, np.int64]:
                if method == 'iqr':
                    Q1 = df_capped[col].quantile(0.25)
                    Q3 = df_capped[col].quantile(0.75)
                    IQR = Q3 - Q1
                    lower_bound = Q1 - 1.5 * IQR
                    upper_bound = Q3 + 1.5 * IQR
                    df_capped[col] = df_capped[col].clip(lower=lower_bound, upper=upper_bound)
        
        self.df = df_capped
        return df_capped
    
    def standardize_text(self, columns=None):
        """Standardize text columns (lowercase, strip whitespace)."""
        if columns is None:
            columns = self.df.select_dtypes(include='object').columns
        
        for col in columns:
            if col in self.df.columns:
                self.df[col] = self.df[col].str.lower().str.strip()
        
        return self.df
    
    def auto_clean(self):
        """Automatically apply all cleaning steps."""
        # Standardize text
        self.standardize_text()
        
        # Remove duplicates
        self.remove_duplicates()
        
        # Impute missing values (mean for numeric)
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        self.impute_missing_values(method='median', columns=numeric_cols)
        
        # Cap outliers
        self.cap_outliers(method='iqr')
        
        return self.df
    
    def get_cleaned_data(self):
        """Return cleaned dataframe."""
        return self.df
    
    def get_cleaning_summary(self):
        """Get summary of all cleaning operations."""
        return self.cleaning_report
    
    def export_cleaned_data(self, filepath, format='csv'):
        """Export cleaned data to file."""
        if format == 'csv':
            self.df.to_csv(filepath, index=False)
        elif format == 'excel':
            self.df.to_excel(filepath, index=False)
        return filepath
