
.. image:: ./logo.png

======
D4Data
======
Data Engineered with python

.. image:: https://img.shields.io/pypi/v/d4data.svg
        :target: https://pypi.python.org/pypi/d4data

.. image:: https://img.shields.io/travis/kforti/d4data.svg
        :target: https://travis-ci.com/kforti/d4data

.. image:: https://readthedocs.org/projects/d4data/badge/?version=latest
        :target: https://d4data.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Proof of concept project for python data engineering. Envisioned use cases:
    - Data access and sharing with data defined as code.
    - Data catologing and discovery.
    - Data transfer and partitioning for distributed computing.
    - Go from remote data sources to model training with simple and expressive python.

Example API:
 - Define your data


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

 - Download data


.. code-block:: python
    data = NIHChromosomeSNPS38(chromosome=1, local_path="./datasources")

    # calls client.download(uri=self.uri)
    data.to_disk()
    dataset = data.to_dataset()


* Free software: Apache Software License 2.0
* Documentation: https://d4data.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
