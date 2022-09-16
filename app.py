import pandas as pd
import streamlit as st
import datetime
import pandas_datareader as data
import matplotlib.pyplot as plt




try:

    
    today = datetime.date.today()

    end = str(today)
    st.title("Stock Market Data")

    start = st.text_input("Enter Start Date","2022-09-01")
    
    user_input = st.text_input("Enter Stock Ticker",'AAPL')

    df = data.DataReader(user_input,"yahoo",start,end)

    df = df.reset_index()

    high = max(df["High"])

    st.write("Highest Price of Share in Selected Date Range is",high)


    low =  min(df["Low"])
    st.write("Lowest Price of Share in Selected Date Range is",low)
    
    st.subheader(user_input,"Data")
    st.write(df.head())
    
    st.subheader("Statistical Analysis of Data")
    st.write(df.describe())

    st.subheader("Some Graphical Representation")
    fig = plt.figure(figsize=(12,6))
    plt.plot(df.Close)
    st.pyplot(fig)

except:
    st.write("Please Provide Valid Input")
    st.write("NOTE: For Any Stock Ticker Please Refer : yahoo.com")
    

