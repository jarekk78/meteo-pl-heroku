import os, urllib, re
from flask import Flask, redirect, url_for

app = Flask(__name__)

def printfile(fname):
	text = ""
	try:
		f = open(fname, 'r')
		text = f.read()
		f.close()
	except IOError:
		text = "File" + sys.argv[1] + "does not exist."
	return text
      
@app.route('/')
def meteo():
	return printfile("index.html")
    
@app.route('/index.html')
def index_html():
	return printfile("index.html")
	
@app.route('/configure.html')
def configure():
	return printfile("configure.html")
	
with app.test_request_context():
	url_for('static', filename='styles.css')
	url_for('static', filename='sticky-footer.css')	
	url_for('static', filename='step1.png')	
	url_for('static', filename='step2.png')	
	url_for('static', filename='step3.png')		