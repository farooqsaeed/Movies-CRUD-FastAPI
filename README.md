# Movies CRUD APIs

## Introduction
This project provides CRUD (Create, Read, Update, Delete) APIs for managing movies. It allows users to perform various operations such as adding new movies, retrieving movie details, updating existing movies, and deleting movies from the database.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/movies-crud-apis.git
    ```

2. Navigate to the project directory:
    ```
    cd movies-crud-apis
    ```

3. Create a virtual environment:
    ```
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```
        source venv/bin/activate
        ```

5. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage
To run the Movies CRUD APIs, execute the following command:

uvicorn main:app --reload

This will start the server locally, and you can access the API documentation at `http://localhost:8000/docs`.

## Endpoints
- `GET /movies`: Retrieve a list of all movies.
- `GET /movie/{movie_id}`: Retrieve details of a specific movie by ID.
- `GET /movie_by_title/{movie_title}`: Retrieve details of a specific movie by title.
- `POST /movie`: Add a new movie to the database.
- `PUT /update/movie/{movie_id}`: Update details of a specific movie by ID.
- `DELETE /movie/{movie_id}`: Delete a movie from the database by ID.
