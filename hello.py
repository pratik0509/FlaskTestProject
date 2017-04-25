
from flask import Flask

host = '127.0.0.1'
port = '5050'


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!!"

if __name__=='__main__':
    app.run(host, port)
