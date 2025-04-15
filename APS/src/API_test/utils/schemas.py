from pydantic import BaseModel 
from typing import Optional, List 
 
class User(BaseModel): 
    id: int 
    email: str 
    first_name: str 
    last_name: str 
    avatar: str 
 
class UserCreate(BaseModel): 
    name: str 
    job: str 
    id: Optional[str] = None 
    createdAt: Optional[str] = None 
 
class UserListResponse(BaseModel): 
    page: int 
    per_page: int 
    total: int 
    total_pages: int 
    data: List[User] 
    support: dict 
 
class UserResponse(BaseModel): 
    data: User 
    support: dict 
