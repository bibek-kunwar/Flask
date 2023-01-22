from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mydb.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/main')
def main():
    return render_template("main.html")


@app.route('/')
def index():
    return render_template("index.html")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        fname = request.form['fname']
        lname = request.form['lname']
        print(email, password, username, lname, fname)
        user = User(username=username, email=email, firstname=fname,
                    lastname=lname, password=password)
        db.session.add(user)
        db.session.commit()
        return ('user resgister sucessfully')
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template('Login page')


if __name__ == '__main__':
    app.run(debug=True)
