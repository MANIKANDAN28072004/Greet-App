from flask import Flask,render_template,request, flash

app = Flask(__name__)
app.secret_key="dbaiadadda da  duahd "

@app.route("/hello")
def index():
    flash("What's Your Sex?")
    return render_template("index.html")
@app.route("/greet",methods=["POST","GET"])   
def greet():
    request.form['name_input']
    flash("Since you are "+str(request.form['name_input'])+"You can access my website for free :)")
    return render_template("index.html")
