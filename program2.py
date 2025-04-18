from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!"

@app.route('/mojastrona')  # ← Nowa podstrona
def moja_strona():
    return "To jest moja strona!"  # ← Nowa odpowiedź

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
