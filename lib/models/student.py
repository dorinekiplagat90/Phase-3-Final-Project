from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Session
from lib.db.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    enrollments = relationship(
        "Enrollment",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    # CREATE
    @classmethod
    def create(cls, session: Session, name: str, email: str):
        student = cls(name=name, email=email)
        session.add(student)
        session.commit()
        session.refresh(student)
        return student

    # READ
    @classmethod
    def get(cls, session: Session, student_id: int):
        return session.get(cls, student_id)

    # UPDATE
    def update(self, session: Session, **fields):
        for key, value in fields.items():
            setattr(self, key, value)
        session.commit()
        session.refresh(self)
        return self

    # DELETE
    def delete(self, session: Session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"<Student {self.id}: {self.name}>"
