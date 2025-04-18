
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict')
def predict():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    
    return jsonify({
        'prediction': 1 if (num1 + num2) > 5.8 else 0,
        'features': {
            'num1': num1,
            'num2': num2
        }
    })

if __name__ == '__main__':
    app.run()
