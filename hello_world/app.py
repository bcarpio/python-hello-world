from flask import Flask, render_template, redirect, make_response, Response, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    hello = {'Who' : 'Joe', 'What': 'The Shit'}
    return jsonify(hello)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
