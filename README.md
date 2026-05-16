# 🔍 EconoStat: The Regression-Ready Data Cleaner & Analyzer

A production-ready desktop application for econometric analysis. Feed it messy data, get clean datasets, automated regression analysis, and professional reports—all offline, all in one app.

## ✨ What It Does

**End-to-End Workflow:**

1. **Load messy data** (CSV/Excel from surveys, government datasets, your logs)
2. **Auto-clean** (missing values, outliers, inconsistencies)
3. **Run regression** (OLS with diagnostics, multicollinearity checks, assumption tests)
4. **Export reports** (professional HTML with plain-English interpretations)

## 🎯 Features

### Phase 1: Smart Data Cleaner ✅
- 🔍 Missing value detection with intelligent imputation (mean, median, mode, MICE, forward-fill)
- 📊 Outlier detection (IQR & Z-score methods)
- 🏷️ Data type inference and inconsistency standardization
- 🗑️ Duplicate removal
- 💾 Export cleaned datasets

### Phase 2: Auto Regression Engine ✅
- 🔗 Multicollinearity testing (VIF calculation & recommendations)
- 📈 OLS regression with optional robust standard errors (Huber-White)
- ✔️ Residual normality testing (Shapiro-Wilk)
- 📉 Heteroskedasticity detection (Breusch-Pagan)
- 🎯 Automatic assumption violation detection
- 💡 Transformation suggestions

### Phase 3: Report Generator ✅
- 📄 Professional HTML reports
- 📊 Regression summary tables (coefficients, p-values, R², adjusted R²)
- 📈 Diagnostic visualizations
- 📝 Plain-English interpretations of coefficients
- ⚠️ Warning flags for assumption violations

### Phase 4: Desktop GUI ✅
- 🎨 Intuitive 4-tab interface (Load Data → Clean → Regression → Reports)
- 🖱️ Drag-and-drop friendly
- ⚡ No command line required
- 💾 Session persistence

## 🚀 Quick Start

### Installation

```bash
# 1. Clone repository
git clone https://github.com/Morris718/econostat.git
cd econostat

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Running the App

```bash
python src/main.py
```

A desktop window will open. Start by loading a CSV or Excel file!

## 📖 Typical Workflow

1. **Load Data Tab**
   - Click "Load CSV File" or "Load Excel File"
   - See preview of your data
   - Check summary statistics

2. **Clean Data Tab**
   - Click "Detect Issues" → See missing values, outliers, duplicates
   - Click "Auto-Clean" → Intelligent imputation & handling
   - Click "Export Cleaned Data" → Get CSV/Excel file

3. **Regression Tab**
   - Select dependent variable (Y) from dropdown
   - Select independent variables (X) from list
   - Click "Run Regression"
   - View coefficients, R², diagnostic tests, warnings

4. **Reports Tab**
   - Click "Generate HTML Report" → Professional report with interpretations
   - Click "Export Coefficients CSV" → Coefficients table
   - Click "Export Model Summary" → Full regression summary

## 💻 Tech Stack

| Library | Purpose |
|---------|---------|
| **pandas** | Data manipulation & analysis |
| **numpy** | Numerical operations |
| **statsmodels** | Regression & diagnostics |
| **scipy** | Statistical tests |
| **scikit-learn** | Advanced imputation (MICE) |
| **matplotlib** + **seaborn** | Visualizations |
| **tkinter** | Native desktop GUI |

**100% offline** • **No data leaves your PC** • **Fully Python-native**

## 📊 Example Workflow

```
1. Load survey_data.csv
   ↓
2. Auto-Clean detects:
   - 23 missing values in 'Income' column
   - 5 outliers in 'Spending' column
   - Case variations in 'Education' column
   ↓
3. Clean with one click
   ↓
4. Select variables:
   Y: Spending
   X: Income, Age, Education
   ↓
5. Run regression → Get results:
   R² = 0.73, p < 0.001
   Income coefficient: 0.58 (p=0.002) ✓ Significant
   Heteroskedasticity detected: ⚠️ Robust SE applied
   ↓
6. Export HTML Report
   → Ready to paste into assignments!
```

## 🔧 File Structure

```
econostat/
├── src/
│   ├── main.py              # GUI application (run this!)
│   ├── data_cleaner.py      # Phase 1: Data cleaning engine
│   ├── regression_engine.py # Phase 2: Regression analysis
│   ├── report_generator.py  # Phase 3: Report generation
│   └── utils.py             # Helper functions
├── tests/
│   └── test_cleaner.py      # Unit tests for data cleaner
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🧪 Testing

Run unit tests:

```bash
pytest tests/ -v
```

## 📋 Supported Data Formats

**Input:**
- CSV (.csv)
- Excel (.xlsx, .xls)
- Up to 1GB (limited by RAM)

**Output:**
- CSV (.csv)
- Excel (.xlsx)
- HTML reports (.html)
- Text summaries (.txt)

## 🎓 What You'll Learn

✅ **Real econometrics** - Not just coding, but proper statistical workflows  
✅ **Data quality** - How to identify and handle messy data  
✅ **OLS regression** - Coefficients, p-values, diagnostics, assumptions  
✅ **Multicollinearity** - What it is, how to detect it, what to do  
✅ **Assumption testing** - Normality, heteroskedasticity, autocorrelation  
✅ **Automation** - How to build statistical workflows  

## 💼 Why This Matters

- **For students**: Automate repetitive econometrics assignments
- **For researchers**: Clean & analyze data in seconds, not hours
- **For employers**: Shows you understand statistical workflows & can build tools
- **For privacy**: Everything stays on your PC—no cloud, no data sharing

## ⚠️ Important Notes

- **Data Privacy**: All data stays on your local machine. Nothing is uploaded anywhere.
- **Assumptions**: This tool assumes your data is reasonably clean to start
- **Sample Size**: For reliable regression results, aim for n > 30 observations
- **Interpretation**: Always use statistical judgment. Statistical significance ≠ practical significance

## 🐛 Troubleshooting

**Problem**: "ModuleNotFoundError"
- **Solution**: Run `pip install -r requirements.txt`

**Problem**: "MemoryError" with large files
- **Solution**: Use a subset of columns or a machine with more RAM

**Problem**: Regression won't run
- **Solution**: Check that Y and X variables are numeric and n > k+1

## 📝 Sample Output

Generated HTML reports include:

```
┌─────────────────────────────────────┐
│ EconoStat Regression Report         │
├─────────────────────────────────────┤
│ Model Fit                           │
│ R² = 0.73 | Adj R² = 0.71          │
│ F = 45.23 (p < 0.001) ✓            │
├─────────────────────────────────────┤
│ Coefficients                        │
│ Income: 0.58*** (p=0.002)          │
│ Age:    0.12*   (p=0.043)          │
│ Edu:   -0.05    (p=0.156)          │
├─────────────────────────────────────┤
│ Diagnostics                         │
│ Normality:        ✓ Pass            │
│ Heteroscedasticity: ⚠️ Warning     │
│ Autocorrelation:  ✓ OK              │
└─────────────────────────────────────┘
```

## 📄 License

MIT License - Use freely in personal, commercial, or academic projects.

## 🤝 Contributing

Found a bug? Have a feature idea?

1. Create an issue: [GitHub Issues](https://github.com/Morris718/econostat/issues)
2. Fork & submit a pull request
3. Share feedback!

## 🙏 Acknowledgments

Built with:
- [pandas](https://pandas.pydata.org/) for data manipulation
- [statsmodels](https://www.statsmodels.org/) for regression analysis
- [scikit-learn](https://scikit-learn.org/) for imputation
- [matplotlib](https://matplotlib.org/) & [seaborn](https://seaborn.pydata.org/) for visualization

## 📧 Support

Questions? Open an issue on GitHub or check the troubleshooting section above.

---

**EconoStat** - Making econometrics accessible, automated, and awesome. 🚀

Last updated: 2026-05-16
