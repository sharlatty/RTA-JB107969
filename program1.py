from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)  # ← Zawsze używaj 127.0.0.1 zamiast localhost
