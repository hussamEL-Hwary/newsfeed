
# News Feed API Project

This project is a simple Flask API that provides endpoints for creating, updating, deleting, and retrieving posts. It uses MySQL as the database and Marshmallow for input validation.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Docker Setup](#docker-setup)


## Project Overview

This API allows users to create, update, delete, and retrieve posts. It ensures that only valid users can create posts by checking the `user_id` against the `User` table in the database. Input data is validated using Marshmallow schemas.

## Features

- Create new posts with user validation.
- Update existing posts.
- Delete posts.
- Retrieve posts by ID.
- Uses environment variables for database configuration.
- Dockerized setup with MySQL.

## Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/hussamEL-Hwary/newsfeed.git
    cd newsfeed
    ```

2. **Create a virtual environment**:

    ```
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file** in the root directory of your project with the following content:

    ```env
    DB_HOST=localhost
    DB_USER=user
    DB_PASSWORD=password
    DB_NAME=db
    ```

5. **Set up the database** using the provided SQL scripts.

## Environment Variables

The application uses the following environment variables for database configuration. Make sure these variables are set correctly in your `.env` file:

- `DB_HOST`: The database host (e.g., `localhost`).
- `DB_USER`: The database username.
- `DB_PASSWORD`: The password for the database user.
- `DB_NAME`: The name of the database.

## Running the Application

To run the Flask application, use the following command:

```bash
flask run or python app.py
```

Ensure that your MySQL server is running and accessible based on the environment variables specified.

## API Endpoints

### 1. Create a Post

- **URL**: `/posts`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "user_id": 1,
        "content": "This is a test post"
    }
    ```
- **Response**:
    - `201 Created`: Post added successfully.
    - `400 Bad Request`: Validation errors or user does not exist.

### 2. Update a Post

- **URL**: `/posts/<post_id>`
- **Method**: `PUT`
- **Request Body**:
    ```json
    {
        "content": "Updated post content"
    }
    ```
- **Response**:
    - `200 OK`: Post updated successfully.
    - `400 Bad Request`: Validation errors.

### 3. Delete a Post

- **URL**: `/posts/<post_id>`
- **Method**: `DELETE`
- **Response**:
    - `200 OK`: Post deleted successfully.
    - `404 Not Found`: Post not found.

### 4. Get a Post

- **URL**: `/posts/<post_id>`
- **Method**: `GET`
- **Response**:
    - `200 OK`: Returns the post details.
    - `404 Not Found`: Post not found.

## Docker Setup

This project includes a Docker setup for running the MySQL database.

### Using Docker Compose

1. **Ensure Docker is installed** on your machine.
2. **Run the following command** in your project directory:

    ```
    docker compose -f docker-compose-feed.yaml -p newsfeed up -d

    ```

This will start the MySQL service as defined in the `docker-compose.yml` file.
