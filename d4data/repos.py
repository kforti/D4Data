



class Repo:
    def __init__(self, data_access, serializer, index_key=None):
        self.data_access = data_access
        self.serializer = serializer
        self.index_key = index_key

    def get(self, index):
        data = self.data_access.read(index)
        obj = self.serializer.deserialize(data)
        return obj

    def add(self, obj, index=None):
        data = self.serializer.serialize(obj)
        self.data_access(index, data)
