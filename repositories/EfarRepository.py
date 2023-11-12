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

from modules.file.EfarDataFile import EfarDataFile

class EfarRepository:
    """
    Efardb class
    """
    def __init__(self, directory):
        """
        __init__ method
        """
        self.df_login, self.df_api, self.df_application, self.shap_explaine_expected_value, self.shap_values, self.shap_waterfall_expected_value, self.shap_values_waterfall = self.load_data(directory)

    def load_data(self, directory):
        efardatafile = EfarDataFile(directory)
        df_login = efardatafile.to_data('data_login', 'scr')
        df_api = efardatafile.to_data('data_api', 'scr')
        df_api = df_api.set_index('SK_ID_CURR')
        df_application = efardatafile.to_data('data_application', 'scr')
        df_application = df_application.set_index('SK_ID_CURR')
        shap_explaine_expected_value = efardatafile.to_data('data_shap_explaine_expected_value', 'scr')
        shap_values = efardatafile.to_data('data_shap_values', 'scr')
        shap_waterfall_expected_value = efardatafile.to_data('data_shap_waterfall_expected_value', 'scr')
        shap_values_waterfall = efardatafile.to_data('data_shap_values_waterfall', 'scr')
        
        return df_login, df_api, df_application, shap_explaine_expected_value, shap_values, shap_waterfall_expected_value, shap_values_waterfall
        
    def get_login_data(self):
        """
        get_login_data method
        """
        return self.df_login
    
    def get_api_data(self):
        """
        get_api_data method
        """
        return self.df_api
        
    def get_application_data(self):
        """
        get_application_data method
        """
        return self.df_application
    
    def get_shap_explaine_expected_value_data(self):
        """
        get_shap_explaine_expected_value_data method
        """
        return self.shap_explaine_expected_value
    
    def get_shap_values_data(self):
        """
        get_shap_values_data method
        """
        return self.shap_values
    
    def get_shap_waterfall_expected_value_data(self):
        """
        get_shap_waterfall_expected_value_data method
        """
        return self.shap_waterfall_expected_value
    
    def get_shap_values_waterfall_data(self):
        """
        get_shap_values_waterfall_data method
        """
        return self.shap_values_waterfall
