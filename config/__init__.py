"""
@brief Configuration package for IT infrastructure analysis
Contains enums and message templates for system configuration
"""

from .enums import AnalysisType, DepartmentCategory, UtilizationLevel
from .messages import LogMessages, ReportMessages, ErrorMessages

__all__ = [
    'AnalysisType',
    'DepartmentCategory',
    'UtilizationLevel',
    'LogMessages',
    'ReportMessages',
    'ErrorMessages'
]