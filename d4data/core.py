import os
from dataclasses import dataclass

from torch.utils.data.dataset import Dataset
from build.lib.d4data.core import StorageClient



CONTEXT = {"cloud": None,
           "sources": []}


class D4Dataset(Dataset):
    pass


@dataclass
class DataSource:

    def to_disk(self):
        """ Downloads datasource from uri to local path; will take arguments- and set object attributes to those arguments- or default to objecta attributes."""
        self.client.download(self.uri, self._local_path)


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


def catalog(cls):
    CONTEXT["sources"].append(cls)
    return cls

def get_sources():
    return CONTEXT["sources"]


