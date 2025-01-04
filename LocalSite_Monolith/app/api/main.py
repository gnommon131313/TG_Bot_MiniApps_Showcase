from fastapi import FastAPI
from app.api.routers.orders import router as orders_router
from app.api.routers.products import router as products_router
from app.api.routers.users import router as users_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import FileResponse
import os


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")  # Раздаем статические файлы (например, ваш HTML, CSS, JS)
templates = Jinja2Templates(directory="templates")  # Jinja2 получает доступ к шаблонам html (этот способ ориентирован на фреймворки типа FastAPI или Starlette)

@app.get("/favicon.ico")
async def favicon():
    return FileResponse(os.path.join('static', 'favicon.ico'))

@app.get("/", tags=['root']) 
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "my_param1": "Привет из FastAPI!"})
    
# @app.post("/", tags=['root'])
# async def create_user(my_data):
#     print()
#     print(my_data)
#     print(type(my_data))
#     print()
#     return {"message": "User data received", "my_data": my_data}

def include_routers() -> None:
    app.include_router(orders_router)
    app.include_router(products_router)
    app.include_router(users_router)

include_routers()

# CORS
# Когда фронтенд и сервер с FastAPI находятся на разных доменах или портах, возникает необходимость настроить CORS (кросс-доменные запросы)
# Для этого FastAPI предоставляет специальный механизм для обработки CORS.
origins = [
    "http://localhost:3000",  # URL фронтенда (если используется, например, React)
    "http://localhost:4200",  # URL фронтенда (если используется Angular)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # или ['*'], чтобы разрешить все домены
    allow_credentials=True,
    allow_methods=["*"],  # разрешить все методы
    allow_headers=["*"],  # разрешить все заголовки
)