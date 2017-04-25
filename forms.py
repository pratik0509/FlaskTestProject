
from flask import Flask, request, render_template

host = '127.0.0.1'
port = '5050'

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('testForm.html')
    elif request.method == 'POST':
        return 'Hello' + request.form['name']

if __name__=='__main__':
    app.run(host, port)
