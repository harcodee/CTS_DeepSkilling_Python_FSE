from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    Numeric
)

from sqlalchemy.orm import (
    declarative_base,
    relationship
)

# ==========================================================
# Database Connection
# ==========================================================

engine = create_engine(
    "mysql+mysqlconnector://root:YOUR_PASSWORD@localhost/college_db_orm",
    echo=True
)

Base = declarative_base()

# ==========================================================
# Department Model
# ==========================================================

class Department(Base):

    __tablename__ = "departments"

    dept_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100), nullable=False)

    students = relationship(
        "Student",
        back_populates="department",
        cascade="all, delete-orphan"
    )

    professors = relationship(
        "Professor",
        back_populates="department",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Department({self.dept_name})>"


# ==========================================================
# Student Model
# ==========================================================

class Student(Base):

    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)

    first_name = Column(String(50), nullable=False)

    last_name = Column(String(50), nullable=False)

    email = Column(String(100), unique=True)

    phone = Column(String(20))

    dept_id = Column(
        Integer,
        ForeignKey("departments.dept_id")
    )

    department = relationship(
        "Department",
        back_populates="students"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Student({self.first_name} {self.last_name})>"


# ==========================================================
# Professor Model
# ==========================================================

class Professor(Base):

    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True)

    professor_name = Column(String(100), nullable=False)

    designation = Column(String(50))

    salary = Column(Numeric(10,2))

    dept_id = Column(
        Integer,
        ForeignKey("departments.dept_id")
    )

    department = relationship(
        "Department",
        back_populates="professors"
    )

    def __repr__(self):
        return f"<Professor({self.professor_name})>"


# ==========================================================
# Course Model
# ==========================================================

class Course(Base):

    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True)

    course_name = Column(String(100), nullable=False)

    credits = Column(Integer)

    professor_id = Column(
        Integer,
        ForeignKey("professors.professor_id")
    )

    professor = relationship("Professor")

    enrollments = relationship(
        "Enrollment",
        back_populates="course",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Course({self.course_name})>"


# ==========================================================
# Enrollment Model
# ==========================================================

class Enrollment(Base):

    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("students.student_id")
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.course_id")
    )

    enrollment_year = Column(Integer)

    grade = Column(String(2))

    student = relationship(
        "Student",
        back_populates="enrollments"
    )

    course = relationship(
        "Course",
        back_populates="enrollments"
    )

    def __repr__(self):
        return (
            f"<Enrollment(Student={self.student_id}, "
            f"Course={self.course_id})>"
        )


# ==========================================================
# Create Tables
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Creating Tables...")
    print("=" * 60)

    Base.metadata.create_all(engine)

    print("\nTables created successfully!")

    print("\nTables Created:")
    print("1. departments")
    print("2. students")
    print("3. professors")
    print("4. courses")
    print("5. enrollments")