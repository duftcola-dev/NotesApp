import uuid
import datetime


class MetaModel:

    def __init__(self) -> None:
        pass

    def GetDate(self)->str:

        d=datetime.datetime.now()
        string_date=""

        year=str(d.year)
        month=str(d.month)
        day=str(d.day)
        hour=str(d.hour)
        minute=str(d.minute)
        second=str(d.second)
        string_date=f"{year}-{month}-{day} | {hour}:{minute}:{second}"
        return string_date

    def GetId(self)->str:

        return str(uuid.uuid1())


class NoteModel(MetaModel):

    def __init__(self,content) -> None:
        super().__init__()
        self.content=content

    def GetNote(self):

        id=self.GetId()
        date=self.GetDate()

        note={
            "id":id,
            "date":date,
            "content":self.content
        }

        return note
    

class Models:

    def __init__(self) -> None:
        pass
        
    def GetNoteModel(self,content:str):

            if type(content) is not str:
                
                raise Exception(f"Note Model only admits type string(str)  but type {type(content)} was provided")
        
            new_note=NoteModel(content)
            return new_note