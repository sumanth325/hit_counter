from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key='thisisnotasecret'

@app.route('/')
def home():
    if 'counter' not in session:
        session['counter']=0
    session['count']+=1
    return render_template('index.html', counter=session['counter'])

@app.route('/addtwo')
def add2():
    session['counter']+=2
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter']=0
    return redirect('/')

@app.route('/resetone')
def reset0():
    session['count']+=1
    return redirect('/')

app.run(debug=True)