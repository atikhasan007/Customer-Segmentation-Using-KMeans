import streamlit as st
import numpy as np
import pickle


#Load Train Kmeans Model
kmeans = pickle.open('kmeans.pkl','rb')


#simple clustering function
def clustering(age, avg_spend, visit_per_week, promotion_interest):
    # 1st array te convert korte hobe
    new_customer = np.array([[age, avg_spend, visit_per_week, promotion_interest]])

    # 2nd train by model
    predicted_cluster = kmeans.predict(new_customer)

    if predicted_cluster[0] == 0:
        return "Promotion"
    elif predicted_cluster[0] == 1:
        return "Irregular"
    elif predicted_cluster[0] == 2:
        return "Weekend"
    else:
        return "Daily"


#streamlit app is here
st.title("Customer Clustomer Details")
st.write("Enter Customer Details")


#row1
col1, col2  = st.columns(2)

with col1:
    st.subheader("Customer Age")
    age = st.number_input("Age",min_value=18, max_value=100, value=40)



with col2:
    st.subheader("Customer Spent Time")
    average_spend = st.number_input("Average Spend",min_value=0.0, max_value=1000.0, value=30.0)


#row2
col1, col2  = st.columns(2)

with col1:
    st.subheader("Visits Per Week")
    visit_per_week = st.number_input("Visits Per Week",min_value=0, max_value=20, value=4)



with col2:
    st.subheader("Promotion Interest")
    promotion_interest = st.number_input("Promotion Interest",min_value=0, max_value=10, value=7)


#predict button
if st.button("Predicted Cluster"):
    cluster_label = clustering(age,average_spend,visit_per_week, promotion_interest)
    st.success(f'The customer belongs to the "{cluster_label}" cluster.')
