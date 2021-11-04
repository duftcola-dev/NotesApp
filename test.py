from os import truncate
import unittest
from unittest import result
from app.src.interface import CheckConnection
from app.src.interface import GetNotes
from app.src.interface import GetNote
from app.src.interface import SaveNote
from app.src.interface import DeleteNote
from app.src.interface import ClearDataBase
from app.src.dependencies.models.models import Models
class Test(unittest.TestCase):

    #test variable

    test_id=None


    def test_db_connection(self):
        
        result=CheckConnection()
        self.assertEqual(result,True,"Cannot acces data.json")

    def test_model(self):

        model=Models()
        result=model.GetNoteModel("Some test message")
        self.assertEqual(type(result.GetDate()),str,"Model must return date as string")
        self.assertEqual(type(result.GetId()),str,"Model must return id as string")
        self.assertEqual(type(result.GetNote()),dict,"Model must note as dict object")

    def test_read_database(self):

        #while database is still empty
        result=GetNotes()#spected true when db empty
        self.assertNotEqual(result,False,"Database is currently empty, spect True")

        #while database is still empty
        model=Models()
        result=model.GetNoteModel("Some test message")
        id=result.GetId()
        result=GetNote(id)
        self.assertEqual(result,False,"While databse is empty get note must return false")
        

    def test_add_note(self):

        result=SaveNote("Some test message")
        self.assertNotEqual(result,False," updating database Failed")
   

    def test_get_item_delte_item(self):
        if self.test_id != None:
            result=GetNote(self.test_id)
            self.assertEqual(type(result),dict,"Cannot get item from databse")

        if self.test_id != None:
            result=DeleteNote(self.test_id)
            self.assertEqual(result,True,"Delete item failed . Cannot delete item")

    def test_get_items(self):

        result=GetNotes()
        self.assertEqual(type(result),dict," GetNotes must return a list containing all the notes")
        #is iterable ? 
        try:
            count=0
            for item in result:
                count=count+1
                if count == 2:
                    break
            result=True
        except Exception:
            result=False
        self.assertEqual(result,True," GetNotes must return a collection but the result is not and iterable")


    def test_empty_database(self):

        result=ClearDataBase()
        self.assertEqual(result,True," Database cannot be emptyed")



    

if __name__ == "__main__":

    unittest.main()