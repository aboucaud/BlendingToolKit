![tests](https://github.com/LSSTDESC/BlendingToolKit/workflows/tests/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/blendingtoolkit/badge/?version=latest)](https://blendingtoolkit.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/LSSTDESC/BlendingToolKit/branch/master/graph/badge.svg)](https://codecov.io/gh/LSSTDESC/BlendingToolKit)

**NOTE:** BTK is currently in development and rapidly changing, as such the documentation and most jupyter notebooks are deprecated. We will release a new stable version of BTK in the near future and fix these issues. 

# BlendingToolKit
Framework for fast generation and analysis of galaxy blends catalogs. This toolkit is a convenient way of
producing multi-band postage stamp images of blend scenes.

Documentation can be found at https://blendingtoolkit.readthedocs.io/en/latest/

## Workflow
<img src="docs/source/images/flow_chart.png" alt="btk workflow" width="450"/>


## Running BlendingToolKit
- BlendingToolKit (btk) requires an input catalog that contains information required to simulate galaxies and blends.
This repository includes sample input catalogs with a small number of galaxies that can be used to draw blend images with btk. See [tutorials](https://github.com/LSSTDESC/BlendingToolKit/tree/master/notebooks) to learn how to run btk with these catalogs.
- CatSim Catalog corresponding to one square degree of sky and processed WeakLensingDeblending catalogs can be downloaded from [here](https://stanford.app.box.com/s/s1nzjlinejpqandudjyykjejyxtgylbk).
- [Cosmo DC2](https://arxiv.org/abs/1907.06530) catalog requires pre-processing in order to be used as input catalog to btk. Refer to this [notebook](https://github.com/LSSTDESC/WeakLensingDeblending/blob/cosmoDC2_ingestion/notebooks/wld_ingestion_cosmoDC2.ipynb) on how to convert the DC2 catalog into a CatSim-like catalog that can be analyzed with btk.

## Requirements
The code is intended to run in python >=3.7.
To run btk you need to install
- [WeakLensingDeblending](https://github.com/LSSTDESC/WeakLensingDeblending)
- [GalSim](https://github.com/GalSim-developers/GalSim/)
- numpy
- astropy
- fitsio
- scipy
- lmfit

More detailed installation instructions can be found [here](https://blendingtoolkit.readthedocs.io/en/latest/install.html).

### Optional
The tutorials include examples of using btk with some detection, deblending or measurement packages including
- [scarlet](https://github.com/fred3m/scarlet/) (multi-band deblender)
- [sep](https://sep.readthedocs.io/en/v1.0.x/index.html) (Source Extraction and Photometry)
- [lsst](https://pipelines.lsst.io) (LSST science pipeline)
