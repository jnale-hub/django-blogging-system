# Django Blogging System

A Django-based blogging system with API support for managing posts and comments.

## Setup

1. Clone the repository.
2. Create and activate a virtual environment:
3. Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```
4. Apply migrations and seed the database:
  ```sh
  python manage.py makemigrations
  python manage.py migrate
  python manage.py seed
  ```
5. Run the development server:
  ```sh
  python manage.py runserver
  ```

## Running Tests

To run the tests, use the following command:
```sh
pytest
```
