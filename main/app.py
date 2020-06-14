# we are importing flask class
from flask import Flask 

# creating app variable and settin this to instance 
#of this flask class
app = Flask(__name__) 	

@app.route('/') #our route
@app.route('/home')	
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/about') 	#our route
def about():
    return '<h1>about page</h1>'

#run application directly using python 
#(this conditinal only true if we run this script directly)
if __name__ == '__main__': 
	app.run(debug=True)