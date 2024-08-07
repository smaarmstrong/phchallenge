## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd planning_permission
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file with a new secret key:**

    ```bash
    touch .env
    python -c 'from django.core.management.utils import get_random_secret_key; print(f"SECRET_KEY={get_random_secret_key()}")' >> .env
    ```

5. **Run migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and navigate to `http://localhost:8000/enclosures/check/`.