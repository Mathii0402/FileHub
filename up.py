# from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename
# app = Flask(__name__)

# @app.route('/upload',methods=["POST","GET"])
# def upload_file():
#    if request.method == 'POST':
#         f = request.files['file']
#         if f.filename != "":
#             f.save(secure_filename(f.filename))
#             return 'file uploaded successfully'
#         return 'file not uploaded'
#    return render_template('upload.html')

		
# if __name__ == '__main__':
#    app.run(debug = True,port=5052)
import os,subprocess

# get the current working directory
# current_working_directory = ""
# print(os.getcwd())

# print output to the console
# print(current_working_directory)

# proc = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE,stdout=subprocess.PIPE)
# stdout,stderr = proc.communicate('dir c:\\')
# stdout
# /home/mathi/django/FileHub/templates
# os.path.expanduser('~/django/FileHub/server.py')
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return 'Hello World'

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run(port=8002,host='0.0.0.0',debug=True)
    