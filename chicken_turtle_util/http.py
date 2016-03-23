# Copyright (C) 2015, 2016 VIB/BEG/UGent - Tim Diels <timdiels.m@gmail.com>
# 
# This file is part of Chicken Turtle Util.
# 
# Chicken Turtle Util is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Chicken Turtle Util is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with Chicken Turtle Util.  If not, see <http://www.gnu.org/licenses/>.

'''
HTTP utilities
'''

from urllib.parse import urlparse
from pathlib import Path
import requests
import re

URL_MAX_LENGTH = 2000  # http://stackoverflow.com/a/417184/1031434

# Based on http://stackoverflow.com/a/16696317/1031434
def download_file(url, destination):
    '''
    Download an HTTP resource
    
    Parameters
    ----------
    url : str
        HTTP resource to download
    destination : pathlib.Path
        Location at which to store downloaded resource. If `destination` does
        not exist, it's assumed to be a file path. If `destination` exists and
        is a file, it is overwritten. If `destination` exists and is a
        directory, the file will be saved inside the directory with as name the
        file name suggested by a server, if any, or the last part of the URL
        otherwise (excluding query and fragment parts).
    
    Returns
    -------
    path : pathlib.Path
        Path to the downloaded file.
    name : str or None
        File name suggested by the server or None if none was suggested.
    '''
    response = requests.get(url, stream=True)
    
    # Get file name suggested by server
    file_name = None
    if 'content-disposition' in response.headers:
        match = re.match(r'filename=(.+)', response.headers['content-disposition'])
        if match:
            file_name = match.groups(0)
            
    # Ensure destination is a file
    if destination.is_dir():
        if file_name:
            destination /= file_name
        else:
            destination /= Path(urlparse(url).path).name
    
    # Download
    with destination.open('wb') as f:
        for chunk in response.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive chunks
                f.write(chunk)
    return destination, file_name
