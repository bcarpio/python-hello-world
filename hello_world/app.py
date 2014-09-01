from flask import Flask, render_template, redirect, make_response, Response
app = Flask(__name__)

@app.route("/")
def hello():
    hello = "Joe Really Is Dope"
    return render_template('index.html',hello=hello)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
