from app.database import init as db_init
from app.api.main import app as api_app
import asyncio
import uvicorn


async def server_run():
    config = uvicorn.Config(api_app, host="127.0.0.1", port=8000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    db_init.init()  # Лучше дожидаться полной инициализации базы, а не пихать это в асинхронность 
    
    await asyncio.gather(
        server_run(),  # Запуск FastAPI
        #other_run()  # Запуск других чего-нибудь
    )

# Для запуска python main.py (или Run Python File F5)
# Тут будет запуск на localhost (для публичности в интернете использовать тоннели (note -> cloudflared) или полный деплой)
if __name__ == "__main__":
    asyncio.run(main())