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

class EfarLoginController:
    """
    Efardb class
    """
    def __init__(self, repository):
        """
        __init__ method
        """
        self.login_data = repository.get_login_data()
    
    def get_login(self):
        """
        get_login method
        """
        return self.login_data
        