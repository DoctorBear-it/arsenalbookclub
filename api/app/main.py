# from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["http://127.0.0.1:8000/", "http://localhost:8000/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def hello_world():
    return {"message": "Hello, world!"}


# TODO: Check out SQLAlchemy 2 ORM
# TODO: Check out Pydantic models
# TODO: Check out SQLModel to replace the two above
# TODO: Check out HTTPS certificates https://medium.com/@mariovanrooij/adding-https-to-fastapi-ad5e0f9e084e

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
