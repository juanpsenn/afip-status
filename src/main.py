from fastapi import FastAPI
from starlette.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise

from src.v1.databases.settings import DATABASE_URL
from src.v1.routes import status

app = FastAPI()
app.include_router(status.router)


@app.get("/", include_in_schema=False)
def root():
    response = RedirectResponse(url="/docs")
    return response


# Register Tortoise ORM with DB
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["src.v1.databases.models"]},
    generate_schemas=False,
    add_exception_handlers=True,
)
