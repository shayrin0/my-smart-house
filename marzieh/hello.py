from flask import Flask 	#import flask

app = Flask(__name__) 		#creat instance of a flask web app

@app.route("/") 			#creat first route(path)
def home():					#return value(will be displayed on web page)
	return "Hello World!"

if __name__ =="__main__"	#run the app
	app.run()
