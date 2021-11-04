from fastapi import FastAPI,HTTPException
from src import interface

app=FastAPI()


@app.get("/note/",status_code=200)
def GetNotesCollection():

    response=interface.GetNotes()
    if response == False:
        raise HTTPException(status_code=404, detail="Cannot get items")
    return {"items":response}
        


@app.get("/note/{id}",status_code=200)
def GetNote(id:str):
  
    item=interface.GetNote(id)
    if item == False:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item":item}


@app.post("/note/{content}",status_code=201)
def NewNote(content:str):

    result=interface.SaveNote(content)
    if result ==False:
        raise HTTPException(status_code=418, detail="Note wasn't saved")
    return{"id":result}


@app.delete("/note/{id}",status_code=204)
def DeleteNote(id:str):
    
    result=interface.DeleteNote(id)
    if result ==False:
        raise HTTPException(status_code=418, detail="Cannot delete item")

