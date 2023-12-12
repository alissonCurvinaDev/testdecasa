from flask import Flask, render_template, redirect

app = Flask(__name__)

#apenas para teste
logged = True

@app.route('/')
def home():
    if not logged:
        return redirect('/login')
    else:
        return render_template('home.html', name="Alisson")
    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/myAccount')
def myAccount():
    return render_template('myAccount.html')

app.run(debug=True)