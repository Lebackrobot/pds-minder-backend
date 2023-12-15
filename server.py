import uvicorn
from fastapi import FastAPI
from src.database.db_connect import engine, Base

from src.api.api import api_router
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run('server:app', host='localhost', port=8000, reload=True)
