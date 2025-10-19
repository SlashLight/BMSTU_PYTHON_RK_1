"""
@brief Base analyzer class for company-wide data analysis
Provides common functionality for loading and preparing financial and HR data.
"""

import pandas as pd
import json
from utils.logger import analysis_logger
from config.messages import LogMessages

class BaseAnalyzer:
    """
    @brief Base class for all company data analyzers.
    Implements common data loading and processing from the main JSON file.
    """

    def __init__(self, json_file_path, analysis_name):
        """
        @brief Initialize base analyzer with data source.
        """
        self.json_file_path = json_file_path
        self.analysis_name = analysis_name
        self.logger = analysis_logger.get_analysis_logger(analysis_name)
        self.data = None

        self.departments_df = pd.DataFrame()
        self.employees_df = pd.DataFrame()
        self.kpi_metrics_df = pd.DataFrame()
        self.projects_df = pd.DataFrame()
        self.equipment_df = pd.DataFrame()
        self.company_overview_df = pd.DataFrame()

        self.logger.info(LogMessages.SYSTEM_START)
        self._load_data()
        self._setup_dataframes()

    def _load_data(self):
        """
        @brief Load JSON data from specified file path.
        (Этот метод универсален и не требует изменений)
        """
        self.logger.info(LogMessages.DATA_LOAD_START)
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as json_file:
                self.data = json.load(json_file)
            self.logger.info(LogMessages.DATA_LOAD_SUCCESS.format(self.json_file_path))
        except Exception as loading_error:
            error_message = LogMessages.DATA_LOAD_ERROR.format(
                self.json_file_path, str(loading_error)
            )
            self.logger.error(error_message)
            raise loading_error

    def _setup_dataframes(self):
        """
        @brief Create pandas DataFrames from loaded JSON data.
        """
        self.logger.info(LogMessages.DATA_PROCESSING_START.format(self.analysis_name))

        if not self.data:
            self.logger.warning("JSON data is empty. Cannot create DataFrames.")
            return

        if 'departments' in self.data:
            self.departments_df = pd.DataFrame(self.data.get('departments', []))
            self.logger.info(f"Loaded {len(self.departments_df)} departments.")

        if 'employees' in self.data:
            self.employees_df = pd.json_normalize(self.data.get('employees', []))
            self.logger.info(f"Loaded {len(self.employees_df)} employees.")

        if 'kpi_metrics' in self.data:
            self.kpi_metrics_df = pd.json_normalize(self.data.get('kpi_metrics', []))
            self.logger.info(f"Loaded KPI metrics for {len(self.kpi_metrics_df)} departments.")

        if 'projects' in self.data:
            self.projects_df = pd.json_normalize(self.data.get('projects', []))
            self.logger.info(f"Loaded {len(self.projects_df)} projects.")

        if 'equipment' in self.data:
            self.equipment_df = pd.json_normalize(self.data.get('equipment', []))
            self.logger.info(f"Loaded {len(self.equipment_df)} equipment items.")

        if 'company_overview' in self.data:
            self.company_overview_df = pd.DataFrame(self.data.get('company_overview', []))
            self.logger.info(f"Loaded company overview with {len(self.company_overview_df)} records.")

    def execute_analysis(self):
        """
        @brief Execute the analysis (to be implemented by subclasses).
        (Этот метод не требует изменений)
        """
        raise NotImplementedError("Subclasses must implement execute_analysis method")