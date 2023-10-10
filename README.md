# Bookstore RESTful API

This project is built on the Django Rest Framework. It implments a RESTful API for a simple online bookstore. It allows users to perform basic CRUD (Create, Read, Update, Delete) operations on books. The API follows RESTful design principles and is thouroughly tested using Django's inbuilt testing capabilities.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python (3.6+)
- PostgreSQL (15.4+)

### Cloning the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/Blank333/bookstore-api.git
```

### Installing

Navigate to the project directory and install the required packages:

```bash
cd bookstore-api
pip install -r requirements.txt
```
Move to the main directory

```bash
cd bookstore
```

### Database Setup

Apply the migrations to set up the database:

```bash
python manage.py migrate
```

### Creating the Environment file

Create a file named `.env` in the root folder. Below is a sample file, please fill it with your information.

```bash
#Django
DJANGO_SECRET_KEY = ''
DEBUG = True
DJANGO_ALLOWED_HOSTS = 'localhost 127.0.0.1'

#Database
DB_ENGINE = 'django.db.backends.postgresql_psycopg2'
DB_NAME = 'bookstore'
DB_USER = 'user'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_PORT = '5432'
```

### Running the API

Start the development server:

```bash
python manage.py runserver
```

The API should now be running locally. You can access it at `http://localhost:8000`.

## API Endpoints

All API endpoints are available through `/api/v1/`

### Retrieve a list of books

- **Endpoint**: `/books/`
- **Method**: GET
- **Description**: Retrieves a list of all available books in the store.
- **sample curl request**: `curl --location 'http://127.0.0.1:8000/api/v1/books/' \
--header 'Cookie: csrftoken=6CdmaTnTAt5EKd1mGQ3vqIIlT66yY9IM'`

### Retrieve details of a specific book

- **Endpoint**: `/books/{id}/`
- **Method**: GET
- **Description**: Retrieves details of a specific book based on its ID.
- **sample curl request**: `curl --location 'http://127.0.0.1:8000/api/v1/books/1/' \
--header 'Cookie: csrftoken=6CdmaTnTAt5EKd1mGQ3vqIIlT66yY9IM'`

### Add a new book

- **Endpoint**: `/books/`
- **Method**: POST
- **Description**: Adds a new book to the store.
- **sample curl request**: `curl --location 'http://127.0.0.1:8000/api/v1/books/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=6CdmaTnTAt5EKd1mGQ3vqIIlT66yY9IM' \
--data '{
    "title": "Siddhartha",
    "author": "Hermann Hesse",
    "genre": "Philosophical",
    "price": "6.24"
}'`

### Update the details of an existing book

- **Endpoint**: `/books/{id}/`
- **Method**: PUT
- **Description**: Updates the details of an existing book based on its ID.
- **sample curl request**: `curl --location --request PUT 'http://127.0.0.1:8000/api/v1/books/1/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=6CdmaTnTAt5EKd1mGQ3vqIIlT66yY9IM' \
--data '{
    "title": "Romeo and Juliet",
    "author": "William Shakespeare",
    "genre": "Shakespearean tragedy",
    "price": 7.14
}'`

### Delete a book

- **Endpoint**: `/books/{id}/`
- **Method**: DELETE
- **Description**: Deletes a book from the store based on its ID.
- **sample curl request**: `curl --location --request DELETE 'http://127.0.0.1:8000/api/v1/books/6/' \
--header 'Cookie: csrftoken=6CdmaTnTAt5EKd1mGQ3vqIIlT66yY9IM'`

## License

This project is licensed under the [MIT License](LICENSE).
