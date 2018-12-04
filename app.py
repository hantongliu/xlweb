# coding=utf-8

from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def homepage():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
