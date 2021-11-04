from _typeshed import WriteableBuffer
import json
import os
from types import resolve_bases
class Driver:

    __instance=None

    def __init__(self,path:str) -> None:

        if Driver.__instance != None:
            raise Exception("Database driver already implemented")
        self.log_debug=None
        self.__path=path



    @staticmethod
    def GetInstance(path:str=None):

        if Driver.__instance == None:
            if path == None:
                raise Exception("Database driver not implemented . Instance of database driver requires path!")
            Driver(path)

        return Driver.__instance




    def GetNote(self,note_id)->dict:

        root=self.__ItemExists(note_id)
        if root == False or root == -1:
            return False

        result=root.get(note_id)
        return result
        


    def GetNotes(self)->dict:
        
        notes=self.__ReadFile()
        return notes
    


    def DeleteNote(self,note_id)->dict:
        
        return self.__Delete(note_id)




    def NewNote(self,note:object)->bool:
        
        root=self.__ReadFile()

        new_note=note.GetNote()
        id=new_note["id"]
        root.update({id:new_note})

        self.__WriteFile(root)
        result=self.__ItemExists(id)
        
        if result==False or result == -1:

            self.__Log(f"ERR Wasnt possible to update database , cannot complete operation","error")
            return False 

        else :

            self.__Log(f"New note added {id}","info")
            return True




    def ClearDatbase(self)->bool:
        pass




    def __Delete(self,item_id:str)->bool:

        result=self.__ItemExists(item_id)

        if result== False:
            self.__Log(f"No such item in database","warning")
            return True

        elif result == -1:

            self.__Log(f"ERR Cannot complete operation","error")
            return False

        else:

            result.pop(item_id)
            self.__WriteFile(result)

            if self.__ItemExists(item_id)==False:

                self.__Log(f"Item deleted : --{item_id}--","info")
                return True

            else:

                self.__Log(f"Err Cannot delete : --{item_id}-- / cannot confirm if item was deleted / cannot access database","error")
                return False




    def CheckConnections(self)->bool:

        try:
            if self.__FileExists()== True:

                file=open(self.__path,"r")
                file.read()
                file.close()
                self.__Log(f"Connection to database!","info")

                return True
            else:
                return False

        except FileExistsError as err:

            self.__Log(f"ERR File doenst exists or cannot be found : {err}","error")
            return False

        except FileNotFoundError as err:

            self.__Log(f"ERR File cannot be found : {err}","error")
            return False

        except Exception as err:

            self.__Log(f"ERR Unknown err : {err}","error")
            return False




    def __ItemExists(self,item_id:str)->bool:
        
        root=self.__ReadFile()

        if root == False:#error 
            self.__Log(f"ERR Not possible to check if item exists, cannot access database ","error")
            return -1

        control_value=0
        result=root.get(item_id,control_value)
        
        if result==control_value:
            self.__Log(f"Item not found","info")
            return False
        
        else:
            self.__Log(f"Item found","info")
            return root



    def __WriteFile(self,data:dict)->bool:
        
        try:
            file=open(self.__path,"w")
            new_data=json.dumps(data)
            file.write(new_data)
            file.close()
            return True
        
        except FileNotFoundError as err:

            self.__Log(f"ERR File not found, cannot write database : {err}","error")
            return False

        except Exception as err:

            self.__Log(f"ERR Unknown err cannot write database : {err}","error")
            return False



    def __ReadFile(self)->dict:
        
        try:

            file=open(self.__path,"r")
            content=file.read()
            content=json.loads(content)
            file.close()

            
            if type(content) is dict:

                root=content.get("ROOT")

                if type(root) is dict:

                    if len(root) == 0:

                        self.__Log(f"Database is currently empty ","info")
                        return True

                    return root
            else:

                self.__Log(f"ERR Database found but (dict) data is missing , check data.json ","error")
                return False

        except Exception as err:
            
            self.__Log(f"ERR cannot extract content from database : {err}","error")
            return False

        return False




    def __FileExists(self)->bool:
        
        if os.path.isfile(self.__path):
            return True

        self.__Log(f"ERR Database file cannot be found in app","error")
        return False



    def __Log(self,message:str,type:str="info"):

        if self.log_debug != None:
            self.log_debug.LogMessage(type,message)
            pass
        else:
            print(message)