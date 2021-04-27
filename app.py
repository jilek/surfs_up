from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'
@app.route('/a')
def goodbye_world():
    return 'Goodbye World'
