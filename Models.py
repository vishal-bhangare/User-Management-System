from pydantic import BaseModel
from datetime import datetime
# Model for User Registration


class UserRegistration(BaseModel):
    username: str
    email: str
    full_name: str
    password: str

# Model for User Profile


class UserProfile(BaseModel):
    username: str
    email: str
    full_name: str
    created_at: datetime


class UserLogin(BaseModel):
    email: str
    password: str


class UpdatePassword(BaseModel):
    new_password: str
