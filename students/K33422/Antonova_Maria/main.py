from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.settings.connection import init_db
from src.routes.profile import profile_route
from src.routes.team import team_route
from src.routes.project import project_route
from src.routes.auth import auth_route
from alembic.config import Config
from alembic import command

@asynccontextmanager
async def lifespan(app: FastAPI):
    # init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(profile_route)
app.include_router(team_route)
app.include_router(project_route)
app.include_router(auth_route)

if __name__ == "__main__":
    # alembic_cfg = Config("C:/Users/Мария/Documents/6_web_lab1.4(2)/alembic.ini")
    # #command.init(alembic_cfg, "migrations")
    # command.revision(config=alembic_cfg, message="st",autogenerate=True)
    # print("aa")
    uvicorn.run(app, host="127.0.0.1", port=8000)
