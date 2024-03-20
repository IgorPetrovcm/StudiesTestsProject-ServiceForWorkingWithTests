import os
import sys

sys.path.append("./Exceptions")

from EnvironmentException import EnvironmentException

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