from torch.utils.data.dataset import Dataset



class DataSource:
    def __init__(self, local_path=None):
        self._local_path = local_path
        self.name = "Datasource"

    def to_disk(self):
        raise NotImplemented

    def to_memfs(self):
        raise NotImplemented

    def to_dataset(self):
        raise NotImplemented

    @property
    def local_paths(self):
        return self._local_paths

    @local_paths.setter
    def local_paths(self, value):
        self._local_paths = value

    @property
    def uri(self):
        return self._uri

    @uri.setter
    def uri(self, value):
        self._uri = value

    def __str__(self):
        return self.name


class StorageClient:
    def __init__(self):
        pass

    def download(self):
        pass


class CompositeDataSource:
    def __init__(self, sources=None):
        self._sources = {}
        if sources:
            for s in sources:
                self._sources[s.name] = s

    def add(self, source):
        self._sources[source.name] = source

    def __iter__(self):
        self._count = 0
        return iter([source for name, source in self._sources.items()])

    def __getitem__(self, item):
        return self._sources[item.name]

    def __setitem__(self, key, value):
        self._sources[key] = value


class DataStrategy:
    pass


class D4Dataset(Dataset):
    def to_dataset(self):
        raise NotImplemented


