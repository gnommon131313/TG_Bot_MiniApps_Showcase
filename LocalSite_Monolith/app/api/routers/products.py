from fastapi import APIRouter, HTTPException
from app.api import schemes
from app.api import main
from app.database.engine import SessionLocal
from app.database import models
from pydantic import ValidationError
from starlette.requests import Request


router = APIRouter()
    
@router.get("/catalog", tags=['products'])
async def read_html(request: Request):
    return main.templates.TemplateResponse("catalog.html", {"request": request,})
    
@router.get("/api/catalog", tags=['products'])
async def read_products():
    with SessionLocal() as session: 
        products = session.query(models.Product).all()
        
    return {"products": products, "msg": "response is success"}

@router.get("/catalog/{product_id}", tags=['products'])
async def read_product(product_id: int):
    with SessionLocal() as session: 
        product = session.query(models.Product).filter_by(id=product_id).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Element not found in database")
    
    try:
        product_dict = vars(product)
        product_schema = schemes.Product(**product_dict)
        
        return {"product orm": product, "product schema": product_schema, "msg": "response is success"}
    
    except ValidationError as err:
        raise HTTPException(status_code=422, detail=f'{err}')