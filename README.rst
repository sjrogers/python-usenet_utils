========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-usenet_utils/badge/?style=flat
    :target: https://readthedocs.org/projects/python-usenet_utils
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/sjrogers/python-usenet_utils.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/sjrogers/python-usenet_utils

.. |requires| image:: https://requires.io/github/sjrogers/python-usenet_utils/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/sjrogers/python-usenet_utils/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/sjrogers/python-usenet_utils/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/sjrogers/python-usenet_utils

.. |version| image:: https://img.shields.io/pypi/v/usenet-utils.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/usenet-utils

.. |commits-since| image:: https://img.shields.io/github/commits-since/sjrogers/python-usenet_utils/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/sjrogers/python-usenet_utils/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/usenet-utils.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/usenet-utils

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/usenet-utils.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/usenet-utils

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/usenet-utils.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/usenet-utils


.. end-badges

miscellaneous utilities for building usenet applications

* Free software: Apache Software License 2.0

Installation
============

::

    pip install usenet-utils

Documentation
=============

https://python-usenet_utils.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
