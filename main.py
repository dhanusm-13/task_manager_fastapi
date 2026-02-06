from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base,DBTask,get_db


Base.metadata.create_all(bind=engine)

app=FastAPI()

class Task(BaseModel):
    id:int
    title:str
    description:Optional[str]=None
    completed:bool=True
    
@app.get('/')
def greet_user():
    return {"hello":"user"}



@app.post("/tasks")
def create_tasks(task:Task,db:Session=Depends(get_db)):
    new_task=DBTask(
        id=task.id,
        title=task.title,
        description=task.description,
        completed=task.completed
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"Message":"Task added successfully"}


@app.get('/tasks')
def get_tasks(title:Optional[str]=None,completed:Optional[str]=None,db:Session=Depends(get_db)):
    query=db.query(DBTask)
    
    
    #filter by title
    if title:
        query=query.filter(DBTask.title.contains(title))
    
    #filter by completion status
    if completed is not None:
        query=query.filter(DBTask.completed==completed)
        
    return query.all()
        

@app.get('/tasks/{task_id}')
def get_single_data(task_id:int,db:Session=Depends(get_db)):
    task=db.query(DBTask).filter(DBTask.id==task_id).first()
    
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return task



    
@app.put('/tasks/{task_id}')
def update_task(task_id:int,updated_task:Task,db:Session=Depends(get_db)):
    db_task=db.query(DBTask).filter(DBTask.id==task_id).first()
    
    if not db_task:
        raise HTTPException(status_code=404,detail="task not found")
    db_task.title=updated_task.title
    db_task.description=updated_task.description
    db_task.completed=updated_task.completed
    
    db.commit()
    db.refresh(db_task)
    return {"message":"Task updated successfully"}
    

@app.delete("/tasks/{task_id}")
def delete_data(task_id:int,db:Session=Depends(get_db)):
    db_task=db.query(DBTask).filter(DBTask.id==task_id).first()
    
    if not db_task:
        raise HTTPException(status_code=404,detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"message":"Task deleted from database"}


#pagination
@app.get('/tasks')
def get_tasks(
    skip:int=0,
    limit:int=10,
    db:Session=Depends(get_db)
):
    return db.query(DBTask).offset(skip).limit(limit).all()