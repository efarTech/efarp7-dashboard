from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

import os

from datetime import datetime, date

import pandas as pd
import numpy as np

import joblib
import warnings
import dill
import logging

from flask import Flask, jsonify
from repositories.EfarRepository import EfarRepository

class EfarScoringController:
    """
    Efardb class
    """
    def __init__(self, directory):
        """
        __init__ method
        """
        self.repository = EfarRepository(directory)
        self.api_data = self.repository.get_api_data()
        self.application_data = self.repository.get_application_data()
    
    def get_api(self):
        """
        get_api method
        """
        return self.api_data
    
    def get_application(self):
        """
        get_application method
        """
        return self.application_data
        