from dataclasses import dataclass


@dataclass
class Data:
    name: str
    path: str

    def __post_init__(self):
        self.fpath = self.path + self.name

d = Data(name="hi",  path="/home/")
print(d.fpath)
