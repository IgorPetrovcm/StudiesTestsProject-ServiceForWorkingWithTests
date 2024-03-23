from pymongo import MongoClient
import sys

sys.path.append("../Exceptions")

from Exceptions.dbConnectionException import DbConnectionException

class ApplicationContext:
    def __init__(self, connectionString):
        self.__connectionString = connectionString
        self.__context = MongoClient(connectionString)
        
    @property
    def context(self):
        return self.__context
            