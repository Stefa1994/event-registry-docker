from abc import ABCMeta, abstractmethod

class Collector(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def connect_to_service(self):
        pass
    
    @abstractmethod
    def exec_query(self, filters = None):
        pass