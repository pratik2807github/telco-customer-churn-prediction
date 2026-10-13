import streamlit as st 
import pandas as pd 
import joblib 
import os

# Page configuration 
st.set_page_config( 
    page_title="Customer Churn Prediction", 
    page_icon="📊", 
    layout="centered" 
) 

# Load the trained model 
MODEL_PATH = os.path.join( 
    os.path.dirname(os.path.abspath(__file__)), 
    "churn_model.pkl" 
)

@st.cache_resource 
def load_model(): 
    return joblib.load(MODEL_PATH) 
    
try: 
    model = load_model() 
except Exception as e: 
    st.error(f"Could not load the model: {e}") 
    st.stop()

# Application title 
st.title("Telco Customer Churn Prediction")
st.header("Model Performance")

col1, col2, col3 = st.columns(3)

col1.metric("Accuracy", "73.81%")
col2.metric("Recall", "78.34%")
col3.metric("F1 Score", "61.36%")
st.write( 
    "Enter the customer's details to predict whether " 
    "they are likely to leave the company." 
)

# Customer information 
st.header("Customer Information") 

col1, col2 = st.columns(2) 
with col1: 
    gender = st.selectbox( 
     "Gender", 
     ["Male", "Female"] 
    ) 
    
    senior_citizen = st.selectbox( 
        "Senior Citizen", 
        [0, 1], 
        format_func=lambda x: "Yes" if x == 1 else "No" 
    ) 
    
    partner = st.selectbox( 
        "Has Partner?", 
        ["Yes", "No"] 
    ) 
    
    dependents = st.selectbox( 
        "Has Dependents?", 
        ["Yes", "No"] 
    ) 
    
    tenure = st.number_input( 
        "Tenure (months)", 
        min_value=0, 
        max_value=100, 
        value=12 
    ) 
    
    phone_service = st.selectbox( 
        "Phone Service", 
        ["Yes", "No"] 
    ) 
    
    multiple_lines = st.selectbox( 
        "Multiple Lines", 
        ["Yes", "No", 
         "No phone service"] 
    ) 
    
    internet_service = st.selectbox( 
        "Internet Service", 
        ["DSL", "Fiber optic", "No"] 
    ) 
    
    online_security = st.selectbox( 
        "Online Security", 
        ["Yes", "No", "No internet service"] 
    )

with col2: 
    online_backup = st.selectbox( 
        "Online Backup", 
        ["Yes", "No", "No internet service"] 
    ) 
    
    device_protection = st.selectbox( 
        "Device Protection", 
        ["Yes", "No", "No internet service"] 
    ) 
    
    tech_support = st.selectbox( 
        "Tech Support", 
        ["Yes", "No", "No internet service"] 
    ) 
    
    streaming_tv = st.selectbox( 
        "Streaming TV", 
        ["Yes", "No", "No internet service"] 
    ) 
    
    streaming_movies = st.selectbox( 
        "Streaming Movies", 
        ["Yes", "No", "No internet service"] 
    ) 
    
    contract = st.selectbox( 
        "Contract", 
        ["Month-to-month", "One year", "Two year"] 
    ) 
    
    paperless_billing = st.selectbox( 
        "Paperless Billing", 
        ["Yes", "No"] 
    ) 
    
    payment_method = st.selectbox( 
        "Payment Method", 
        [ "Electronic check", 
         "Mailed check", 
         "Bank transfer (automatic)", 
         "Credit card (automatic)" 
        ] 
    ) 
    
    monthly_charges = st.number_input( 
        "Monthly Charges", 
        min_value=0.0, 
        value=70.0 
    ) 
    
    total_charges = st.number_input( 
        "Total Charges", 
        min_value=0.0, 
        value=840.0 
    ) 
    
# Create the input DataFrame 
customer_data = pd.DataFrame([{ 
    "gender": gender, 
    "SeniorCitizen": senior_citizen, 
    "Partner": partner, 
    "Dependents": dependents, 
    "tenure": tenure, 
    "PhoneService": phone_service, 
    "MultipleLines": multiple_lines, 
    "InternetService": internet_service, 
    "OnlineSecurity": online_security, 
    "OnlineBackup": online_backup, 
    "DeviceProtection": device_protection, 
    "TechSupport": tech_support, 
    "StreamingTV": streaming_tv, 
    "StreamingMovies": streaming_movies, 
    "Contract": contract, 
    "PaperlessBilling": paperless_billing, 
    "PaymentMethod": payment_method, 
    "MonthlyCharges": monthly_charges, 
    "TotalCharges": total_charges 
}])

# Predict churn 

if st.button("Predict Customer Churn"):
    try:
        prediction = model.predict(customer_data)[0]
        probabilities = model.predict_proba(customer_data)[0]

        classes = list(model.classes_)
        churn_index = classes.index("Yes")
        churn_probability = probabilities[churn_index] * 100

        st.subheader("Prediction Result")

        if prediction == "Yes":
            st.error("This customer is predicted to churn.")
        else:
            st.success("This customer is predicted to stay.")

        st.metric(
            "Churn Probability",
            f"{churn_probability:.2f}%"
        )

        st.progress(float(churn_probability / 100))
        st.subheader("Business Recommendations")

        if churn_probability >= 70:
            st.warning("High churn risk: Take action to retain this customer.")
            st.write("- Offer a suitable loyalty discount.")
            st.write("- Contact the customer to understand their concerns.")
            st.write("- Explain the benefits of a long-term contract.")
    
        elif churn_probability >= 40:
            st.info("Medium churn risk: Monitor this customer.")
            st.write("- Check customer satisfaction.")
            st.write("- Offer suitable support or service options.")
    
        else:
            st.success("Low churn risk: Continue regular customer engagement.")
            st.write("- Maintain good customer service.")
            st.write("- Continue monitoring customer satisfaction.")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
