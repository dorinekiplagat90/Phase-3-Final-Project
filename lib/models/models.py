from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Session
from lib.db.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    enrollments = relationship(
        "Enrollment",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    # -------- CRUD METHODS --------

    @classmethod
    def create(cls, session: Session, name: str, email: str):
        student = cls(name=name, email=email)
        session.add(student)
        session.commit()
        session.refresh(student)
        return student

    @classmethod
    def get(cls, session: Session, student_id: int):
        return session.get(cls, student_id)

    @classmethod
    def get_all(cls, session: Session):
        return session.query(cls).all()

    def update(self, session: Session, **fields):
        for key, value in fields.items():
            setattr(self, key, value)
        session.commit()
        session.refresh(self)
        return self

    def delete(self, session: Session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)

    enrollments = relationship(
        "Enrollment",
        back_populates="course",
        cascade="all, delete-orphan"
    )

    # -------- CRUD METHODS --------

    @classmethod
    def create(cls, session: Session, code: str, title: str, credits: int):
        course = cls(code=code, title=title, credits=credits)
        session.add(course)
        session.commit()
        session.refresh(course)
        return course

    @classmethod
    def get(cls, session: Session, course_id: int):
        return session.get(cls, course_id)

    @classmethod
    def get_all(cls, session: Session):
        return session.query(cls).all()

    def update(self, session: Session, **fields):
        for key, value in fields.items():
            setattr(self, key, value)
        session.commit()
        session.refresh(self)
        return self

    def delete(self, session: Session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return (
            f"<Course(id={self.id}, code={self.code}, "
            f"title={self.title}, credits={self.credits})>"
        )
