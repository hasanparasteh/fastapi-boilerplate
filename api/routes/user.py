from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas.user as _schemas
import services.user as _services

import services.services as _base_services

router = _fastapi.APIRouter()

@router.post("/users/", response_model=_schemas.User)
def create_user(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_base_services.get_db)
):
    db_user = _services.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise _fastapi.HTTPException(
            status_code=400, detail="woops the email is in use"
        )
    return _services.create_user(db=db, user=user)


@router.get("/users/", response_model=List[_schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_base_services.get_db),
):
    users = _services.get_users(db=db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=_schemas.User)
def read_user(user_id: int, db: _orm.Session = _fastapi.Depends(_base_services.get_db)):
    db_user = _services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return db_user


# @router.post("/users/{user_id}/posts/", response_model=_schemas.Post)
# def create_post(
#     user_id: int,
#     post: _schemas.PostCreate,
#     db: _orm.Session = _fastapi.Depends(_base_services.get_db),
# ):
#     db_user = _services.get_user(db=db, user_id=user_id)
#     if db_user is None:
#         raise _fastapi.HTTPException(
#             status_code=404, detail="sorry this user does not exist"
#         )
#     return _services.create_post(db=db, post=post, user_id=user_id)