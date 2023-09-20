from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
	return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/categories.html")
def categories():
    return render_template("categories.html")

@app.route("/joinus.html")
def joinus():
    return render_template("joinus.html")
