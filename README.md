# 💱 Currency Converter API

A RESTful API built with Django and Django REST Framework for currency conversion, custom alert creation, and automatic notifications. The project includes JWT authentication, Google OAuth integration, asynchronous tasks with Celery + Redis, and recurring tasks with `django-crontab`.

[🌍 Live Demo](https://currencyconverterapi-77aca58d0b2f.herokuapp.com/)

---

## ⚙️ Technologies

- Python 3.11
- Django 4.2
- Django REST Framework
- JWT with `dj-rest-auth`
- PostgreSQL
- Celery + Redis
- Django Crontab
- Google OAuth2
- Heroku (Deployment)
- drf-spectacular (API documentation)
- WhiteNoise (static file handling)
- Gunicorn (WSGI server)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/CostaPedroHenrique/currency-converter-api.git
cd currency-converter-api
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements-dev.txt
```

## 🔐 Environment Variables

Create a `.env` file in the root directory and define the following variables:

```env
# Django settings
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# PostgreSQL (Heroku provides this automatically in production)
DATABASE_URL=postgres://your-db-user:your-db-password@your-db-host:your-db-port/ your-db-name (optional)

# Celery + Redis
CELERY_BROKER_URL=redis://default:your-redis-password@your-redis-host:your-redis-port/0

# Google OAuth2 credentials
GOOGLE_CLIENT_ID=your-google-client-id (optional)
GOOGLE_CLIENT_SECRET=your-google-client-secret (optional)
```

## 🚀 Running Locally

```bash
python manage.py migrate
python manage.py runserver
python manage.py crontab add
celery -A currencyConverter worker -l info
```

Once the server is running, the API will be available at:
http://localhost:8000/

## 🧪 API Endpoints

Here are the main endpoints exposed by the Currency Converter API in production:

> 🛡️ All routes require **Bearer Token Authentication**.
> To obtain a token, make a `POST` request to `/api/token/` with `username` and `password`.

- **Transactions**
  `GET/POST/DELETE`:
  [https://currencyconverterapi-77aca58d0b2f.herokuapp.com/api/transactions/](https://currencyconverterapi-77aca58d0b2f.herokuapp.com/api/transactions/)

- **Currency Alerts**
  `GET/POST/PUT/DELETE`:
  [https://currencyconverterapi-77aca58d0b2f.herokuapp.com/api/currency-alerts/](https://currencyconverterapi-77aca58d0b2f.herokuapp.com/api/currency-alerts/)

- **Notifications**
  `GET/PUT`:
  [https://currencyconverterapi-77aca58d0b2f.herokuapp.com/api/notifications/](https://currencyconverterapi-77aca58d0b2f.herokuapp.com/api/notifications/)

- **Token Authentication**
  `POST`:
  [https://currencyconverterapi-77aca58d0b2f.herokuapp.com/api/token/](https://currencyconverterapi-77aca58d0b2f.herokuapp.com/api/token/)
  **Payload Example:**
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
