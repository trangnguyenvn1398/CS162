from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/trangnguyenvn1398/Desktop/CS162/cs162/session7_1/KanbanFlask/todo.db'
# app.config['SQLAlCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
db = SQLAlchemy(app)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    to_do = db.Column(db.Boolean)
    doing = db.Column(db.Boolean)
    done = db.Column(db.Boolean)

@app.route('/')

def index():
    to_do = Task.query.filter_by(to_do=True).all()
    doing = Task.query.filter_by(doing=True).all()
    done = Task.query.filter_by(done=True).all()
    return render_template('index.html', to_do = to_do, doing = doing, done = done)

@app.route('/add', methods=['POST'])
def add():
    newtask = Task(text=request.form['newitem'], to_do = True, doing = False, done = False)
    db.session.add(newtask)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/move_to_doing/<id>')
def move_to_doing(id):
    task = Task.query.filter_by(id=int(id)).first()
    task.doing = True
    task.to_do = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/move_to_done/<id>')
def move_to_done(id):
    task = Task.query.filter_by(id=int(id)).first()
    task.doing = False
    task.done = True
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
