


class JSONDictRepo:
    def __init__(self, data_access, serializer):
        self.data_access = data_access
        self.serializer = serializer

    def get(self, name):
        data = self.data_access.read(name)
        obj = self.serializer.deserialize(data)
        return obj

    def add(self, name, obj):
        data = self.serializer.serialize(obj)
        self.data_access(name, data)


class JSONListRepo:
    def __init__(self, data_access, serializer, primary_key):
        self.data_access = data_access
        self.serializer = serializer
        self.primary_key = primary_key
        self.objects = self._get_objects()
        self.key_map = self._build_key_map()

        self.object_idx = -1

    def _get_objects(self):
        objects = self.data_access.read()
        return objects

    def _build_key_map(self):
        key_map = {obj[self.primary_key]: obj for obj in self.objects}
        return key_map

    def get(self, name):
        data = self.key_map.get(name, None)
        obj = self.serializer.deserialize(data)
        return obj

    def add(self, name, obj):
        data = self.serializer.serialize(obj)
        assert name == data[self.primary_key]
        self.objects.append(data)
        self.data_access.update("", self.objects)
        self.key_map = self._build_key_map()
        return None

    def __iter__(self):
        return self

    def __next__(self):
        self.object_idx += 1
        if self.object_idx >= len(self.objects):
            self.object_idx = -1
            raise StopIteration
        obj = self.objects[self.object_idx]
        return obj


class JSONDirectoryRepo:
    def __init__(self, file_access, json_access, serializer):
        self.file_access = file_access
        self.json_access = json_access
        self.serializer = serializer

    def get(self, name):
        data = self.key_map.get(name, None)
        obj = self.serializer.deserialize(data)
        return obj

    def add(self, name, obj):
        data = self.serializer.serialize(obj)
        assert name == data[self.primary_key]
        self.objects.append(data)
        self.data_access.update("", self.objects)
        self.key_map = self._build_key_map()
        return None
