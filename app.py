from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'why are you running'

if __name__ == '__main__':
    app.run(debug=True)

