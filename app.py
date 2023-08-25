import pickle
import streamlit as st
import sklearn
import joblib
# pickle_in = open('randomforest.pkl','rb')
# model = pickle.load(pickle_in)
model = pickle.load(open("randomforest.pkl","rb")
# def main():
st.title("Predicting customer churn")

customerID = st.number_input("The Id's of customer's")
gender = st.number_input('The gender of individuals be it male or female')
SeniorCitizen = st.number_input('SeniorCitizen')
Partner = st.number_input('Partner')
Dependents = st.number_input('Dependents')
tenure = st.number_input('tenure') 
PhoneService = st.number_input('PhoneService')
MultipleLines = st.number_input('MultipleLines')
InternetService = st.number_input('InternetService')
OnlineSecurity = st.number_input('OnlineSecurity')
OnlineBackup = st.number_input('OnlineBackup')
DeviceProtection = st.number_input('DeviceProtection')
TechSupport = st.number_input('TechSupport')
StreamingTV = st.number_input('StreamingTV')
StreamingMovies = st.number_input('StreamingMovies')
Contract = st.number_input('Contract')
PaperlessBilling = st.number_input('PaperlessBilling')
PaymentMethod = st.number_input('PaymentMethod')
MonthlyCharges = st.number_input('MonthlyCharges')
TotalCharges = st.number_input('TotalCharges')
submit = st.button('Predict')

#prediction code
  if submit:
        Prediction = model.predict([[customerID, gender, SeniorCitizen, Partner, Dependents,
       tenure, PhoneService, MultipleLines, InternetService,
       OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
       StreamingTV, StreamingMovies, Contract, PaperlessBilling,
       PaymentMethod, MonthlyCharges, TotalCharges]])
        
        if Prediction == 0:
            st.write('There was no Customer churning')
        else:
            st.write("There was Customer churning")
            
            
# if __name__ == '__main__':
#     main()
