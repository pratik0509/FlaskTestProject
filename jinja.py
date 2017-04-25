
from flask import Flask, render_template, request

app = Flask(__name__)

users = {
    'Pratik Jain': {
        'university': 'IIIT-H',
        'year': '1st'
        },
    'Naruto Uzumaki': {
        'university': 'Konoha National Academy',
        'year': 'Genin'
        },
    'Ichigo Kurosaki': {
        'university': 'Unknown',
        'year': 'Unknown'
        }
    }

@app.route('/')
def render():
    return render_template('jinjaTestTemplate.html', data = users)

if __name__=='__main__':
    app.run()
