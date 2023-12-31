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

class EfarScoringController:
    """
    Efardb class
    """
    def __init__(self, repository):
        """
        __init__ method
        """
        self.api_data = repository.get_api_data()
        self.application_data = repository.get_application_data()
    
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
        