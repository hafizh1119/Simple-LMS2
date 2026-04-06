from courses.models import Course, Enrollment
from django.db import connection

def reset_queries():
    connection.queries_log.clear()

def show_queries(label):
    print(f"\n===== {label} =====")
    print(f"Total Queries: {len(connection.queries)}")

def n_plus_one():
    courses = Course.objects.all()

    for course in courses:
        print(course.title, "-", course.instructor.username)

def optimized():
    courses = Course.objects.select_related('instructor')

    for course in courses:
        print(course.title, "-", course.instructor.username)

def demo_custom_managers():

    reset_queries()
    courses = Course.objects.for_listing()

    for c in courses:
        print(c.title, "-", c.instructor.username)

    show_queries("Course.objects.for_listing()")

    reset_queries()
    enrollments = Enrollment.objects.for_student_dashboard()

    for e in enrollments:
        print(e.student.username, "-", e.course.title)

    show_queries("Enrollment.objects.for_student_dashboard()")

def run():
    # N+1
    reset_queries()
    n_plus_one()
    show_queries("N+1 Problem")

    # Optimized
    reset_queries()
    optimized()
    show_queries("Optimized Query")

    # Custom Manager
    demo_custom_managers()