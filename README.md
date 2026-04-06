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
![login](Dokumentasi/docker.png)
---
### 3. Migration Database

```bash
docker-compose exec web python manage.py migrate
```

![login](Dokumentasi/migrate.png)
---
### 4. Load Initial Data (Fixtures)

```bash
docker-compose exec web python manage.py loaddata fixtures/initial_data.json
```

![login](Dokumentasi/Initial_data.png)
---
### 5. Membuat Superuser

```bash
docker-compose exec web python manage.py createsuperuser
```
- username: hafizh 
- password: hafizh123
---

![login](Dokumentasi/create_superuser.png)
### 6. Halaman Login Admin
Buka di browser:
```bash
http://localhost:8000/admin
```
Masukkan 
- username: hafizh 
- password: hafizh123
---
![login](Dokumentasi/login.png)
---
### 7. Dashboard Admin
halaman dashboard admin
ada menu:
- Users
- Courses
- Lessons
- Enrollment
- Progress
```bash
http://localhost:8000/admin
```

![login](Dokumentasi/dashboardAdmin.png)
---
### 8. QUERY OPTIMIZATION
Masuk shell:
```bash
docker-compose exec web python manage.py shell
```
lalu:
```bash
from courses.scripts.query_demo import run
run()
```
![login](Dokumentasi/query_optimization.png)
---
## 📁 Project Structure

```bash
simple-lms2/
├── config/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── courses/
│   ├── __pycache__/
│   ├── migrations/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   ├── scripts/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── query_demo.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── managers.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── fixtures/
│   └── initial_data.json
│
├── staticfiles/
│   └── admin/
│       ├── css/
│       ├── img/
│       └── js/
│
├── .env
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── image.png
├── README.md
└── requirements.txt
```

---

## 📌 Penjelasan Struktur

* **config/** → Konfigurasi utama Django (settings, urls, wsgi)
* **courses/** → Aplikasi utama LMS (models, admin, managers, dll)
* **courses/scripts/** → Script untuk demo query optimization
* **courses/migrations/** → File migrasi database
* **fixtures/** → Data awal (initial data)
* **staticfiles/** → File static (CSS, JS, Image)
* **Dokumentasi/** → Screenshot hasil project
* **.env** → Konfigurasi environment
* **docker-compose.yml** → Konfigurasi multi-container Docker
* **Dockerfile** → Build image Django
* **manage.py** → Command-line Django
* **requirements.txt** → Dependencies project
* **README.md** → Dokumentasi project

```
>>>>>>> 37aa328e88006d20d5cd96aaebdb3fe0764d2143
