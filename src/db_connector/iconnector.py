from abc import ABCMeta, abstractmethod

class DBConnector(object):

    __metaclass__ = ABCMeta 

    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def save_all(db):
        pass