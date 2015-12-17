from flask import Flask, render_template, redirect, make_response, Response, jsonify
import requests
import os
app = Flask(__name__)

@app.route("/")
def hello():
    who =  os.environ.get('WHO')
    what = os.environ.get('WHAT')
    hello = {'Who' : who, 'What': what}
    dict = {'text': hello, 'test':'bob'}
    return jsonify(dict)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
