import os

from .dependencies.TreeGeneratorLiteModule.DirectoryTreeGenerator_lite import TreeExplorer
from .dependencies.Database_Driver.Driver import Driver
from .dependencies.LogMessageModule.Logs import Logs
from .dependencies.LogMessageModule.Logs import GetLogInstance
from .dependencies.models.models import Models

local_path=os.getcwd()
explorer=TreeExplorer()# files mapping class
explorer.ExploreDirectories(local_path)#map files

app_files=explorer.GetFilesDict()# map of files path
log_file_path=app_files.get("logs.txt")
data_file_path=app_files.get("data.json")

logs=Logs(log_file=log_file_path) #App logs limited to 1 instance
internal_logs=GetLogInstance(log_file_path)#Internal classes log limited to n instances
driver=Driver(data_file_path)# database driver
driver.log_debug=internal_logs
app_models=Models()# database objects models



def CheckConnection()->bool:
    logs.LogMessage("info","Checking connection to database")
    return driver.CheckConnections()


def SaveNote(content:str):
    
    logs.LogMessage("info","Adding new item")
    note=app_models.GetNoteModel(content)
    id=note.GetId()
    result=driver.NewNote(note)
    if result == True:
        logs.LogMessage("Database Updated","info")
    else:
        return False
        
    return id


def GetNote(note_id:str):
    
    logs.LogMessage("info","Extracting item")
    return driver.GetNote(note_id)


def GetNotes():
    
    logs.LogMessage("info","Extracting collection")
    return driver.GetNotes()


def DeleteNote(note_id:str):

    logs.LogMessage("info","Deleting item")
    return driver.DeleteNote(note_id)


def ClearDataBase():
    
    logs.LogMessage("warning","Purging database")
    return driver.ClearDatbase()