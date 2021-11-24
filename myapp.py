import yfinance as yf
import streamlit as st

st.write("""
## TSLA analysis
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'TSLA'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-10-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

# tickerData.info
# info on the company
# tickerData.splits
st.write("""
## TSLA news
""")
tickerData.news
st.write("""
## Recommendation by experts
""")
tickerData.recommendations
# get recommendation data for ticker
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume 
""")
st.line_chart(tickerDf.Volume)
