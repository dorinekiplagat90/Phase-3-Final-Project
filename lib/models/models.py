
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    enrollments = relationship("Enrollment", back_populates="student", cascade="all, delete")

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    title = Column(String)
    credits = Column(Integer)

    enrollments = relationship("Enrollment", back_populates="course", cascade="all, delete")

    def __repr__(self):
        return f"<Course(id={self.id}, code={self.code}, title={self.title}, credits={self.credits})>"