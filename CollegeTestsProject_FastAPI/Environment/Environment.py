import os
import sys
import json

sys.path.append("../Exceptions")

from Exceptions.environmentException import EnvironmentException 

sys.path.insert(1, os.path.join)

class Environment:
    def __init__(self, pathToAppSettings = os.getcwd() + "/Environment"):
        if self.__checkPath(pathToAppSettings):
            self.__pathToAppSettings = pathToAppSettings


    @property
    def pathToAppSettings(self):
        return self.__pathToAppSettings
    
    @pathToAppSettings.setter
    def pathToAppsettings(self, pathToAppSettings):
        if self.__checkPath(pathToAppSettings):
            self.pathToAppSettings = pathToAppSettings
            
        
    def __checkPath(self, path) -> bool:
        if os.path.isdir(path):
            return True
        else:
            raise EnvironmentException("The folder does not exists")
        
    def get_appsetting_value(self, key):
        file = open(self.__pathToAppSettings + "\\appsettings.json", 'r')
        appsettings_dict = json.loads(file.read())
        connectionStrings = appsettings_dict["ConnectionToDatabaseString"]
        return connectionStrings[key]