module skatelocations

from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import csv

app = Flask(__name__, template_folder='templates')


@app.route ("/")
def hello():
	return render_template("map.html")


@app.route("/signup")
def signup_form():
	return render_template("signup2.html")

@app.route("/submit")
def submit_location():
	return render_template("submit2.html")

@app.route("/map")
def map():
	return render_template("map.html")


@app.route('/signup', methods=['POST'])
def signup():
	if request.method == 'POST':
			name = request.form['name']
			contact = request.form['contact']
			county = request.form['county']

			fieldnames = ['name', 'contact', 'county']

			with open('signups.csv','a') as inFile:

				writer = csv.DictWriter(inFile, fieldnames=fieldnames)
				writer.writerow({'name': name, 'contact': contact, 'county': county})

				return render_template ("signupthanks.html")



@app.route('/submit', methods=['POST'])
def submit():
	if request.method == 'POST':
			name = request.form['name']
			location = request.form['location']
			length= request.form['length']

			fieldnames = ['name', 'location', 'length']

			with open('newlocations.csv','a') as inFile:

				writer = csv.DictWriter(inFile, fieldnames=fieldnames)
				writer.writerow({'name': name, 'location': location, 'length': length})

				return render_template ("submitthanks.html")

if __name__ == '__main__':
	app.run()
