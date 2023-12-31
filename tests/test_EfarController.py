from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

import sys
import os

#sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from flask import Flask
from repositories.EfarRepository import EfarRepository
from controllers.EfarScoringController import EfarScoringController
from controllers.EfarLoginController import EfarLoginController
from controllers.EfarShapController import EfarShapController

class TestEfarController:
    def test_when_get_login(self):
        """
        test_when_get_login_data method
        """
        repository = EfarRepository('../repositories/data/')
        loginController = EfarLoginController(repository)
        assert loginController.get_login() is not None
    
    def test_when_get_api(self):
        """
        test_when_get_api_data method
        """
        repository = EfarRepository('../repositories/data/')
        scoringController = EfarScoringController(repository)
        assert scoringController.get_api() is not None
        
    def test_when_get_application(self):
        """
        test_when_get_application_data method
        """
        repository = EfarRepository('../repositories/data/')
        scoringController = EfarScoringController(repository)
        assert scoringController.get_application() is not None
    
    def test_when_get_shap_explaine_expected_value(self):
        """
        test_when_get_shap_explaine_expected_value_data method
        """
        repository = EfarRepository('../repositories/data/')
        shapController = EfarShapController(repository)
        assert shapController.get_shap_explaine_expected_value() is not None
    
    def test_when_get_shap_values(self):
        """
        test_when_get_shap_values_data method
        """
        repository = EfarRepository('../repositories/data/')
        shapController = EfarShapController(repository)
        assert shapController.get_shap_values() is not None
    
    def test_when_get_shap_waterfall_expected_value(self):
        """
        test_when_get_shap_waterfall_expected_value method
        """
        repository = EfarRepository('../repositories/data/')
        shapController = EfarShapController(repository)
        assert shapController.get_shap_waterfall_expected_value() is not None
        
    def test_when_get_shap_values_waterfall(self):
        """
        test_when_get_shap_values_waterfall method
        """
        repository = EfarRepository('../repositories/data/')
        shapController = EfarShapController(repository)
        assert shapController.get_shap_values_waterfall() is not None