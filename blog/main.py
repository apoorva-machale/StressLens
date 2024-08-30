from fastapi import FastAPI
from .models import models
from .database import engine
from .routers import blog, user, authentication
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Response
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from fastapi_redis_cache import FastApiRedisCache
from sqlalchemy.orm import Session
import os
from redis import asyncio as aioredis

#any new model found create on db
models.Base.metadata.create_all(engine)
load_dotenv()

REDIS_URL = os.environ.get("REDIS_URL")

redis_cache = FastApiRedisCache()
async def init_redis_cache():
    redis = await aioredis.from_url(REDIS_URL)
    redis_cache.init(
        RedisBackend(redis),
        prefix="myapi-cache",
        response_header="X-MyAPI-Cache",
        ignore_arg_types=[Request, Response, Session]
    )
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    r_cache = await init_redis_cache()
    yield
    pass


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)




