from flask import Flask, send_file

app = Flask(__name__)

options = {'first thing': "FT",
           'second thing': "ST",
           'third thing': "TT"
       }

@app.route('/')
def index():
    return render_template('index.html', options=options)
