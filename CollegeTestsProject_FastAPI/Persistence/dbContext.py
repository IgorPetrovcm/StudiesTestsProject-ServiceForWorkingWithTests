from pymongo import MongoClient

class DbContext:
    def __init__(self, connectionString):
        try: 
            self.__mongoClient = MongoClient(connectionString) 
        except Exception as ex:
            raise(ex)
        
    @property
    def mongoClient(self):
        return self.__mongoClient
    
    