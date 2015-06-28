from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/about')
def about():
	var aboutus = ''' This webapp is build  for alfahealth project.
	The server side scripting would be done on python.... '''
	return aboutus
