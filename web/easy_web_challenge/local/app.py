from flask import Flask, request, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    return a / b

def getFlag(a, b):
    if a == 1337 and b == 7331:
        return "FLAG"
    else:
        return "NO FLAG"


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression')

        result = "Error Occurred"

        if '+' in expression:
            expression = expression.split('+')
            result = add(int(expression[0]), int(expression[1]))
        elif '-' in expression:
            expression = expression.split('-')
            result = sub(int(expression[0]), int(expression[1]))
        elif '*' in expression:
            expression = expression.split('*')
            result = mul(int(expression[0]), int(expression[1]))
        elif '/' in expression:
            expression = expression.split('/')
            result = divide(int(expression[0]), int(expression[1]))
        elif '=' in expression:
            if ';' not in expression and 'import' not in expression and ' ' not in expression:
                expression = expression.split('=')
                exec(expression[0] + '=' + expression[1])
            result = "Value set"

        if len(expression) != 2:
            result = "Error Occurred"

        return jsonify({"result": str(result)})
    except Exception as e:
        return jsonify({"error": str(e)})

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0')
