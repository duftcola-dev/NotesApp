import os

from .dependencies.TreeGeneratorLiteModule.DirectoryTreeGenerator_lite import TreeExplorer
from .dependencies.Database_Driver.Driver import Driver
from .dependencies.LogMessageModule.Logs import Logs
from .dependencies.LogMessageModule.Logs import GetLogInstance


local_path=os.getcwd()
explorer=TreeExplorer()# files mapping class
explorer.ExploreDirectories(local_path)#map files

app_files=explorer.GetFilesDict()# map of files path
log_file_path=app_files.get("logs.txt")
data_file_path=app_files.get("data.json")

logs=Logs(log_file=log_file_path) #App logs limited to 1 instance
internal_logs=GetLogInstance(log_file=log_file_path)#Internal classes log limited to n instances
driver=Driver(data_file_path)# database driver
driver.log_debug=internal_logs


def SaveNote():
    pass

def GetNote():
    pass

def GetNotes():
    pass

def DeleteNote():
    pass

def ClearDataBase():
    pass