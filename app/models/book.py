from app import db

class Book(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    # links it to table name "books" instead of "Book"
    # __tablename__ = "books"
    
    def to_string(self):
        return f'{self.id}: {self.title} Description: {self.description}'

    def to_dict(self):
        book_as_dict = {}
        book_as_dict["id"] = self.id
        book_as_dict["title"] = self.title
        book_as_dict["description"] = self.description

        return book_as_dict
        
    @classmethod
    def from_dict(cls, book_data):
        new_book = Book(
                        title=book_data["title"],
                        description=book_data["description"]
                    )
        return new_book