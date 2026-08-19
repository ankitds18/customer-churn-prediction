# Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn based on customer demographics, account information, financial details, and subscribed services.

## 📌 Project Overview

Customer churn occurs when a customer stops using a company's service. Predicting churn in advance can help businesses identify high-risk customers and take proactive retention actions.

This project uses Machine Learning to analyze customer information and predict churn risk through an interactive Streamlit web application.

## 🎯 Project Objectives

- Predict whether a customer is likely to churn.
- Analyze customer demographics and account information.
- Identify important factors associated with customer churn.
- Compare multiple Machine Learning classification models.
- Evaluate model performance using standard classification metrics.
- Build an interactive web application for churn prediction.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Jupyter Notebook
- Streamlit
- Git & GitHub

## 🤖 Machine Learning Models

The project compares:
1. Logistic Regression
2. Decision Tree
3. Random Forest
4. XGBoost

Evaluation metrics:
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix

## 📊 Dataset

The project uses the Telco Customer Churn dataset.

It contains customer demographics, tenure, contract type, payment method, monthly charges, total charges, internet services, phone services, online security, online backup, device protection, tech support, and streaming services.

The dataset can be downloaded using `download_data.py`.

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Preprocessing
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Model Comparison
   ↓
Model Evaluation
   ↓
Best Model
   ↓
Streamlit Dashboard
   ↓
Churn Prediction
```

## 🧹 Data Preprocessing

- Removing unnecessary customer identifiers.
- Converting numerical columns into appropriate data types.
- Handling missing values.
- Encoding the target variable.
- Scaling numerical features.
- Encoding categorical features.
- Splitting the dataset into training and testing sets.

## 📈 Model Evaluation

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | ~80.2% | ~64.9% | ~54.7% | ~0.594 | ~0.844 |
| Decision Tree | ~78.8% | ~60.3% | ~57.9% | ~0.591 | ~0.826 |
| Random Forest | ~80.3% | ~65.6% | ~53.3% | ~0.588 | ~0.840 |
| XGBoost | ~78.3% | ~59.9% | ~53.6% | ~0.566 | ~0.823 |

## 🖥️ Streamlit Dashboard

The project includes an interactive Streamlit dashboard where users can enter customer information and receive a churn-risk prediction.

## 📁 Repository Structure

```text
customer-churn-prediction/
│
├── app.py
├── churn_prediction.ipynb
├── download_data.py
├── model.pkl
├── requirements.txt
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ankitds18/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Download the dataset

```bash
python download_data.py
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

## 💡 Business Insights

Customer churn can be influenced by factors such as contract type, customer tenure, monthly charges, payment method, internet service, technical support, and additional subscribed services.

## 🔮 Future Improvements

- Deploy the application online.
- Add advanced feature engineering.
- Improve model performance through hyperparameter tuning.
- Add explainable AI techniques such as SHAP.
- Add interactive visual analytics.
- Implement customer retention recommendations.

## 👨‍💻 Author

**Ankit Kumar**

Aspiring Data Scientist | Python | SQL | Machine Learning | Power BI

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
