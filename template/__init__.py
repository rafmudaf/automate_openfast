# Copyright 2019 NREL

# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of the
# License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

"""
The :py:obj:`template` package contains :py:obj:`template.utilities` module
and other packages which make up the software.

All modules and package can be imported with

    >>> import template

The ``__init__.py`` file enables the import of all modules in this
package so any additional modules should be included there.

Examples:
    >>> import template
    
    >>> dir(template)
    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
    '__name__', '__package__', '__path__', '__spec__', 'utilities']

    >>> dir(template.utilities)
    ['Output', 'Vec3', '__builtins__', '__cached__', '__doc__',
    '__file__', '__loader__', '__name__', '__package__', '__spec__',
    'cosd', 'np', 'sind', 'tand', 'wrap_180', 'wrap_360']
"""

from . import utilities
