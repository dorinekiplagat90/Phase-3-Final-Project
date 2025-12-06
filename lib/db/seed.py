from lib.db.database import engine, Base, Session
from lib.models.student import Student
from lib.models.course import Course
from lib.models.enrollment import Enrollment

def seed():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = Session()

    # Students
    s1 = Student(name="Alice", email="alice@example.com")
    s2 = Student(name="Bob", email="bob@example.com")

    # Courses
    c1 = Course(code="CS101", title="Intro to CS", credits=3)
    c2 = Course(code="MAT202", title="Linear Algebra", credits=4)

    session.add_all([s1, s2, c1, c2])
    session.commit()

    # Enrollments
    e1 = Enrollment(student_id=s1.id, course_id=c1.id)
    e2 = Enrollment(student_id=s1.id, course_id=c2.id)

    session.add_all([e1, e2])
    session.commit()

    session.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed()
