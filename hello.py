from flask import Flask, render_template, request
import yfinance as yf
import streamlit as st
from datetime import date 
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Monte Carlo Simulation")
stocks = ("AAPL", "GOOG", "MSFT", "GME")

selected_stocks = st.selectbox("Select dataset for simulation", stocks)
sim_years = st.slider("Years of prediction:", 1 , 10)
period = sim_years * 365

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data
data_load_state = st.text("Load data...")
data = load_data(selected_stocks)
data_load_state.text("Loading data...done")

st.subheader('Raw data')
st.write(data.tail())

def plot_raw_data():
    fig = plot_plotly.figure()
    fig.add_trace(plot_plotly.Scatter(x=data['Date'],y=data['Open'], name='stock_open'))
    fig.add_trace(plot_plotly.Scatter(x=data['Date'],y=data['Close'], name='stock_close'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()
app = Flask(__name__, template_folder='templates')

@app.route("/home")
def home_page():
    return render_template('index.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route('/calculator/', methods=["GET", "POST"])
def calculator_page():

    return render_template("calculator.html")

@app.route("/Steps-to-Follow")
def steps_page():
    return render_template('Steps-to-Follow.html')

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"