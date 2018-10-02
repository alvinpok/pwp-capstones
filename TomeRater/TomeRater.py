class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        
    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        

    def __repr__(self):
        return "User {name}, email: {email}, books read: {nos}".format(name = self.name, email = self.email, nos = len(self.books))

    def __eq__(self, other_user):
        pass

    def __hash__(self):
        return hash((self.name))

    def read_book(self, book, rating):
        self.books[book] = rating

    def get_average_rating(self):
        total_rating = 0
        valid_rating = 0
        for rating in self.books.values():
            if rating in range(5):
               total_rating += rating
               valid_rating += 1
        try:       
           return total_rating / valid_rating
        except:
           return 0 
    
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn  = isbn
        self.rating = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
        
    def add_rating(self, rating):
        if rating in range(5):
            self.rating.append(rating)
        else:
            print("Invalid Rating : {rating} for book title: {title}".format(rating = rating,title = self.title)) 

    def get_average_rating(self):
        total_rating = 0
        valid_rating = 0
        for rating in self.rating:
            if rating in range(5):
               total_rating += rating
               valid_rating += 1
        try:       
           return total_rating / valid_rating
        except:
           return 0

    def __repr__(self):
        return "{title}, ISBN : {isbn}".format(title = self.title, isbn = self.isbn)

    
    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level   = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

    
    
class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self,title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        fiction = Fiction(title, author, isbn)
        return fiction

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self, book, email, rating):
        email_found = False
        for user in self.users:
           if user.get_email() == email:
              email_found = True
              user.read_book(book, rating)
              book.add_rating(rating)
              book_found = False 
              for curr_book in self.books:
                  if curr_book == book:
                      book_found = True
                      self.books[book] += 1
              if book_found == False:
                  self.books[book]=1
        if email_found == False:          
           print("No user with email {email}".format(email = email))

    def add_user(self, name, email, user_books = []):
        user = User(name, email)
        self.users.update({user : email})
        for book in user_books:
             self.add_book_to_user(book, email, rating = None)
            
    def print_catalog(self):
        for book in self.books:
           print(book)

    def print_users(self):
        for user in self.users:
           print(user)

    def get_most_read_book(self):
        most_read = 0
        for book in self.books:
            if self.books[book] >= most_read:
                most_read = self.books[book]
                booktitle = book.title
        return "Most read book: {title} : {readnos}".format(title=booktitle, readnos=most_read)

    def most_positive_user(self):
        highest_rate = 0
        for user in self.users:
            if user.get_average_rating() >= highest_rate:
                highest_rate = user.get_average_rating()
                most_positive_user = user
        return "Most positive user: {name}, rating: {rating}".format(name = most_positive_user.name, rating = highest_rate)
            
    def highest_rated_book(self):
        highest_rate = 0
        for book in self.books:
            if book.get_average_rating() >= highest_rate:
                highest_rate = book.get_average_rating()
                highest_rated_book = book
        return "Highest rated book: {name}, rating: {rating}".format(name = highest_rated_book.title, rating = highest_rate)

    def get_n_most_read_books(self, n):
        read_book = {}
        for user in self.users:
            for book in user.books:
                title = book.title
                if title in read_book:
                    read_book[title] += 1
                else:
                    read_book.update({title : 1})
        
        i = n        
        Sorted_book = sorted(read_book.items(), reverse=True, key=lambda x: x[1])
        for elem in Sorted_book :
          if i > 0:  
             print(elem[0] , " ::" , elem[1] )
          i = i - 1
        
        
            
          
    def get_n_most_prolific_readers(self, n):
        book_user = {}
        for user in self.users:
            username = user.name
            book_user[username] = 0
            for book in user.books:
                book_user[username] += 1
        i = n        
        Sorted_users = sorted(book_user.items(), reverse=True, key=lambda x: x[1])
        for elem in Sorted_users :
          if i > 0:  
             print(elem[0] , " ::" , elem[1] )
          i = i - 1

          
            
                
