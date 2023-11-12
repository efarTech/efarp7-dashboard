from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

import sys
import os

#sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from repositories.EfarRepository import EfarRepository

class TestEfarRepository:
    def test_when_get_login_data(self):
        """
        test_when_get_login_data method
        """
        repository = EfarRepository('../repositories/data/')
        assert repository.get_login_data() is not None
    
    def test_when_get_api_data(self):
        """
        test_when_get_api_data method
        """
        repository = EfarRepository('../repositories/data/')
        assert repository.get_api_data() is not None
        
    def test_when_get_application_data(self):
        """
        test_when_get_application_data method
        """
        repository = EfarRepository('../repositories/data/')
        assert repository.get_application_data() is not None
    
    def test_when_get_shap_explaine_expected_value_data(self):
        """
        test_when_get_shap_explaine_expected_value_data method
        """
        repository = EfarRepository('../repositories/data/')
        assert repository.get_shap_explaine_expected_value_data() is not None
    
    def test_when_get_shap_values_data(self):
        """
        test_when_get_shap_values_data method
        """
        repository = EfarRepository('../repositories/data/')
        assert repository.get_shap_values_data() is not None
    
    def test_when_get_shap_waterfall_expected_value_data(self):
        """
        test_when_get_shap_waterfall_expected_value_data method
        """
        repository = EfarRepository('../repositories/data/')
        assert repository.get_shap_waterfall_expected_value_data() is not None
        
    def test_when_get_shap_values_waterfall_data(self):
        """
        test_when_get_shap_values_waterfall_data method
        """
        repository = EfarRepository('../repositories/data/')
        assert repository.get_shap_values_waterfall_data() is not None