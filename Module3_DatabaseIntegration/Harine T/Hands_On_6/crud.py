from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from models import (
    engine,
    Department,
    Student,
    Professor,
    Course,
    Enrollment
)

# ==========================================
# Create Session
# ==========================================

Session = sessionmaker(bind=engine)
session = Session()

# ==========================================
# Task 81
# Insert Department
# ==========================================

cs = Department(
    dept_id=1,
    dept_name="Computer Science"
)

session.add(cs)

# ==========================================
# Insert Professor
# ==========================================

prof = Professor(
    professor_id=1,
    professor_name="Dr. Rajesh",
    designation="Associate Professor",
    salary=85000,
    department=cs
)

session.add(prof)

# ==========================================
# Insert Courses
# ==========================================

course1 = Course(
    course_id=101,
    course_name="Python Programming",
    credits=4,
    professor=prof
)

course2 = Course(
    course_id=102,
    course_name="Database Management",
    credits=3,
    professor=prof
)

session.add_all([course1, course2])

# ==========================================
# Insert Students
# ==========================================

student1 = Student(
    student_id=1,
    first_name="Harine",
    last_name="T",
    email="harine@gmail.com",
    phone="9876543210",
    department=cs
)

student2 = Student(
    student_id=2,
    first_name="Ananya",
    last_name="K",
    email="ananya@gmail.com",
    phone="9876500000",
    department=cs
)

student3 = Student(
    student_id=3,
    first_name="Rahul",
    last_name="S",
    email="rahul@gmail.com",
    phone="9876511111",
    department=cs
)

student4 = Student(
    student_id=4,
    first_name="Priya",
    last_name="M",
    email="priya@gmail.com",
    phone="9876522222",
    department=cs
)

student5 = Student(
    student_id=5,
    first_name="Arun",
    last_name="R",
    email="arun@gmail.com",
    phone="9876533333",
    department=cs
)

session.add_all([
    student1,
    student2,
    student3,
    student4,
    student5
])

# ==========================================
# Task 82
# Insert Enrollments
# ==========================================

enrollments = [

    Enrollment(
        student=student1,
        course=course1,
        enrollment_year=2025,
        grade="A"
    ),

    Enrollment(
        student=student2,
        course=course2,
        enrollment_year=2025,
        grade="A"
    ),

    Enrollment(
        student=student3,
        course=course1,
        enrollment_year=2025,
        grade="B"
    ),

    Enrollment(
        student=student4,
        course=course2,
        enrollment_year=2025,
        grade="A"
    )

]

session.add_all(enrollments)

session.commit()

print("\nRecords Inserted Successfully\n")

# ==========================================
# Task 83
# Count Students
# ==========================================

print("Total Students")

print(session.query(Student).count())

print("\nStudents in Computer Science")

students = (
    session.query(Student)
    .join(Department)
    .filter(Department.dept_name == "Computer Science")
)

for s in students:
    print(s.first_name, s.last_name)

# ==========================================
# Task 84
# Join Query
# ==========================================

print("\nStudent Enrollments")

rows = (
    session.query(
        Student.first_name,
        Student.last_name,
        Course.course_name
    )
    .join(Enrollment)
    .join(Course)
)

for row in rows:
    print(row)

# ==========================================
# Task 85
# Update
# ==========================================

student = (
    session.query(Student)
    .filter(Student.student_id == 1)
    .first()
)

student.first_name = "Harine T"

session.commit()

print("\nStudent Updated")

# ==========================================
# Task 86
# Delete
# ==========================================

record = (
    session.query(Enrollment)
    .filter(Enrollment.student_id == 4)
    .first()
)

if record:
    session.delete(record)
    session.commit()
    print("\nEnrollment Deleted")

else:
    print("\nEnrollment Not Found")

# ==========================================
# Task 87
# Observe N+1 Problem
# ==========================================

print("\n" + "=" * 60)
print("TASK 87 - N+1 QUERY DEMONSTRATION")
print("=" * 60)

enrollments = session.query(Enrollment).all()

for enrollment in enrollments:
    print(
        enrollment.student.first_name,
        "-",
        enrollment.course.course_name
    )


# ==========================================
# Task 88
# Use joinedload()
# ==========================================

print("\n" + "=" * 60)
print("TASK 88 - USING joinedload()")
print("=" * 60)

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for enrollment in enrollments:
    print(
        enrollment.student.first_name,
        "-",
        enrollment.course.course_name
    )

# ==========================================
# Task 89
# Compare SQL Queries
# ==========================================

print("\n" + "=" * 60)
print("TASK 89")
print("=" * 60)

print("""
Without joinedload():
SQLAlchemy executes one query for Enrollment
plus additional queries for Student and Course.

With joinedload():
SQLAlchemy performs a single JOIN query,
eliminating the N+1 Query Problem.
""")

"""
==========================================================
Task 90
Difference between Lazy Loading and joinedload()

Lazy Loading:
- Fetches related objects only when accessed.
- Causes the N+1 Query Problem.
- Generates multiple SQL queries.

joinedload():
- Uses SQL JOIN.
- Fetches related objects in one query.
- Eliminates the N+1 Query Problem.
- Improves performance significantly.

Query Count Example

Without joinedload() :
1 query for enrollments
+ N queries for students
+ N queries for courses

With joinedload() :
Only ONE SQL query is executed.
==========================================================
"""

# ==========================================
# Close Session
# ==========================================

session.close()

print("\nCRUD Operations Completed Successfully")
