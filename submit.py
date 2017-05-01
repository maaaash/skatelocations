from flask import Flask
from flask import render_template
from flask import request

app = Flask("MyApp")


@app.route ("/")
def hello():
	return render_template("submit.html")


@app.route("/<name>")
def hello_someone(name):
	return render_template("submit.html", name=name.title())

@app.route("/goodbye/<name>")
def goodbye_someone(name):
	return render_template("submit.html", goodbye=name.title())

@app.route("/submit", methods=['POST'])
def submit():
	form_data = request.form
	print (form_data ['name'])
	print (form_data ['location'])
	print (form_data ['length'])
	return "Thanks for submitting this location"


app.run()
