# Progress 2: Simple LMS - Database Design & ORM Implementation

Project ini merupakan aplikasi Simple Learning Management System (LMS) berbasis Django yang dijalankan menggunakan Docker dan menggunakan PostgreSQL sebagai database.

---

## 🚀 Cara Menjalankan Project

Ikuti langkah-langkah berikut untuk menjalankan project dari awal:

### 1. Clone repository

```bash
git clone https://github.com/hafizh1119/simple-lms2
```

---
### 2. Menjalankan Docker

```bash
docker-compose up -d --build
```

---
### 3. Migration Database

```bash
docker-compose exec web python manage.py migrate
```

---
### 4. Load Initial Data (Fixtures)

```bash
docker-compose exec web python manage.py loaddata fixtures/initial_data.json
```

---
### 5. Membuat Superuser

```bash
docker-compose exec web python manage.py createsuperuser
```
username: admin 
password: admin123
---
### 5. Akses Djangon Admin
Buka di browser:
```bash
http://localhost:8000/admin
```
---
## 📁 Project Structure

```bash
simple-lms/
├── config/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── staticfiles/
├── .env
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── README.md
└── requirements.txt
Penjelasan Struktur
```
