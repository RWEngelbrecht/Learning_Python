from flask import Flask, render_template, url_for, request, redirect
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


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		task_content = request.form['newTask']
		new_task = Todo(content=task_content)

		try:
			db.session.add(new_task)
			db.session.commit()
			return redirect('/')
		except:
			return 'Something went horribly wrong!'

	else:
		tasks = Todo.query.order_by(Todo.date_created).all()
		return render_template('index.html', tasks=tasks) #render html with jinja2 function
										 #file should be in templates folder

@app.route('/delete/<int:id>')
def delete(id):
	try:
		

@app.route('/modal/<int:score>')		#bind functions to specific url with route()
def hello(score):
	return render_template('modal_score.html', marks = score)

if __name__ == "__main__":
	app.run(debug=True)
