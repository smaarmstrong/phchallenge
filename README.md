## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/smaarmstrong/phchallenge.git
    ```

2. **Create a virtual environment:**

    ```bash
    cd phchallenge/
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    cd phchallenge/ # yes, do it again!
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

8. **Test the application:**

   ```bash
   python manage.py test enclosures
   ```
