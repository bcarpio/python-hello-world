from flask import Flask, render_template, redirect, make_response, Response, jsonify
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    hello = {'Who' : 'Joe', 'What': 'The Shit'}
    r = requests.get("http://ip.jsontest.com/")
    dict = {'data': r.json(), 'text': hello}
    return jsonify(dict)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
