from  pydantic import BaseModel, Field

class User(BaseModel):
    id: str
    email: str
    role:str
    password:str
    
    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "email": "JHb2X@example.com",
                "role": "admin",
                "password": "password"
            }
        }