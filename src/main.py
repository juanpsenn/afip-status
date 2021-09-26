from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.v1.routes import status

app = FastAPI()
app.include_router(status.router)


@app.get("/")
async def root():
    response = RedirectResponse(url='/docs')
    return response
