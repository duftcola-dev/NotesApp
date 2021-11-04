import unittest
from unittest import result
from app.src.interface import CheckConnection
from app.src.interface import GetNotes
from app.src.interface import GetNote
from app.src.dependencies.models.models import Models
class Test(unittest.TestCase):


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
        self.assertEqual(result,True,"Database is currently empty, spect True")

        #while database is still empty
        model=Models()
        result=model.GetNoteModel("Some test message")
        id=result.GetId()
        result=GetNote(id)
        self.assertEqual(result,False,"While databse is empty get note must return false")
        

    def test_add_note(self):

        


if __name__ == "__main__":

    unittest.main()