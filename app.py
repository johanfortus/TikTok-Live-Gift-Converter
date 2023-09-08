from flask import Flask
from flask import render_template, request, redirect, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "4534gdghjkef5d#$RGR^HDG"

def diamond_converter(amount):
    return 0.005 * amount

@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/results', methods = ['POST'])
def result():
    amount = request.form['amount']

    try:
        convertedAmount = diamond_converter(int(amount))
        formatted = f"{convertedAmount:.2f}"
        return render_template('results.html', convertedAmount = formatted)
    
    except:
        error_message = "Please Enter a Valid Number"
        flash(error_message)
        return redirect('/', )