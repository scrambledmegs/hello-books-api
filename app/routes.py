from flask import Blueprint, jsonify

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, 'Something Borrowed', 'Romance Novel'),
    Book(2, 'Harry Potter and The Goblet of Fire', 'Fantasy'),
    Book(3, 'Think Like a Man, Act Like a Lady', 'Self Help')
]

books_bp = Blueprint("books", __name__, url_prefix = "/books")
@books_bp.route("", methods = ["GET"])

def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        }), 200
    return jsonify(books_response)

@books_bp.route("/<book_id>", methods = ["GET"])
def handle_book(book_id):

    try:
        book_id = int(book_id)
    except:
        return {"message": f"book {book_id} invalid"}, 400

    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }, 200

    return {"message":f"book {book_id} not found"}, 404
