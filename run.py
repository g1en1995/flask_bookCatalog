from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config.update(
    SECRET_KEY='',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:0820@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)


# Hello flask through app routing!
'''
@app.route('/index')
@app.route('/')
def hello_flask():
    return 'hello_flask!'
'''

# examples of different routes and requests and rendering html templates
'''   
@app.route('/new/')
def query_strings(greetings='hello'):
    val = request.args.get('greetings', greetings)
    return (f'<h1> Hi! the greeting is {val} </h1>')

@app.route('/user')
@app.route('/user/<name>')
def new_query(name="wowza"):
    return f'<h1> Hi this is a new greeting {name} </h1>'

@app.route('/temp')
def htmlfiles():
    return render_template('hello.html')
'''

# route and function to take in extra data for implementing dictionaries using jinja2 for loops and if..elif..else.
'''@app.route('/movies')
def movies_plus():

    movies = {
        'Dark Knight': 5,
        'Die Hard 4': 4,
        'Hera Pheri': 4.5,
        'Hangover': 4.8,
        'Scary Movie': 1,
        'Harry Potter 3': 3.5
    }

    return render_template('movies_plus.html', movies=movies, name="Glen")
'''

# Publication of the book table
class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self,  name):
        self.name = name

    def __repr__(self):
        return f"the name is {self.name}"

# Book table
class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(100))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(200), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # Establishing a relationship between publication and book tables
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, format, image, num_pages,pub_id):
        self.title=title
        self.author=author
        self.avg_rating=avg_rating
        self.format=format
        self.image=image
        self.num_pages=num_pages
        self.pub_id=pub_id

    def __repr__(self):
        return f" the author is {self.author} and the book is {self.title}"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)