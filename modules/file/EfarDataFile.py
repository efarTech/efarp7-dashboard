from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

import os 
from datetime import datetime, date

import dill
import logging

class EfarDataFile:
    """EfarDataFile class"""
    def __init__(self, directory):
        """__init__ method"""
        self.directory = directory
        self.stage='DataFile:'
        
    def to_data(self, filename, extension):
        """to_data method"""
        if((not bool(filename)) or (not bool(extension))):
            return
        path = os.path.join(self.directory, f'{filename}.{extension}')
        
        try:
            if (os.path.exists(path) == False):
                print(f'\033[1m>>>\033[0m [{datetime.now()}][\033[1m{self.stage}\033[0m] File [{path}] not found')
            
            with open(path, 'rb') as file:
                data = dill.load(file)

            return data
        except Exception as err:
            logging.exception(err)

    def to_file(self, data, filename, extension):
        """to_file method"""
        if((data is None) or (not bool(filename)) or (not bool(extension))):
            return
        path = os.path.join(self.directory, f'{filename}.{extension}')
        
        try:
            if (os.path.exists(self.directory) == False):
                os.makedirs(self.directory, exist_ok=True) 

            if os.path.exists(path):
                os.remove(path)
                
            with open(path, 'wb') as file:
                dill.dump(data, file)
        except Exception as err:
            logging.exception(err)