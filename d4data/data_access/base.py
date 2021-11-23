from abc import abstractmethod, ABC



class BaseDataAccess(ABC):

    @abstractmethod
    def read(self, name):
        raise NotImplemented

    @abstractmethod
    def update(self, name, data):
        raise NotImplemented

    @abstractmethod
    def put(self, name, data):
        raise NotImplemented

    @abstractmethod
    def delete(self, name):
        raise NotImplemented


