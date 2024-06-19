from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


import sqlite3
con = sqlite3.connect("Library.db", check_same_thread=False)
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Books (
    id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Author TEXT NOT NULL,
    Year_Published INTEGER NOT NULL,
    Type INTEGER NOT NULL CHECK (Type IN (1, 2, 3))
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    City TEXT NOT NULL,
    Age INTEGER NOT NULL
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Loans (
    CustID INTEGER NOT NULL,
    BookID INTEGER NOT NULL,
    LoanDate TEXT NOT NULL,
    ReturnDate TEXT,
    FOREIGN KEY (CustID) REFERENCES Customers(id),
    FOREIGN KEY (BookID) REFERENCES Books(id),
    PRIMARY KEY (CustID, BookID)
)
''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_book', methods=['POST'])
def add_book():
    name = request.form['Name']
    author = request.form['Author']
    year_published = request.form['Year_Published']
    book_type = request.form['Type']
    cur.execute("INSERT INTO Books (Name, Author, Year_Published, Type) VALUES (?, ?, ?, ?)", 
                (name, author, year_published, book_type))
    con.commit()
    return redirect(url_for('index'))

@app.route('/add_customer', methods=['POST'])
def add_customer():
    name = request.form['Name']
    city = request.form['City']
    age = request.form['Age']
    cur.execute("INSERT INTO Customers (Name, City, Age) VALUES (?, ?, ?)", 
                (name, city, age))
    con.commit()
    return redirect(url_for('index'))

@app.route('/add_loan', methods=['POST'])
def add_loan():
    cust_id = request.form['CustID']
    book_id = request.form['BookID']
    loan_date = request.form['LoanDate']
    return_date = request.form['ReturnDate']
    cur.execute("INSERT INTO Loans (CustID, BookID, LoanDate, ReturnDate) VALUES (?, ?, ?, ?)", 
                (cust_id, book_id, loan_date, return_date))
    con.commit()
    return redirect(url_for('index'))

# Добавляем маршрут для отображения всех книг
@app.route('/books')
def show_books():
    cur.execute("SELECT * FROM Books")
    books = cur.fetchall()
    return render_template('show_books.html', books=books)

# Добавляем маршрут для отображения всех клиентов
@app.route('/customers')
def show_customers():
    cur.execute("SELECT * FROM Customers")
    customers = cur.fetchall()
    return render_template('show_customers.html', customers=customers)

# Добавляем маршрут для отображения всех займов
@app.route('/loans')
def show_loans():
    cur.execute('''
        SELECT Loans.CustID, Customers.Name, Loans.BookID, Books.Name, Loans.LoanDate, Loans.ReturnDate
        FROM Loans
        JOIN Customers ON Loans.CustID = Customers.id
        JOIN Books ON Loans.BookID = Books.id
    ''')
    loans = cur.fetchall()
    return render_template('show_loans.html', loans=loans)

# Добавляем маршрут для удаления книги
@app.route('/delete_book/<int:id>', methods=['POST'])
def delete_book(id):
    cur.execute("DELETE FROM Books WHERE id=?", (id,))
    con.commit()
    return redirect(url_for('show_books'))

# Добавляем маршрут для удаления клиента
@app.route('/delete_customer/<int:id>', methods=['POST'])
def delete_customer(id):
    cur.execute("DELETE FROM Customers WHERE id=?", (id,))
    con.commit()
    return redirect(url_for('show_customers'))

# Добавляем маршрут для удаления займа
@app.route('/delete_loan/<int:cust_id>/<int:book_id>', methods=['POST'])
def delete_loan(cust_id, book_id):
    cur.execute("DELETE FROM Loans WHERE CustID=? AND BookID=?", (cust_id, book_id))
    con.commit()
    return redirect(url_for('show_loans'))

# Добавляем маршруты для редактирования книги, клиента и займа
@app.route('/edit_book/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    if request.method == 'POST':
        name = request.form['Name']
        author = request.form['Author']
        year_published = request.form['Year_Published']
        book_type = request.form['Type']
        cur.execute('''
            UPDATE Books
            SET Name=?, Author=?, Year_Published=?, Type=?
            WHERE id=?
        ''', (name, author, year_published, book_type, id))
        con.commit()
        return redirect(url_for('show_books'))
    else:
        cur.execute("SELECT * FROM Books WHERE id=?", (id,))
        book = cur.fetchone()
        return render_template('edit_book.html', book=book)

@app.route('/edit_customer/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    if request.method == 'POST':
        name = request.form['Name']
        city = request
        city = request.form['City']
        age = request.form['Age']
        cur.execute('''
            UPDATE Customers
            SET Name=?, City=?, Age=?
            WHERE id=?
        ''', (name, city, age, id))
        con.commit()
        return redirect(url_for('show_customers'))
    else:
        cur.execute("SELECT * FROM Customers WHERE id=?", (id,))
        customer = cur.fetchone()
        return render_template('edit_customer.html', customer=customer)
    
@app.route('/edit_loan/<int:cust_id>/<int:book_id>', methods=['GET', 'POST'])
def edit_loan(cust_id, book_id):
    if request.method == 'POST':
        loan_date = request.form['LoanDate']
        return_date = request.form['ReturnDate']
        cur.execute('''
            UPDATE Loans
            SET LoanDate=?, ReturnDate=?
            WHERE CustID=? AND BookID=?
        ''', (loan_date, return_date, cust_id, book_id))
        con.commit()
        return redirect(url_for('show_loans'))
    else:
        cur.execute('''
            SELECT * FROM Loans WHERE CustID=? AND BookID=?
        ''', (cust_id, book_id))
        loan = cur.fetchone()
        return render_template('edit_loan.html', loan=loan)
                
if __name__ == '__main__':
    app.run(debug=True, port=8000)
