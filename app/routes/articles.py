from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from app.prisma import prisma
from prisma.models import Articles

router = APIRouter()


class CreateRequest(BaseModel):
    title: str
    content: str


class UpdateRequest(BaseModel):
    id: int
    title: str
    content: str


@router.get('/articles')
async def find_all():
    return await prisma.articles.find_many()


@router.get('/articles/{id}')
async def find(id: int):
    return await prisma.articles.find_unique(where={"id": id})


@router.post('/articles')
async def create(article: CreateRequest):
    article = await prisma.articles.create(
        data={
            'title': article.title,
            'content': article.content,
        },
    )

    return article


@router.put('/articles')
async def create(article: UpdateRequest):
    article = await prisma.articles.update(
        where={
            'id': article.id,
        },
        data={
            'title': article.title,
            'content': article.content,
        },
    )

    return article


@router.delete('/articles/{id}')
async def delete(id: int):
    article = await prisma.articles.delete(
        where={
            'id': id,
        }
    )

    return article

