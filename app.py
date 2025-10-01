# app.py
from flask import Flask

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return "Welcome to my Flask App 🚀"

# Simple Hello route
@app.route("/hello")
def hello():
    return "Hello, World!"

# Personalized greeting
@app.route("/hello/<name>")
def greet(name):
    return f"Hello, {name.capitalize()} 👋"

# About route
@app.route("/about")
def about():
    return "This app is built with Flask to show multiple routes."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
