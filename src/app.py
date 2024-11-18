from flask import Flask, request, redirect, render_template
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()  
    return redirect("/")

@app.route("/set", methods=["POST"])
def set_value():
    try:
        input_value = int(request.form["value"])
        cnt.set_value(input_value)
    except ValueError:
        pass  
    return redirect("/")