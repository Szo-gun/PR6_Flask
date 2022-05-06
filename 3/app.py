from urllib import request
from flask import render_template
from flask import Flask
from flask import request, redirect

app = Flask(__name__)

@app.route("/me")
def me():
    return render_template ("me.html")

@app.route("/contact", methods=['GET', 'POST']) 
def contact():
    if request.method == 'GET':
        return render_template ("contact.html")
    elif request.method == 'POST':
        print(request.form)
        return redirect("/result")

@app.route("/result")
def result():
    return render_template ("/result.html")

        


