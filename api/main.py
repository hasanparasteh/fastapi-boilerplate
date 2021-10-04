import fastapi as _fastapi
import sqlalchemy.orm as _orm

import services.services as _services

import routes.post as _post_routes
import routes.user as _user_routes

app = _fastapi.FastAPI()
_services.create_database()

app.include_router(_post_routes.router)
app.include_router(_user_routes.router)

