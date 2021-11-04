from fastapi import FastApi


app=FastApi()


@app.get("/note/")
def GetNotesCollection():
    pass


@app.get("/note/{id}")
def GetNote(id:str):

    pass

@app.post("/note/{content}")
def NewNote(content:str):

    pass

@app.delete("/note/{id}")
def DeleteNote(id:str):
    pass
