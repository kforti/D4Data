from d4data.core import D4Dataset

import pandas as pd


class CSVDataset(D4Dataset):
    def __init__(self, names, paths):
        self.names = names
        self.paths = paths

    def __getitem__(self, index):
        pass

    def to_dataframe(self):
        df = pd.read_csv(self._local_path, **self.dataframe_key_words)
        return df
