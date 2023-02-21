from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route("/home")
def home_page():
    return render_template('index.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/calculator")
def calculator_page():
    return render_template('calculator.html')

@app.route("/Steps-to-Follow")
def steps_page():
    return render_template('Steps-to-Follow.html')