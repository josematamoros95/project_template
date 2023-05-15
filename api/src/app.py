# coding=UTF-8
from flask import Flask

app = Flask(__name__)

@app.route('/index')
def hello_world():
    print("hhhhhhhhhhhhhh")
    return "Hello!"

if __name__ == "__main__":
    app.run(debug=True)
    