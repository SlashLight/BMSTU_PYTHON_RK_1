"""
@brief Message templates for IT Infrastructure Analysis
Contains all user-facing messages and logging templates
"""

class LogMessages:
    """
    @brief Log message templates for analysis operations
    Standardized messages for different logging levels and operations
    """

    # System initialization messages
    SYSTEM_START = "IT Infrastructure Analysis System initialization started"
    SYSTEM_READY = "IT Infrastructure Analysis System ready"
    DATA_LOAD_START = "Starting data loading process from JSON file"
    DATA_LOAD_SUCCESS = "Data successfully loaded from file: {}"
    DATA_LOAD_ERROR = "Error loading data from file: {} - {}"

    # Analysis process messages
    TOTAL_BUDGET_ANALYSIS_START = "Starting {} analysis"
    ANALYSIS_START = "Starting {} analysis"
    ANALYSIS_COMPLETE = "{} analysis completed successfully"
    ANALYSIS_ERROR = "Error during {} analysis: {}"

    # Data processing messages
    DATA_PROCESSING_START = "Starting data processing for {}"
    DATA_FILTERING_START = "Filtering IT equipment from dataset"
    DATA_TRANSFORMATION_START = "Starting data transformation"

    # Equipment analysis messages
    EQUIPMENT_COUNT = "Total IT equipment identified: {} units"
    EQUIPMENT_COST_CALCULATION = "Calculating total equipment costs"
    UTILIZATION_CALCULATION = "Calculating equipment utilization metrics"
    MAINTENANCE_COST_CALCULATION = "Calculating maintenance costs"

class ReportMessages:
    """
    @brief Report message templates for analysis results
    Standardized output messages for different analysis sections
    """

    # Section headers
    INVENTORY_HEADER = "EQUIPMENT INVENTORY ANALYSIS"
    UTILIZATION_HEADER = "EQUIPMENT UTILIZATION ANALYSIS"
    COST_HEADER = "COST ANALYSIS"
    REPLACEMENT_HEADER = "EQUIPMENT REPLACEMENT PLANNING"
    OPTIMIZATION_HEADER = "INFRASTRUCTURE OPTIMIZATION"

    # Results messages
    TOTAL_EQUIPMENT_COUNT = "Total IT equipment identified: {} units"
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