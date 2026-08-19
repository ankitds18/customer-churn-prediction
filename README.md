# End-to-End Customer Churn Prediction & Analysis

This repository contains a comprehensive **Customer Churn Prediction and Business Intelligence** project. Predicting customer churn (identifying customers who are likely to cancel their subscriptions) is a critical objective for subscription-based businesses, such as telecom providers, SaaS companies, and utilities.

By predicting churn early, businesses can target high-risk customers with proactive retention campaigns (e.g., custom offers, contracts, discounts), directly reducing customer acquisition costs and stabilizing recurring revenue.

---

## 🎯 Project Objective
1. **Predict:** Build a Machine Learning pipeline to classify whether a customer is at high risk of churning.
2. **Understand:** Identify key demographic, billing, and behavioral indicators of churn (e.g., contract types, service complaints, tech support presence).
3. **Analyze:** Run analytical SQL queries to answer corporate business intelligence questions.
4. **Visualize:** Provide guidelines to build an interactive dashboard in Power BI representing churn metrics.
5. **Interact:** Deliver a Streamlit web application where sales and customer service agents can input customer profiles to fetch real-time churn predictions.

---

## 🛠️ Project Stack & Technologies
- **Programming & Scripting:** Python 3.13
- **Data Engineering & Analysis:** Pandas, NumPy
- **Visualizations:** Matplotlib, Seaborn
- **Machine Learning (Scikit-Learn & XGBoost):**
  - Logistic Regression (Baseline Model)
  - Decision Trees
  - Random Forest Classifiers
  - XGBoost (Advanced Gradient Boosting)
- **Deployment:** Streamlit (Web App)
- **Business Intelligence & Databases:** SQL, Power BI
- **Version Control:** Git, GitHub

---

## 📁 Repository Structure
```
d:\data science\
├── data\
│   ├── Telco-Customer-Churn.csv          # Raw dataset (from IBM GitHub)
│   └── Telco-Customer-Churn-Cleaned.csv  # Preprocessed dataset
├── models\
│   ├── best_model_pipeline.pkl           # Saved Scikit-Learn Pipeline (Preprocessor + Classifier)
│   └── model_results_summary.txt         # Metric summary for all models
├── sql\
│   └── churn_queries.sql                 # Portfolio SQL scripts for customer analysis
├── src\
│   ├── data_preprocessing.py             # Script for cleaning and mapping data
│   └── train.py                          # Script for model comparison, evaluation, and serialization
├── app.py                                # Streamlit Web Application
├── churn_prediction.ipynb                # Complete EDA & ML Jupyter Notebook
├── requirements.txt                      # Project libraries
└── README.md                             # Project Documentation
```

---

## 🔄 Workflow & Project Execution

### Step 1: Clone and Set Up Environment
```bash
# 1. Create a virtual environment
python -m venv .venv

# 2. Activate virtual environment
# On Windows PowerShell:
.venv\Scripts\Activate.ps1
# On Linux/macOS:
source .venv/bin/activate

# 3. Install packages
pip install -r requirements.txt
```

### Step 2: Download Dataset
Execute the download helper script:
```bash
python download_data.py
```
This fetches the official **Telco Customer Churn** dataset (7,043 rows, 21 columns) containing customer demographic information (gender, senior status, partners), service subscription details (tech support, streaming services, internet type), and account info (tenure, billing charges, contract type).

### Step 3: Run Preprocessing & Cleaning
```bash
python src/data_preprocessing.py
```
- Drops `customerID`.
- Coerces blank spaces in `TotalCharges` to `NaN` and fills them with `0.0` (as these correspond to new users with a `tenure` of 0).
- Encodes the binary target `Churn` (Yes $\rightarrow$ 1, No $\rightarrow$ 0).
- Outputs the cleaned data to `data/Telco-Customer-Churn-Cleaned.csv`.

### Step 4: Model Training and Evaluation
```bash
python src/train.py
```
This trains and compares Logistic Regression, Decision Tree, Random Forest, and XGBoost using a robust **Scikit-Learn Pipeline** (`StandardScaler` for numeric features and `OneHotEncoder(drop='if_binary')` for categorical variables).

Typical evaluation scores:
| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression** | ~80.2% | ~64.9% | ~54.7% | ~0.594 | ~0.844 |
| **Decision Tree** | ~78.8% | ~60.3% | ~57.9% | ~0.591 | ~0.826 |
| **Random Forest** | ~80.3% | ~65.6% | ~53.3% | ~0.588 | ~0.840 |
| **XGBoost** | ~78.3% | ~59.9% | ~53.6% | ~0.566 | ~0.823 |

The pipeline containing the **highest F1-score model** (usually Logistic Regression or Random Forest) is saved to `models/best_model_pipeline.pkl`.

### Step 5: Start the Streamlit Web Application
```bash
streamlit run app.py
```
This launches a browser-based UI where you can adjust customer sliders, select options, and test predictions interactively.

---

## 📊 SQL Business Intelligence
For resume and interview demonstration, refer to [sql/churn_queries.sql](file:///d:/data%20science/sql/churn_queries.sql) which contains analytical SQL statements covering:
1. **Global Churn Rate**
2. **Churn Rate by Contract Type** (Month-to-month contracts exhibit ~42.7% churn vs. Two-year contracts at ~2.8%)
3. **Monthly Revenue Leakage** (loss metrics)
4. **Internet Service & Tech Support Impact**
5. **Tenure Cohort Analysis**

---

## 📈 Power BI Dashboard Design Guide
To create a high-impact dashboard in Power BI, follow these guidelines:

### 1. Data Connection & Preparation
- Import the cleaned CSV file: `data/Telco-Customer-Churn-Cleaned.csv`.
- Rename columns for clean readability in visuals (e.g., `tenure` $\rightarrow$ `Tenure (Months)`).

### 2. Key DAX Measures to Write
Create a new measures table and write the following formulas:
- **Total Customers:**
  ```DAX
  Total Customers = COUNTROWS('Telco-Customer-Churn-Cleaned')
  ```
- **Churned Customers:**
  ```DAX
  Churned Customers = CALCULATE(COUNTROWS('Telco-Customer-Churn-Cleaned'), 'Telco-Customer-Churn-Cleaned'[Churn] = 1)
  ```
- **Churn Rate %:**
  ```DAX
  Churn Rate % = DIVIDE([Churned Customers], [Total Customers], 0)
  ```
- **Monthly Revenue Lost ($):**
  ```DAX
  Monthly Revenue Lost = CALCULATE(SUM('Telco-Customer-Churn-Cleaned'[MonthlyCharges]), 'Telco-Customer-Churn-Cleaned'[Churn] = 1)
  ```

### 3. Suggested Visual Layout
1. **Top KPI Cards:** Total Customers, Churn Rate %, Monthly Revenue Lost.
2. **Donut Charts:**
   - Churn by Contract Type (highlights the month-to-month risk).
   - Churn by Payment Method (shows manual Electronic Check vs. Auto-Pay).
3. **Stacked Bar Chart:** Churn Rate by Internet Service (`Fiber optic` shows disproportionately high churn).
4. **Line Chart:** Churn Rate over Tenure Groups (demonstrating how risk decreases as tenure increases).
5. **Clustered Column Chart:** Churn Rate by Tech Support presence.

---

## 💡 Key Business Recommendations
Based on the EDA and model findings, the business should implement:
1. **Contract Transition campaigns:** Focus heavily on Month-to-Month customers. Offer them a small loyalty discount if they convert to a 1-year or 2-year agreement.
2. **Auto-Pay Enrollment incentives:** Offer a one-time bill credit (e.g., $10) for customers paying via Electronic Check to switch to credit card or bank auto-pay.
3. **Service Bundling:** Provide Tech Support and Online Security as standard features or highly discounted add-ons, as customers with these services show significantly lower churn rates.
4. **New Customer Care:** Set up automated check-ins during the first 6 months of a customer's contract, which represents the highest risk cohort.
