from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    title = Column(String)
    credits = Column(Integer)

    enrollments = relationship("Enrollment", back_populates="course")

    def __repr__(self):
        return f"<Course {self.code}: {self.title}>"
