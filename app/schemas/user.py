from typing import Optional

from pydantic import BaseModel, EmailStr, model_validator

from app.models.user import UserRole


class UserBase(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    role: UserRole
    student_id: Optional[str] = None
    course_year: Optional[str] = None
    is_male: Optional[bool] = None
    school_id_image: Optional[str] = None
    contact: Optional[str] = None

    class Config:
        use_enum_values = True


class UserCreate(UserBase):
    @model_validator(mode="after")
    def ensure_student_id(cls, values):
        if values.role == UserRole.STUDENT and not values.student_id:
            raise ValueError("student_id is required when role is student")
        return values


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    role: Optional[UserRole] = None
    student_id: Optional[str] = None
    course_year: Optional[str] = None
    is_male: Optional[bool] = None
    school_id_image: Optional[str] = None
    contact: Optional[str] = None

    class Config:
        use_enum_values = True


class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True
