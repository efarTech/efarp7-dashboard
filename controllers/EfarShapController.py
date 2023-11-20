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

class EfarShapController:
    """
    Efardb class
    """
    def __init__(self, repository):
        """
        __init__ method
        """
        self.shap_explaine_expected_value = repository.get_shap_explaine_expected_value_data()
        self.shap_values = repository.get_shap_values_data()
        self.shap_waterfall_expected_value = repository.get_shap_waterfall_expected_value_data()
        self.shap_values_waterfall = repository.get_shap_values_waterfall_data()
    
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
        