from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define post schema
class Post(BaseModel):
    title: str
    content: str
    published: bool = False
# Method("Path")
@app.get("/") 
# Function
def root():
    return {"message": "return 200"}

@app.get("/posts")
def get_posts():
    return {"data": "data posts"}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    return {"data": new_post.title,
            "published": new_post.published}
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"data": payload['title']}