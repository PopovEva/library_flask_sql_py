# Library Management System

A simple Library Management System built with Flask and SQLite. This application allows users to manage books, customers, and loans within a library.

## Features

- Add, view, update, and delete books
- Add, view, update, and delete customers
- Add, view, update, and delete loan records
- User-friendly interface with forms for each action
- Responsive and clean design using CSS

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLite

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    cd library-management-system
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python app.py
    ```

5. Open your web browser and navigate to `http://127.0.0.1:8000`

### Project Structure

library-management-system/  
│  
├── static/  
│ └── styles.css  
│  
├── templates/  
│ ├── layout.html  
│ ├── index.html  
│ ├── books.html  
│ ├── customers.html  
│ ├── loans.html  
│ ├── edit_book.html  
│ ├── edit_customer.html  
│ └── edit_loan.html  
│  
├── app.py  
└── requirements.txt  

### Routes

- `/` - Home page with forms to add books, customers, and loans
- `/books` - View all books
- `/customers` - View all customers
- `/loans` - View all loans
- `/edit_book/<id>` - Edit a specific book
- `/edit_customer/<id>` - Edit a specific customer
- `/edit_loan/<cust_id>/<book_id>` - Edit a specific loan
- `/delete_book/<id>` - Delete a specific book
- `/delete_customer/<id>` - Delete a specific customer
- `/delete_loan/<cust_id>/<book_id>` - Delete a specific loan

### Usage

- To **add a book**, fill in the form on the home page and submit.
- To **view all books**, click the "Show all books" button on the home page.
- To **edit or delete a book**, navigate to the "Show all books" page, and use the provided buttons.
- To **add a customer**, fill in the form on the home page and submit.
- To **view all customers**, click the "Show all customers" button on the home page.
- To **edit or delete a customer**, navigate to the "Show all customers" page, and use the provided buttons.
- To **add a loan**, fill in the form on the home page and submit.
- To **view all loans**, click the "Show all loans" button on the home page.
- To **edit or delete a loan**, navigate to the "Show all loans" page, and use the provided buttons.

### Customization

To customize the styles, edit the `static/styles.css` file.

### License

This project is licensed under the MIT License.

### Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [SQLite](https://www.sqlite.org/index.html) - Database engine