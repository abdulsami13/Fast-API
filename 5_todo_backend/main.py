from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todo", response_model=schemas.CreateTodo)
def create_todo(todo:schemas.CreateTodo,db:Session=Depends(get_db)):
    db_todo = crud.create_todo(db,todo=todo)
    return db_todo

@app.get("/todoget", response_model=list[schemas.CreateTodo])
def read_Todo(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    Todo = crud.get_todo(db, skip=skip, limit=limit)
    return Todo



# Update a TODO item
@app.put("/todos/{todo_id}", response_model=schemas.CreateTodo)
def update_todo(todo_id: int, todo_update: schemas.CreateTodo, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db, todo_id=todo_id, todo_update=todo_update)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="TODO item not found")
    return db_todo

# Delete a TODO item
@app.delete("/todos/{todo_id}", response_model=schemas.CreateTodo)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.delete_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="TODO item not found")
    return db_todo


