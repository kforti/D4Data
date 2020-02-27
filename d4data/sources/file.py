import os

from d4data.datasets.csv_dataset import CSVDataset

from ..core import DataSource

class CSVDataSource(DataSource):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_memfs(self, path=None):
        pass

    def to_disk(self, uri=None, path=None):
        """ Downloads datasource from uri to local path; will take arguments- and set object attributes to those arguments- or default to objecta attributes."""
        if path:
            self._local_path = path
        if uri:
            self._uri = uri
        self.client.download(self.uri, self._local_path)

    def to_dataset(self):
        names = [self.name + os.path.basename(path) for path in self.local_paths]
        return CSVDataset(names=names, paths=self.local_paths)


