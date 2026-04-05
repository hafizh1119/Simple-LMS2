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
