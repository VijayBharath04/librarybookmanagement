from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory data store
books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "available": True},
    {"id": 2, "title": "1984", "author": "George Orwell", "available": True}
]

@app.route('/', methods=['GET'])
def menu():
    return jsonify({
        "message": "Welcome to the Library Management System",
        "menu_options": {
            "1. View available books": "/books",
            "2. Add a book": "/add (POST json with title and author)"
        }
    })

@app.route('/books', methods=['GET'])
def view_books():
    # Only return available books
    available_books = [b for b in books if b['available']]
    return jsonify({"available_books": available_books}), 200

@app.route('/add', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({"error": "Missing title or author"}), 400
    
    new_book = {
        "id": len(books) + 1,
        "title": data['title'],
        "author": data['author'],
        "available": True
    }
    books.append(new_book)
    return jsonify({"message": "Book added successfully", "book": new_book}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
