from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'jzlkgajlgzhgr#22'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(200), nullable=False)
    course_name = db.Column(db.String(200), nullable=False)
    course_cradit = db.Column(db.Integer, nullable=False)
    got_marks = db.Column(db.Integer, nullable=False)

    def __repr__(self, course_code, course_name, course_cradit, got_marks):
        self.course_code = course_code
        self.course_name = course_name
        self.course_cradit = course_cradit
        self.got_marks = got_marks

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
