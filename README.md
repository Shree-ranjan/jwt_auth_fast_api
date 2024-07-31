# JWT Auth Server

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Shree-ranjan/jwt_auth_fast_api.git
    cd jwt_auth_fast_api
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure the MySQL database:
    ```python
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{DB_USER}:%s@{DB_HOST}:{DB_PORT}/{DB_NAME}" % quote_plus(DB_PASSWORD)
    use details from .env file
    ```

5. Create the database tables:
    ```bash
    cd core
    python database.py
    ```

6. Run the application:
    ```bash
    uvicorn main:app --reload
    ```

## Endpoints

- `POST /api/v1/register-user`: Register a new user.
- `POST /api/v1/auth/login`: Login and get a JWT token.
- `GET /api/v1/me`: Get the current user's profile.

## Documentation

API documentation is available at `/docs`.
