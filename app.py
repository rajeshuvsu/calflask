from flask import Flask,request,render_template,jsonify
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
        result = int(num1) + int(num2)
    elif operations == 'multiply':
        result = int(num1) * int(num2)
    elif operations == 'division':
        result = int(num1) / int(num2)
    else:
        result = int(num1) - int(num2)

    return "the operation is {} and the result is {}".format(operations,result)


if __name__ == "__main__":
    app.run(debug = True)