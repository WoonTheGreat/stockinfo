import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
## TSLA analysis
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'TSLA'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-12-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
df1 = tickerData.recommendations
df2 = tickerData.news


# tickerData.info
# info on the company
# tickerData.splits
st.write("""
## TSLA news
""")
st.table(df2)

st.write("""
## Recommendation by experts
""")
df1
# get recommendation data for ticker
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume 
""")
st.line_chart(tickerDf.Volume)
