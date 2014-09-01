from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Wally Really Is Dope"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
