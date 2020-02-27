from typing import Any

import prefect
from d4data.core import DataSource
from prefect.utilities.tasks import defaults_from_attrs


class DownloadTask(prefect.Task):
    """
    """
    def __init__(
        self,
        data_source: DataSource,
        disk_memfs: str,
        **kwargs: Any
    ):
        self.data_source = data_source
        self.disk_memfs = disk_memfs
        super().__init__(**kwargs)

    @defaults_from_attrs("data_source", "disk_memfs")
    def run(self, data_source: DataSource = None, disk_memfs: str = None, **kwargs) -> str:
        if disk_memfs == "disk":
            data_source.to_disk(**kwargs)
        elif disk_memfs == "memfs":
            data_source.to_memfs(**kwargs)
