from enum import Enum as PyEnum

from sqlalchemy import Boolean, Column, Enum, Integer, String

from app.core.database import Base


class UserRole(PyEnum):
    STUDENT = "student"
    FACULTY = "faculty"
    NON_FACULTY = "non-faculty"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    student_id = Column(String(50), unique=True, nullable=True)
    age = Column(Integer, nullable=True)
    role = Column(
        Enum(
            UserRole,
            values_callable=lambda enum_cls: [member.value for member in enum_cls],
            native_enum=False,
        ),
        nullable=False,
    )
    course_year = Column(String(100), nullable=True)
    is_male = Column(Boolean, nullable=True)
    school_id_image = Column(String(255), nullable=True)
    contact = Column(String(50), nullable=True)
