#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
    pass

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print (parameter)
    return f'{parameter}'
    pass

@app.route('/count/<int:parameter>')
def count(parameter):
    count= ""
    for number in range(parameter):
        print (f'{number}')
        count = (count + str(number) + "\n")
    return count
    pass

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1,operation,num2):
    result = ""
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    else:
        result = num1 % num2
    return str(result)

    #result = eval(f'{num1} {operation} {num2}')
    #return result
    pass

if __name__ == '__main__':
    app.run(port=5555, debug=True)
