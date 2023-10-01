from flask import Flask,request,render_template
import json

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask"

@app.route('/cal',methods = ['GET','POST'])
def math_ops():
    operations = request.json['operations']
    num1 = request.json['num1']
    num2 = request.json['num2']

    if operations == 'add':
        result = num1 + num2
    elif operations == 'multiply':
        result = num1 * num2
    elif operations == 'division':
        result = num1 / num2
    else:
        result = num1 - num2

    return result


if __name__ == "__main__":
    app.run()