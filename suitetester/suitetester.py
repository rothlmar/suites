from flask import Flask, request, render_template, redirect

app = Flask(__name__)

options = {'first thing': "FT",
           'second thing': "ST",
           'third thing': "TT"
       }

@app.route('/')
def index():
    return render_template('index.html', options=options)

@app.route('/suites')
def vals():
    opts = request.args.getlist('options')
    optvals = [_ for _ in opts if _ in options.values()]
    if len(optvals) == 0 or len(opts) != len(optvals):
        return render_template('suites.html', suitestr="ERROR ERROR ERROR")
    return render_template('suites.html', suitestr=':'.join(optvals))

if __name__ == '__main__':
    app.run(debug=True)
