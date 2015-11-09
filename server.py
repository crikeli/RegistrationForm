from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
app = Flask(__name__)
app.secret_key = 'tiredofsecrets'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/form', methods=['POST'])
def form():
	session ['e-mail'] = request.form ['e-mail']
	session ['first_name'] = request.form ['first_name']
	session ['last_name'] = request.form ['last_name']
	session ['password'] = request.form ['password']
	session ['pwordconfirm'] = request.form ['pwordconfirm']

	if len(request.form['e-mail']) < 1:
		flash('Please fill out all fields!')
	elif len(request.form['first_name']) < 1 :
		flash('Please fill out all fields!')
	elif len(request.form['last_name']) < 1 :
		flash('Please fill out all fields!')
	elif len(request.form['password']) < 1 :
		flash('Please fill out all fields!')
	elif len(request.form['pwordconfirm']) < 1 :
		flash('Please fill out all fields!')
	elif not EMAIL_REGEX.match(request.form['e-mail']):
		flash('e-mail address not valid!')
	elif len(request.form['password']) < 8:
		flash('Passwords must be atleast 8 characters long.')
	elif len(request.form['pwordconfirm']) < 8:
		flash('Passwords must be atleast 8 characters long.')
	elif request.form['password'] != request.form['pwordconfirm']:
		flash('Passwords do not match, please enter again!')
	else:
		flash('Thanks for submitting your information!')
	return redirect('/')

app.run(debug=True)