from sqlalchemy.orm import Session # type: ignore

from . import models, schemas


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item



def create_todo(db:Session,todo:schemas.CreateTodo):
    db_todo=models.Item(todo=todo.todo)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo      

def get_todo(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()



def update_todo(db: Session, todo_id: int, todo_update: schemas.CreateTodo):
    db_todo = db.query(models.Item).filter(models.Item.id == todo_id).first()
    if not db_todo:
        return None
    db_todo.todo = todo_update.todo
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Item).filter(models.Item.id == todo_id).first()
    if not db_todo:
        return None
    db.delete(db_todo)
    db.commit()
    return db_todo