import sys
import os
from inspect import  currentframe, getframeinfo
import threading
import datetime


# Author : Robin
# Description : General purpose log class  mostly meant to be inherited and used within another class. 
# Tested : yes
# last update : 1/9/2021

class Logs():


    def __init__(self,path=None) -> None:
        self.__path=path


    def LogMessage(self,message_type,message):

        self.__type=["warning","error","info"]
    
        if message_type in self.__type:
            
            date=self.__GetDate()
            self.__message=""
            self.__message=self.__message+date+" | "+message_type+" | "+message+"\n"
            sys.stdout.write(self.__message)

            if self.__path != None:
                
                self.__SaveLog(message)




    def __GetDate(self):
        
        x=datetime.datetime.now()
        Year=str(x.year)
        Month=str(x.month)
        Day=str(x.day)
        Hour=str(x.hour)
        Minute=str(x.minute)
        Second=str(x.second)
        
        return Day+"|"+Month+"|"+Year+" - "+Hour+":"+Minute+":"+Second



    def __SaveLog(self,message):

        file=open(self.__path,"a")
        file.write(message)
        file.close()