This is a template Python project
---------------------------------
This project can be used as a starter for future Python projects. It contains
the setup and configuration files for documentation with readthedocs, automated
testing with TravisCI, and installation with pip.

Installation and Package Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A Python package can be locally "installed" using pip with this command:

.. code-block:: python

    pip install -e <path to package>

requirements.txt
================
List the packages and specific version numbers that you use.

Documentation
~~~~~~~~~~~~~
This template project is configured to produce API documentation as prepared in
docstrings. Docstrings should conform to the
`Google style guide <http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>`__
as much as possible.

A `readthedocs <https://readthedocs.org>`__ config file is included at
``python_template/.readthedocs.yml`` which contains default settings for a
connection to readthedocs. See the readthedocs `config documentation
<https://docs.readthedocs.io/en/stable/config-file/v2.html>`__ for more details.

Testing
~~~~~~~
All tests should be contained in the ``python_template/tests`` directory and
reference the module files in ``python_template/template``.

A config file for TravisCI is included at ``python_template/.travis.yml``.

Things you should modify
~~~~~~~~~~~~~~~~~~~~~~~~
There are some files that will be particular to you project and will need
customization.

Requirements files
==================
There are two requirements files:

- requirements.txt
- docs/requirements.txt

Be sure to add any new dependencies to each!

.vscode/launch.json
===================
This is the configuration file for debugging in Visual Studio Code. Each
language has a unique syntax for the debugger setup. Included here is the
Python version.

.. code-block:: json

        {
            "name": "test 1",
            "type": "python",
            "request": "launch",
            "stopOnEntry": false,
            "pythonPath": "${config:python.pythonPath}",
            "program": "${workspaceRoot}/examples/example_script.py",
            "cwd": "${workspaceRoot}/examples",
        },


setup.py
========
This file configures how installation tools like ``pip`` will build and install
the software. As is, ``setup.py`` is configured for a basic installation. There
is a section that should be modified at the beginning of the file:

.. code-block:: python

    # Package meta-data.
    NAME = 'TEMPLATE'
    DESCRIPTION = 'A template Python project.'
    URL = 'https://github.com/rafmudaf/python_template'
    EMAIL = 'rafael.mudafort@nrel.gov'
    AUTHOR = 'NREL National Wind Technology Center'
    REQUIRES_PYTHON = '>=3.3.0'
    VERSION = '0.1.0'

    # What packages are required for this module to be executed?
    REQUIRED = [
        'numpy==1.16.3',
        'scipy==1.1.0',
        'pytest==5.1.1'
    ]

    # What packages are optional?
    EXTRAS = {
        'docs': {
            'readthedocs-sphinx-ext==0.5.15',
            'Sphinx==2.0',
            'sphinxcontrib-napoleon==0.7'
        }
    }

docs/conf.py
============
Similar to ``setup.py``, this configuration file only requires customization
at the beginning. Otherwise, it is well configured for a basic documentation
build.

The section to configure is denoted by this header:

.. code-block:: python

    # -- General configuration ------------------------------------------------

Things you should NOT modify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Anything outside of the beginning portion in ``setup.py``


Other files contained in this package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Templates for GitHub issues and pull requests at ``.github/``
- An Apache 2.0 license file at ``LICENSE.txt``
- This documentation at ``README.rst``

General Python references
~~~~~~~~~~~~~~~~~~~~~~~~~
- `Intro to Python <https://developers.google.com/edu/python/introduction>`__
- `PEP8 style guide <https://www.python.org/dev/peps/pep-0008/>`__
- `Google style guide <http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>`__
