import os
import sys 

sys.path.append("./Environment")

from Environment import Environment

env = Environment("grgrewg")

print(env.pathToAppSettings)