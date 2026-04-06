<<<<<<< HEAD
Progress 2: Simple LMS - Database Design & ORM Implementation

⚙️ Setup Project
1. Clone Repository
git clone https://github.com/hafizh1119/simple-lms2
cd simple-lms

2. Jalankan Docker
docker-compose up -d --build

(image.png)

container berhasil running
✅ 3. Migration Database
docker-compose exec web python manage.py migrate

📸 Screenshot:

migration berhasil
✅ 4. Load Initial Data (Fixtures)
docker-compose exec web python manage.py loaddata fixtures/initial_data.json

📸 Screenshot:

muncul:
Installed X object(s)
✅ 5. Membuat Superuser
docker-compose exec web python manage.py createsuperuser

Isi:

username: admin
password: bebas

📸 Screenshot:

proses pembuatan user
✅ 6. Akses Django Admin

Buka di browser:

http://localhost:8000/admin

📸 Screenshot:

halaman admin berisi:
Users
Courses
Lessons
Enrollment
Progress
🗂️ Data Models

Model yang diimplementasikan:

User (admin, instructor, student)
Category (self-referencing)
Course (relasi instructor & category)
Lesson (dengan ordering)
Enrollment (unique constraint)
Progress (tracking completion)
🛠️ Django Admin

Fitur yang diimplementasikan:

List display
Search
Filter
Inline Lesson pada Course
⚡ Query Optimization
🔹 Menjalankan Demo
docker-compose exec web python manage.py shell
from courses.scripts.query_demo import run
run()

📸 Screenshot (WAJIB):

===== N+1 Problem =====
===== Optimized Query =====
===== Course.objects.for_listing() =====
===== Enrollment.objects.for_student_dashboard() =====
📊 Query Comparison
❌ N+1 Problem

Menggunakan:

Course.objects.all()
Total query: (isi dari hasil kamu)
✅ Optimized Query

Menggunakan:

Course.objects.select_related('instructor')
Total query: (isi dari hasil kamu)
🚀 Custom QuerySet
Course.objects.for_listing()
Menggunakan select_related
Query lebih optimal
Enrollment.objects.for_student_dashboard()
Menggunakan select_related dan prefetch_related
Mengurangi jumlah query
🧠 Kesimpulan

Penggunaan:

select_related
prefetch_related
custom QuerySet

mampu:

Mengurangi jumlah query database
Meningkatkan performa aplikasi
Menghindari N+1 problem
📁 Struktur Project
simple-lms/
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── config/
├── courses/
├── fixtures/
├── screenshots/
└── README.md
=======
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
![login](Dokumentasi/login.png)
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
- username: admin 
- password: admin123
---
### 6. Halaman Login Admin
Buka di browser:
```bash
http://localhost:8000/admin
```
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
