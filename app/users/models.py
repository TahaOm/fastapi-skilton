# Shared properties
import uuid
from sqlmodel import Field

from app.users.schemas import UserBase


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    # items: list["Item"] = Relationship(back_populates="owner", cascade_delete=True)
