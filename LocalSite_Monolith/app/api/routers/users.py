from fastapi import APIRouter, HTTPException
from app.api import schemes
from app.database.engine import SessionLocal
from app.database import models
from pydantic import ValidationError


router = APIRouter()

@router.get("/users/{user_id}", tags=['users'])
async def read_user(user_id: int):
    with SessionLocal() as session: 
        user = session.query(models.User).filter_by(id=user_id).first()
    
    if user is None:
        raise HTTPException(status_code=404, detail="Element not found in database")
    
    return {"user orm": user, "msg": "response is success"}

# @router.post("/create_user", tags=['users'])
# async def create_user(my_data):
#     return {"message": "User data received", "my_data": my_data}