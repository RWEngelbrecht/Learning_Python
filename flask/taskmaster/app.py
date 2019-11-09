from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskmaster.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	# /// for relative path //// for absolute path
db = SQLAlchemy(app)

class Todo(db.Model):		#instanciate database
	id = db.Column(db.Integer, primary_key=True)	#set columns
	content = db.Column(db.String(250), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<Task %r>' % self.id


@app.route('/')
def index():
	return render_template('index.html') #render html with jinja2 function
										 #file should be in templates folder

@app.route('/modal/<int:score>')		#bind functions to specific url with route()
def hello(score):
	return render_template('modal_score.html', marks = score)

if __name__ == "__main__":
	app.run(debug=True)
