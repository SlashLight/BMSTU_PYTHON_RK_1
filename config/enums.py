"""
@brief Enumerations for Financial Analysis System
Contains all enum classes used across the analysis modules
"""

from enum import Enum

class AnalysisType(Enum):
    """
    @brief Analysis type enumeration
    Defines types of financial analyses available
    """
    BUDGET = "budget"
    SALARY = "salary"
    ROI = "roi"
    COST_OPTIMIZATION = "cost_optimization"
    FINANCIAL_PLANNING = "financial_planning"

class DepartmentCategory(Enum):
    """
    @brief Department category classification
    Groups departments by their primary function
    """
    TECHNICAL = "technical"
    COMMERCIAL = "commercial"
    ADMINISTRATIVE = "administrative"
    PRODUCTION = "production"
    RESEARCH = "research"

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