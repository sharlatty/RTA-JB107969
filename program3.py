from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('name', '')
    return f"Hello {name}!" if name else "Hello!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
