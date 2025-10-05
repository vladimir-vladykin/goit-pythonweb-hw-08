from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class ContactModel(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=100)
    phone: str = Field(max_length=20)
    date_of_birth: str = datetime
    info: str = Field(max_length=200)
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
