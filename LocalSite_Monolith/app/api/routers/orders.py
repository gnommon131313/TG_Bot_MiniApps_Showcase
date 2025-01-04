from fastapi import APIRouter, HTTPException
from app.api import schemes
from app.api import main
from app.database.engine import SessionLocal
from app.database import models
from pydantic import ValidationError
import random
from datetime import datetime
from starlette.requests import Request


router = APIRouter()
    
@router.get("/orders", tags=['orders'])
async def read_html(request: Request):
    return main.templates.TemplateResponse("orders.html", {"request": request,})
    
@router.get("/api/orders", tags=['orders'])
async def read_orders():
    with SessionLocal() as session: 
        orders = session.query(models.Order).all()
        
    return {"orders": orders, "msg": "response is success"}
    
@router.get("/api/order", tags=['orders'])
async def read_order(user_id: int):
    with SessionLocal() as session: 
        orders = session.query(models.Order).filter_by(user_id=user_id).all()
    
    return {"orders": orders, "msg": "response is success"}

@router.post("/api/orders/create", tags=['orders'])
async def create_order(order: schemes.CreateOrder):
    with SessionLocal() as session: 
        new_order = models.Order(
            **vars(order),
            date=str(datetime.now().date()),
            total=random.randint(1, 999999))
        
        session.add(new_order)
        session.commit()
    
    return {"msg": "response is success"}