"""
@brief Message templates for Financial Analysis System
Contains all user-facing messages and logging templates
"""

class LogMessages:
    """
    @brief Log message templates for analysis operations
    Standardized messages for different logging levels and operations
    """

    # System initialization messages
    SYSTEM_START = "Financial Analysis System initialization started"
    SYSTEM_READY = "Financial Analysis System ready"
    DATA_LOAD_START = "Starting data loading process from JSON file"
    DATA_LOAD_SUCCESS = "Data successfully loaded from file: {}"
    DATA_LOAD_ERROR = "Error loading data from file: {} - {}"

    # Analysis process messages
    TOTAL_BUDGET_ANALYSIS_START = "Starting total budget calculation"
    ANALYSIS_START = "Starting {} analysis"
    ANALYSIS_COMPLETE = "{} analysis completed successfully"
    ANALYSIS_ERROR = "Error during {} analysis: {}"

    # Data processing messages
    DATA_PROCESSING_START = "Starting data processing for {}"
    DATA_FILTERING_START = "Filtering data from dataset"
    DATA_TRANSFORMATION_START = "Starting data transformation"

    # Calculation messages
    BUDGET_CALCULATION = "Calculating budget metrics"
    SALARY_CALCULATION = "Calculating salary metrics"
    ROI_CALCULATION = "Calculating ROI metrics"
    COST_CALCULATION = "Calculating cost metrics"

class ReportMessages:
    """
    @brief Report message templates for analysis results
    Standardized output messages for different analysis sections
    """

    # Section headers
    BUDGET_HEADER = "BUDGET ANALYSIS"
    SALARY_HEADER = "SALARY ANALYSIS"
    ROI_HEADER = "ROI ANALYSIS"
    COST_HEADER = "COST OPTIMIZATION ANALYSIS"
    PLANNING_HEADER = "FINANCIAL PLANNING ANALYSIS"
    SUMMARY_HEADER = "COMPREHENSIVE FINANCIAL ANALYSIS SUMMARY"

    # Separator
    SEPARATOR = "=" * 70
    SHORT_SEPARATOR = "-" * 70

    # Section messages
    BUDGET_SECTION = "\nEXECUTING BUDGET ANALYSIS..."
    SALARY_SECTION = "\nEXECUTING SALARY ANALYSIS..."
    ROI_SECTION = "\nEXECUTING ROI ANALYSIS..."
    COST_SECTION = "\nEXECUTING COST OPTIMIZATION ANALYSIS..."
    PLANNING_SECTION = "\nEXECUTING FINANCIAL PLANNING ANALYSIS..."
    TOTAL_EQUIPMENT_COST = "Total IT assets value: {:,.0f} RUB"
    AVERAGE_UTILIZATION = "Average equipment utilization rate: {:.1f}%"
    ANNUAL_MAINTENANCE_COST = "Annual maintenance costs: {:,.0f} RUB"

    # Recommendation messages
    CONSOLIDATION_RECOMMENDATION = "Recommended consolidation measures"
    COST_SAVINGS_POTENTIAL = "Potential annual savings: {:,.0f} RUB"
    REPLACEMENT_PRIORITY = "Equipment replacement priority list generated"

class ErrorMessages:
    """
    @brief Error message templates
    Standardized error messages for exception handling
    """

    FILE_NOT_FOUND = "Configuration file not found: {}"
    INVALID_JSON = "Invalid JSON format in file: {}"
    DATA_VALIDATION_ERROR = "Data validation error: {}"
    CALCULATION_ERROR = "Calculation error in {}: {}"