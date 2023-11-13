from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

import os

from datetime import datetime, date

import pandas as pd
import numpy as np

import warnings
import logging

from flask import Flask, jsonify
from repositories.EfarRepository import EfarRepository

class EfarShapController:
    """
    Efardb class
    """
    def __init__(self, directory):
        """
        __init__ method
        """
        self.repository = EfarRepository(directory)
        self.shap_explaine_expected_value = self.repository.get_shap_explaine_expected_value_data()
        self.shap_values = self.repository.get_shap_values_data()
        self.shap_waterfall_expected_value = self.repository.get_shap_waterfall_expected_value_data()
        self.shap_values_waterfall = self.repository.get_shap_values_waterfall_data()
    
    def get_shap_explaine_expected_value(self):
        """
        get_shap_explaine_expected_value method
        """
        return self.shap_explaine_expected_value
    
    def get_shap_values(self):
        """
        get_shap_values method
        """
        return self.shap_values
    
    def get_shap_waterfall_expected_value(self):
        """
        get_shap_waterfall_expected_value method
        """
        return self.shap_waterfall_expected_value
    
    def get_shap_values_waterfall(self):
        """
        get_shap_values_waterfall method
        """
        return self.shap_values_waterfall
        