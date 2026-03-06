from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This tells Flask to look inside the 'templates' folder for index.html
    return render_template('index.html')