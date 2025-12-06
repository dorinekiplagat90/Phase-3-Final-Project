from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    enrollments = relationship("Enrollment", back_populates="student")

    def __repr__(self):
        return f"<Student {self.id}: {self.name}>"
