Telco Customer Churn Prediction

An end-to-end Data Science and Machine Learning project that predicts customer churn for a telecommunications company. The project analyzes customer information, identifies factors associated with churn, compares machine learning models, and provides an interactive web application for making predictions.

Project Overview

Customer churn occurs when customers stop using a company's services. Identifying customers who are likely to leave can help businesses improve customer satisfaction and develop effective retention strategies.

This project uses customer demographic information, service subscriptions, contract details, and billing information to predict whether a customer is likely to churn.

Objectives
Perform data cleaning and exploratory data analysis (EDA).
Identify customer characteristics associated with churn.
Build and compare machine learning classification models.
Evaluate model performance using appropriate classification metrics.
Develop an interactive web application using Streamlit.
Provide illustrative business recommendations based on predicted churn risk.
Dataset

Dataset: Telco Customer Churn

Source: IBM Telco Customer Churn dataset, commonly distributed through Kaggle.

The dataset contains 7,043 customer records and 21 original columns.

It includes information about:

Customer demographics
Account and service details
Contract types
Payment methods
Monthly and total charges
Customer churn status

The customerID column was excluded from model training because it identifies customers rather than providing a useful customer behavior feature.

Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib
Jupyter Notebook
Streamlit
Project Workflow
1. Data Cleaning and Preparation
Inspected dataset structure and data types.
Checked for missing values and data quality issues.
Examined the TotalCharges column.
Removed the customer identifier from model features.
Separated input features from the target variable.
2. Exploratory Data Analysis (EDA)
Analyzed the distribution of customer churn.
Compared churn rates across contract types and payment methods.
Examined customer tenure and monthly charges.
Investigated relationships between service subscriptions and churn.
Identified customer groups with comparatively high churn rates.
3. Data Preprocessing
Split the data into training and testing sets.
Used median imputation and standardization for numerical features.
Used most-frequent imputation and one-hot encoding for categorical features.
Built preprocessing and modeling pipelines to apply transformations consistently.
4. Model Building

The following classification models were trained and compared:

Logistic Regression
Random Forest Classifier
Balanced Logistic Regression

The models were evaluated with particular attention to identifying customers who actually churn.

5. Model Evaluation

The evaluation included:

Accuracy
Precision
Recall
F1-score
Confusion matrix
Cross-validation

Balanced Logistic Regression was selected as the candidate model because it achieved higher recall for the churn class in the test-set comparison.

6. Streamlit Web Application

The interactive application allows users to enter customer information and receive:

A predicted churn or non-churn result
The estimated probability of churn
An illustrative churn-risk category
Suggested customer-retention actions
A summary of model performance

The application's recommendations are examples for demonstration purposes and should not be treated as validated business policies.

Model Performance

The selected Balanced Logistic Regression model achieved the following results on the held-out test set:

Metric	Score
Accuracy	73.81%
Churn Precision	50.43%
Churn Recall	78.34%
Churn F1-score	61.36%
Interpretation
Accuracy: Approximately 73.81% of test-set predictions were correct.
Precision: Approximately 50.43% of customers predicted to churn actually churned.
Recall: Approximately 78.34% of actual churners were identified by the model.
F1-score: The harmonic mean of precision and recall was approximately 61.36%.

Recall was emphasized because identifying more customers who may leave can help a business investigate retention opportunities. However, the model also produces false-positive predictions, so its results require careful interpretation.

These results are from the project's current evaluation and are not a guarantee of performance on new customer data.

Project Structure
telco-customer-churn-prediction/
│
├── app.py
├── churn_model.pkl
├── requirements.txt
├── README.md
└── telco_customer_churn.ipynb

Note: Replace telco_customer_churn.ipynb with the actual name of your notebook if it differs.

How to Run the Project Locally
Step 1: Clone the Repository
git clone https://github.com/YOUR-USERNAME/telco-customer-churn-prediction.git

Replace YOUR-USERNAME with your GitHub username.

Step 2: Open the Project Directory
cd telco-customer-churn-prediction
Step 3: Install the Required Libraries
pip install -r requirements.txt
Step 4: Run the Streamlit Application
streamlit run app.py

The application should open in your browser. If it does not, follow the local URL displayed in the terminal.

Limitations
The model was trained on a specific telecommunications dataset.
Predictions depend on the quality and representativeness of the training data.
The model may not generalize to other companies or customer populations.
Churn predictions indicate estimated risk, not certainty.
The suggested retention actions have not been validated through a business experiment.
Future Improvements
Tune model hyperparameters and evaluate additional algorithms.
Improve precision while maintaining useful churn recall.
Calibrate predicted probabilities and validate risk thresholds.
Add more detailed visualizations to the dashboard.
Deploy the application for public access.
Monitor performance as new customer data becomes available.
Skills Demonstrated
Data Cleaning
Exploratory Data Analysis
Feature Preprocessing
Classification Modeling
Imbalanced Classification
Model Evaluation
Cross-Validation
Python
Scikit-learn Pipelines
Streamlit Application Development
GitHub Project Documentation
Author

Pratik Gurav

Aspiring Data Scientist | Machine Learning Enthusiast

This project was developed as a Data Science portfolio project to demonstrate practical skills in data analysis, machine learning, model evaluation, and application development.
