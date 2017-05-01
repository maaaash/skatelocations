from flask import Flask
from flask import render_template
from flask import request

app = Flask("MyApp")


@app.route ("/")
def hello():
	return render_template("signup.html")


@app.route("/<name>")
def hello_someone(name):
	return render_template("signup.html", name=name.title())

@app.route("/goodbye/<name>")
def goodbye_someone(name):
	return render_template("signup.html", goodbye=name.title())

@app.route("/signup", methods=['POST'])
def sign_up():
	form_data = request.form
	print (form_data ['name'])
	print (form_data ['email'])
	print (form_data ['waist'])
	print (form_data ['length'])
	return "All OK"


app.run()
