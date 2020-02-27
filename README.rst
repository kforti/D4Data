
.. image:: https://github.com/kforti/D4Data/blob/master/logo.png

======
D4Data
======

.. image:: https://img.shields.io/pypi/v/d4data.svg
        :target: https://pypi.python.org/pypi/d4data

Data Engineered with python


Proof of concept project for python data engineering. Envisioned use cases:
    - Data access and sharing with data defined as code.
    - Data catologing and discovery.
    - Data transfer and partitioning for distributed computing.
    - Go from remote data sources to model training with simple and expressive python.

Installation
------------
.. code-block:: bash

    pip install d4data

Example API:
------------
Define data as code

.. code-block:: python

    from d4data.storage_clients import FTPStorageClient
    from d4data.sources import CSVDataSource

    class NIHChromosomeSNPS38(CSVDataSource):
        def __init__(self, chromosome, output_path):
            # define data that is specific to your data source
            self.chromosome = chromosome

            # give your data source a name, file name, local paths to save to and uri
            self.name = "NIH_Chromose_{}_SNPS38".format(self.chromosome)
            self.file_name = "bed_chr_{}.bed.gz".format(self.chromosome)
            self.uri = "https://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606_b151_GRCh38p7/BED/" + self.file_name
            self.local_paths = [os.path.join(output_path, self.file_name)]

            # assign a storage client
            self.client = FTPStorageClient()


- Download data programmatically

.. code-block:: python

    data = NIHChromosomeSNPS38(chromosome=1, local_path="./datasources")

    # calls client.download(uri=self.uri)
    data.to_disk()

- Process data

.. code-block:: python

    dataset = data.to_dataset()
    for i in range(len(dataset)):
        some_func(dataset[i])

- Compose DataSources dynamically with a DataStrategy:

.. code-block:: python

    from d4data.storage_clients import HTTPStorageClient
    from d4data.core import DataStrategy, CompositeDataSource

    # Define the DataSource
    class HaploRegSource(CSVDataSource):
        def __init__(self, population, local_path):
            self.name = "LD_{}".format(population.upper())
            self.file_name = self.name + ".tsv.gz"
            self.uri = "https://pubs.broadinstitute.org/mammals/haploreg/data/" + self.file_name
            self.local_paths = [os.path.join(local_path, self.file_name)]

            self.client = HTTPStorageClient()

    # Define the DataStrategy
    # Data Strategies contain logic for building data sources from some higher level data about the data, e.g list of s3 urls.
    # Data Strategies can also contain a partition strategy where logic for partitioning data sources can be implemented- you may want to partition based on compute resources available.
    class HaploRegStrategy(DataStrategy):
        def __init__(self, populations, local_path):
            self.populations = populations
            self.local_path = local_path

            self._sources = {
                "haplo_reg": HaploRegSource
            }

        def create_sources(self):
            comp_source = CompositeDataSource()
            source = self._sources["haplo_reg"]
            for population in self.populations:
                ds = source(population, self.local_path)
                comp_source.add(ds)
            return comp_source

    pops = ["afr", "eur", "amr]
    haplo_strategy = HaploRegStrategy(pops, local_path="./data_sources")
    comp_source = haplo_strategy.create_sources()
    for source in comp_source:
        # Download sources to in-memory file system
        d = s.to_memfs()

- Prefect Integration: TODO

- Pytorch Integration: TODO

* Free software: Apache Software License 2.0
* Documentation: https://d4data.readthedocs.io.


Features
--------

* TODO

