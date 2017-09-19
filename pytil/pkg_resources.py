# Copyright (C) 2017 VIB - Tim Diels <timdiels.m@gmail.com>
#
# This file is part of pytil.
#
# pytil is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pytil is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pytil.  If not, see <http://www.gnu.org/licenses/>.

'''
Additions to pkg_resources
'''

from pkg_resources import resource_filename  # @UnresolvedImport
from pathlib import Path

def resource_path(package_or_requirement, resource_name):
    '''
    Like resource_filename but return a pathlib.Path instead
    '''
    return Path(resource_filename(package_or_requirement, resource_name))
