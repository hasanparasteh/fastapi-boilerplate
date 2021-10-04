from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas.post as _schemas
import services.post as _services

import services.services as _base_services


router = _fastapi.APIRouter()


@router.get("/posts/", response_model=List[_schemas.Post])
def read_posts(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_base_services.get_db),
):
    posts = _services.get_posts(db=db, skip=skip, limit=limit)
    return posts


@router.get("/posts/{post_id}", response_model=_schemas.Post)
def read_post(post_id: int, db: _orm.Session = _fastapi.Depends(_base_services.get_db)):
    post = _services.get_post(db=db, post_id=post_id)
    if post is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this post does not exist"
        )

    return post


@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db: _orm.Session = _fastapi.Depends(_base_services.get_db)):
    _services.delete_post(db=db, post_id=post_id)
    return {"message": f"successfully deleted post with id: {post_id}"}


@router.put("/posts/{post_id}", response_model=_schemas.Post)
def update_post(
    post_id: int,
    post: _schemas.PostCreate,
    db: _orm.Session = _fastapi.Depends(_base_services.get_db),
):
    return _services.update_post(db=db, post=post, post_id=post_id)