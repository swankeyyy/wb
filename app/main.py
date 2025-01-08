from typing import Optional
from fastapi import FastAPI, Header
from api import router
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
async def index(tst: Optional[str] = Header(None)):
    if tst:
        return tst
    return "hello Kitty"


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
