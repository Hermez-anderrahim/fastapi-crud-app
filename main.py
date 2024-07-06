
from fastapi import FastAPI , Path
from fastapi import HTTPException
from typing import Optional, Union
from decouple import config
from pydantic import BaseModel, conint
from supabase import create_client, Client
from fastapi.encoders import jsonable_encoder
from datetime import datetime 

url = config('SUPABASE_URL')
key = config('SUPABASE_KEY')

app = FastAPI()
supabase:Client = create_client(url, key)

class Task(BaseModel):
    id: int
    title: str
    desc : str
    

@app.get("/")
def read_root():
    
    todos , error = supabase.table("todos").select("*").execute()
    if error.count != 0 :
        raise HTTPException(status_code=400, detail=error)
    return todos

@app.get("/task/{id}")
def get_task(id : int = Path(..., gt=1)) : 
    todos , error = supabase.table("todos" ).select("*").eq("id" , id).execute()

    if error.count:
        raise HTTPException(status_code=400, detail=error)
    return todos

@app.post("/delete")
def delete_task(id:int):
    todos , error = supabase.table("todos").delete().eq("id", id).execute()
    if error.count != 0 :
        raise HTTPException(status_code=400, detail=error)
    if not todos:
        raise HTTPException(status_code=404, detail="Task not found")
    return todos

@app.post("/create/{taskId}") 
def create_task(taskId : int , task:Task):
    existing_task , error = supabase.table("todos").select("*").eq("id",taskId).execute()
    
    if existing_task[1] != []:
        raise HTTPException(status_code=400, detail="Task already exists")
    task_dict = task.dict()
    task_dict["id"] = taskId
    todos , error = supabase.table("todos").insert(task_dict).execute()
    if error.count != 0 :
        raise HTTPException(status_code=400, detail=error)
    return todos
    
@app.get("/get-byname")
def get_task_byname(* , name : Optional[str] = None):#name is optional and * so i can use any params optional + unoptional in any orede
    todos  , error = supabase.table("todos").select("*").ilike("title", name).execute()
    if error.count != 0 :
        raise HTTPException(status_code=400, detail=error)
    return todos

@app.put("/update/{id}")
def update_task(id:int , task:Task): 
    task_dict = task.dict()
   
    todos , error = supabase.table("todos").update(task_dict).eq("id", id).execute()
    if error.count != 0 :
        raise HTTPException(status_code=400, detail=error)
    
    if  todos[1] == []:
        raise HTTPException(status_code=404, detail="Task not found")
    return todos
