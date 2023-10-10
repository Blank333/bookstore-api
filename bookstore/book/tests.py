from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import Book


class BookTestCaseCreate(APITestCase):

    # Setup base data for the test requests
    def setUp(self):
        # Create a test client using Rest Frameworks inbuilt testing capabilities
        self.client = APIClient()

        # Sample test data
        self.data = {
            "title": "Test Book",
            "author": "Test Author",
            "genre": "Test Genre",
            "price": 9.99
        }
        self.url = '/api/v1/books/'

    # Testing book object creation

    # Verifies if a book can be successfully created
    def test_create_book(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')

    # Verifies that creating a book without a title, author or price is not possible
    def test_create_book_without_title(self):
        data = self.data
        data.pop('title')
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_book_without_author(self):
        data = self.data
        data.pop('author')
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_book_without_price(self):
        data = self.data
        data.pop('price')
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Verifies that creating a book without a genre is possible
    def test_create_book_without_genre(self):
        data = self.data
        data.pop('genre')
        response = self.client.post(self.url, self.data)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Verifies that creating a book with a negative price, non-integer price, or a high price (>9999.99) is not possible
    def test_create_book_with_negative_price(self):
        data = self.data
        data['price'] = -10
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_book_with_high_price(self):
        data = self.data
        data['price'] = 10000
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_book_with_noninteger_price(self):
        data = self.data
        data['price'] = 'Not Integer'
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class BookTestCaseRead(APITestCase):
    def setUp(self):
        # Create a test client using Rest Frameworks inbuilt testing capabilities
        self.client = APIClient()

        # Sample test data
        self.book = Book.objects.create(
            title="Test Boo1k", author="Test Author", genre="Test Genre", price=9.99)
        Book.objects.create(
            title="Test Book2", author="Test Author", genre="Test Genre", price=9.99)
        Book.objects.create(
            title="Test Book3", author="Test Author", genre="Test Genre", price=9.99)
        Book.objects.create(
            title="Test Book4", author="Test Author", genre="Test Genre", price=9.99)
        self.url = '/api/v1/books/'

    # Testing books read

    # Verifies if books returns  the correct number of books
    def test_retrieve_book(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 4)

    # Verifies that retrieving details of a book by ID works
    def test_retrieve_book_detail(self):
        response = self.client.get(f'{self.url}{self.book.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Verifies that retrieving a non-existent book is not possible
    def test_retrieve_book_detail_not_exsist(self):
        response = self.client.get(f'{self.url}1000/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BookTestCaseUpdate(APITestCase):

    def setUp(self):
        # Create a test client using Rest Frameworks inbuilt testing capabilities
        self.client = APIClient()

        # Sample test data
        self.book = Book.objects.create(
            title="Test Book", author="Test Author", genre="Test Genre", price=9.99)

        self.url = '/api/v1/books/'

    # Testing book update

    # Verifies if a book can be successfully updated with new data
    def test_update_book(self):
        updated_data = {
            "title": "Updated Book Title",
            "author": "Updated Author",
            "genre": "Updated Genre",
            "price": 14.99
        }
        response = self.client.put(f'{self.url}{self.book.pk}/', updated_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get().title, 'Updated Book Title')
        self.assertEqual(Book.objects.get().author, 'Updated Author')
        self.assertEqual(Book.objects.get().genre, 'Updated Genre')

    # Verifies that updating a book without a title, author or price is not possible
    def test_update_book_without_title(self):
        updated_data = {
            "title": "",
            "author": "Updated Author",
            "genre": "Updated Genre",
            "price": 14.99
        }
        response = self.client.put(f'{self.url}{self.book.pk}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_book_without_author(self):
        updated_data = {
            "title": "Updated Book Title",
            "author": "",
            "genre": "Updated Genre",
            "price": 14.99
        }
        response = self.client.put(f'{self.url}{self.book.pk}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_book_without_price(self):
        updated_data = {
            "title": "Updated Book Title",
            "author": "Updated Author",
            "genre": "Updated Genre",
        }
        response = self.client.put(f'{self.url}{self.book.pk}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Verifies that updating a non-existent book is not possible
    def test_update_book_not_exsist(self):
        response = self.client.put(f'{self.url}1000/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BookTestCaseDelete(APITestCase):

    def setUp(self):
        # Create a test client using Rest Frameworks inbuilt testing capabilities
        self.client = APIClient()

        # Sample test data
        self.book = Book.objects.create(
            title="Test Book", author="Test Author", genre="Test Genre", price=9.99)

        self.url = '/api/v1/books/'

    # Testing book deletion

    # Verifies if a book can be successfully deleted
    def test_delete_book(self):
        response = self.client.delete(f'{self.url}{self.book.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # Verifies that trying to delete a non-existent book is not possible
    def test_delete_book_not_exsist(self):
        response = self.client.delete(f'{self.url}1000/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
