import streamlit as st
import pandas as pd
import joblib
import os

# Set page config
st.set_page_config(page_title="Customer Churn Prediction", page_icon="👥", layout="wide")

st.title("👥 Customer Churn Prediction Dashboard")
st.write("This interactive application uses a Machine Learning model to predict whether a customer is likely to churn (leave the service) and identifies key risk factors.")

# Define paths for separate model and scaler
model_path = "model.pkl"
scaler_path = "scaler.pkl"

if not os.path.exists(model_path) or not os.path.exists(scaler_path):
    st.warning("⚠️ Machine Learning model files (`model.pkl` and `scaler.pkl`) are missing! Please run the training script (`src/train.py`) first to generate them.")
else:
    # Load separate model and scaler objects
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    
    # Create input sections
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("👤 Demographics")
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior_citizen = st.selectbox("Senior Citizen (Age >= 65)", ["No", "Yes"])
        partner = st.selectbox("Has Partner", ["Yes", "No"])
        dependents = st.selectbox("Has Dependents", ["Yes", "No"])
        
    with col2:
        st.subheader("📝 Account & Contract")
        tenure = st.slider("Tenure (Months active)", min_value=0, max_value=72, value=12)
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
        payment_method = st.selectbox("Payment Method", [
            "Electronic check", 
            "Mailed check", 
            "Bank transfer (automatic)", 
            "Credit card (automatic)"
        ])
        
    with col3:
        st.subheader("💰 Financials & Services")
        monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=65.0, step=0.5)
        # Default TotalCharges to monthly * tenure for user convenience
        default_total = float(monthly_charges * tenure)
        total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=default_total, step=5.0)
        
        internet_service = st.selectbox("Internet Service Provider", ["DSL", "Fiber optic", "No"])
        
    st.markdown("---")
    st.subheader("🛠️ Services Subscribed")
    col4, col5, col6 = st.columns(3)
    
    # If Internet Service is "No", some services are automatically "No internet service"
    has_internet = internet_service != "No"
    
    with col4:
        phone_service = st.selectbox("Phone Service", ["Yes", "No"])
        multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"] if phone_service == "Yes" else ["No phone service"])
        online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"] if has_internet else ["No internet service"])
        
    with col5:
        online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"] if has_internet else ["No internet service"])
        device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"] if has_internet else ["No internet service"])
        
    with col6:
        tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"] if has_internet else ["No internet service"])
        streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"] if has_internet else ["No internet service"])
        streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"] if has_internet else ["No internet service"])

    st.markdown("---")
    
    if st.button("Predict Churn Risk", type="primary"):
        # Map inputs to standard dataframe format
        senior_val = 1 if senior_citizen == "Yes" else 0
        
        input_data = {
            'gender': [gender],
            'SeniorCitizen': [senior_val],
            'Partner': [partner],
            'Dependents': [dependents],
            'tenure': [int(tenure)],
            'PhoneService': [phone_service],
            'MultipleLines': [multiple_lines],
            'InternetService': [internet_service],
            'OnlineSecurity': [online_security],
            'OnlineBackup': [online_backup],
            'DeviceProtection': [device_protection],
            'TechSupport': [tech_support],
            'StreamingTV': [streaming_tv],
            'StreamingMovies': [streaming_movies],
            'Contract': [contract],
            'PaperlessBilling': [paperless],
            'PaymentMethod': [payment_method],
            'MonthlyCharges': [float(monthly_charges)],
            'TotalCharges': [float(total_charges)]
        }
        
        input_df = pd.DataFrame(input_data)
        
        # Preprocess features using the scaler first
        input_preprocessed = scaler.transform(input_df)
        
        # Predict using separate model
        pred_prob = model.predict_proba(input_preprocessed)[0][1]
        pred_class = model.predict(input_preprocessed)[0]
        
        # Display Results
        st.subheader("📊 Prediction Results")
        prob_percentage = pred_prob * 100
        
        if pred_class == 1:
            st.error(f"🚨 **High Churn Risk (Probability: {prob_percentage:.1f}%)**")
            st.write("This customer is highly likely to cancel their service. Proactive retention measures are strongly recommended.")
        else:
            st.success(f"🟢 **Low Churn Risk (Probability: {prob_percentage:.1f}%)**")
            st.write("This customer is stable and likely to continue their service.")
            
        # Context-Aware Business Insights & Retention Recommendations
        st.subheader("💡 Key Risk Factors & Action Items")
        risks = []
        if contract == "Month-to-month":
            risks.append("- **Month-to-month Contract**: This is the single highest predictor of churn. **Action**: Offer a 10-15% discount on transitioning them to a 1-Year or 2-Year contract.")
        if internet_service == "Fiber optic":
            risks.append("- **Fiber Optic Service**: Fiber optic plans see high churn rates. **Action**: Proactively check in regarding speed satisfaction or price sensitivity.")
        if tech_support == "No" and internet_service != "No":
            risks.append("- **No Tech Support Subscribed**: Customers who troubleshoot alone are more likely to leave. **Action**: Provide a 3-month free trial of Premium Tech Support.")
        if online_security == "No" and internet_service != "No":
            risks.append("- **No Online Security**: **Action**: Cross-sell security bundles during billing touchpoints.")
        if payment_method == "Electronic check":
            risks.append("- **Manual Electronic Check Billing**: **Action**: Incentivize a one-time $10 credit to switch to automatic payments (Credit Card/Bank Transfer auto-pay).")
        if tenure < 12:
            risks.append("- **New Customer (< 1 Year Tenure)**: Customer is in the critical onboarding lifecycle. **Action**: Schedule a customer success call to ensure setup satisfaction.")
            
        if risks:
            for risk in risks:
                st.write(risk)
        else:
            st.write("This customer exhibits a highly loyal behavior profile. Keep up the good engagement!")
