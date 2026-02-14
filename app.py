import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///books.db")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)

# Create tables and seed data
with app.app_context():
    db.create_all()
    
    # Add sample data only if database is empty
    if Book.query.count() == 0:
        sample_books = [
            Book(title="DevOps Fundamentals"),
            Book(title="Mastering CI/CD"),
            Book(title="Flask for Beginners")
        ]
        db.session.add_all(sample_books)
        db.session.commit()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to BookStore API"})

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{"id": b.id, "title": b.title} for b in books])

# Add new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
