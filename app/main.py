from fastapi import FastAPI

import uvicorn

app = FastAPI(
    title="Article Store",
    description="Test task from xOne",
    version="0.0.1",
    contact={
        "name": "Ivan Levchuk",
        "email": "swankyyy1@gmail.com",
    },
)


@app.get("/")
async def index():
    return "hello Kitty"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
