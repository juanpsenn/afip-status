from fastapi import FastAPI

from v1.routes import status

app = FastAPI()
app.include_router(status.router)
