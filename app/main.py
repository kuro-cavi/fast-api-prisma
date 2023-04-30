from fastapi import FastAPI
from app.prisma import prisma
from app.routes import articles

app = FastAPI()

app.include_router(articles.router)


@app.on_event("startup")
async def startup():
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()


@app.get('/')
async def hello():
    return 'hello fastapi!'
