from flask import Flask, request, jsonify


# flask application instance
app = Flask(__name__)

@app.route('/')
def function():
    return "Hi"

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    length = len(str(n))
    copy_n = n
    while(n > 0):
        digit = n % 10
        sum += digit ** length
        n = n // 10

    if(sum == copy_n):
        print(f"{copy_n} is an armstrong number")
        result = {
            "Number" : copy_n,
            "Armstrong Number" : True,
            "URL": "http://127.0.0.1:5000",
            "Other Number" : [1, 9, 153, 370, 371, 407]
        }
    else:
        print(f'{copy_n} is not an armstrong number')
        result = {
            "Number" : copy_n,
            "Armstrong Number" : False,
            "URL": "http://127.0.0.1:5000",
            "Other Number" : [10, 70, 30, 550, 661]
        }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)