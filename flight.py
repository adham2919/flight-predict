import streamlit as st
import pandas as pd
import joblib
import numpy as np

Model = joblib.load("Model.pkl")
Inputs = joblib.load("Inputs.pkl")

def Predicitons(Airline,Source,Destination,Total_Stops,Additional_Info,day,month,Time_of_Dep,Time_of_Arrival,Duration_in_Minutes):
    pr_df = pd.DataFrame(columns = Inputs)
    pr_df.at[0 ,'Airline' ] = Airline 
    pr_df.at[0 , 'Source'] = Source
    pr_df.at[0 , 'Destination'] = Destination
    pr_df.at[0 ,'Total_Stops' ] = Total_Stops
    pr_df.at[0 , 'Additional_Info'] =Additional_Info
    pr_df.at[0 , 'day' ] =day
    pr_df.at[0 , 'month' ] =month
    pr_df.at[0 , 'Time_of_Dep'] = Time_of_Dep
    pr_df.at[0 , 'Time_of_Arrival'] = Time_of_Arrival
    pr_df.at[0 , 'Duration_in_Minutes'] = Duration_in_Minutes
    prediction = Model.predict(pr_df)
    return prediction[0]


def main():
    st.title("Flight Price Prediction")
    Airline = st.selectbox("Airline" , ['IndiGo', 'Air India' ,'Jet Airways' ,'SpiceJet', 'Multiple carriers' ,'GoAir''Vistara' ,'Air Asia'])
    Source = st.selectbox("Source" ,['Banglore' 'Kolkata', 'Delhi','Chennai' ,'Mumbai'])
    Destination = st.selectbox("Destination" ,['New Delhi', 'Banglore' ,'Cochin' ,'Kolkata', 'Delhi' ,'Hyderabad'] )
    Total_Stops = st.slider("Total_Stops" , min_value=0, max_value=4, value=0, step=1 )
    Additional_Info = st.selectbox("Additional_Info" , ['No info', 'In-flight meal not included', 'No check-in baggage included''Other'])
    day = st.slider("day" ,min_value=1, max_value=31, value=1, step=1 )
    month = st.slider("month" ,min_value=1, max_value=12, value=1, step=1)
    Time_of_Dep = st.selectbox("Time_of_Dep" ,['Night', 'Morning', 'Evening', 'Afternoon'])
    Time_of_Arrival = st.selectbox("Time_of_Arrival",['Night', 'Morning', 'Evening', 'Afternoon'])
    Duration_in_Minutes = st.slider("Duration_in_Minutes" ,min_value=120, max_value=2860, value=500, step=60 )
    if st.button("Predict Price"):
        result = Predicitons(Airline, Source, Destination, Total_Stops, Additional_Info, day, month,  Time_of_Dep, Time_of_Arrival, Duration_in_Minutes)
        st.success(f"Predicted Flight Price: {result:.2f}$")

if __name__ == "__main__":
    main()



    
