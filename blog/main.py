from fastapi import FastAPI
from .models import models
from .database import engine
from .routers import blog, user, authentication
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv


#any new model found create on db
models.Base.metadata.create_all(engine)

app = FastAPI()

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

load_dotenv()


app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)




