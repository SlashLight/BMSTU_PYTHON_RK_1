"""
@brief Enumerations for IT Infrastructure Analysis
Contains all enum classes used across the analysis modules
"""

from enum import Enum

class EquipmentStatus(Enum):
    """
    @brief Equipment operational status enumeration
    Defines possible states of IT equipment
    """
    OPERATIONAL = "operational"
    MAINTENANCE = "maintenance"
    BROKEN = "broken"
    RETIRED = "retired"

class DepartmentType(Enum):
    """
    @brief Department type classification enumeration
    Categorizes company departments by their function
    """
    TECHNICAL = "technical"
    PRODUCTION = "production"
    COMMERCIAL = "commercial"
    ADMINISTRATIVE = "administrative"
    RESEARCH = "research"

class EquipmentType(Enum):
    """
    @brief IT equipment type classification
    Defines categories of IT equipment for analysis
    """
    SERVER = "Сервер"
    WORKSTATION = "Рабочая станция"
    LAPTOP = "Ноутбук"
    MONITOR = "Монитор"
    NETWORK_EQUIPMENT = "Сетевое оборудование"
    PRINTER = "Принтер"
    SCANNER = "Сканер"
    TELEPHONE = "Телефон"
    PROJECTOR = "Проектор"

class AnalysisPriority(Enum):
    """
    @brief Priority levels for equipment replacement
    Defines urgency levels for equipment modernization
    """
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class UtilizationLevel(Enum):
    """
    @brief Equipment utilization level categories
    Classifies equipment based on usage efficiency
    """
    VERY_LOW = "very_low"      # < 30%
    LOW = "low"               # 30-50%
    MEDIUM = "medium"         # 50-70%
    HIGH = "high"             # 70-85%
    VERY_HIGH = "very_high"   # > 85%