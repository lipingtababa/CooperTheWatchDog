
from enum import Enum

class Corporation(Enum):
    AWS = 1
    OPENAI = 2

class Analyst():
    def __init__(self, corporation, dataFolder):
        self.corporation = corporation
        self.dataFolder = dataFolder
    def initialize(self):
        raise NotImplementedError("Subclasses must implement this method")
    def analysis(self):
        raise NotImplementedError("Subclasses must implement this method") 
