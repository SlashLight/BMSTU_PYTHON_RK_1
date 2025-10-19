"""
@brief Configuration package for IT infrastructure analysis
Contains enums and message templates for system configuration
"""

from .enums import EquipmentStatus, DepartmentType, EquipmentType, AnalysisPriority, UtilizationLevel
from .messages import LogMessages, ReportMessages, ErrorMessages

__all__ = [
    'EquipmentStatus',
    'DepartmentType',
    'EquipmentType',
    'AnalysisPriority',
    'UtilizationLevel',
    'LogMessages',
    'ReportMessages',
    'ErrorMessages'
]