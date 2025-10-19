"""
@brief Salary analysis module for Financial department
Analyses salary distribution and employee compensation
"""

import pandas as pd
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages


class RoiAnalyzer(BaseAnalyzer):
    """
    @brief ROI analysis module for Financial department
    Analyzes return on investment for various projects
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize ROI analyzer with data source
        Sets up data loading and logger configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "ROI Analysis")
        self.roi_dataframe = None

    def execute_analysis(self):
        """
        @brief Create pandas DataFrame for ROI analysis
        Processes ROI data from loaded JSON

        @return: Dictionary containing ROI analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("ROI"))

        try:
            self.completed_projects = self.projects_df[self.projects_df['status'] == 'completed']
            self.completed_projects['calculated_roi'] = (self.completed_projects['financials.profit'] / self.completed_projects['financials.actual_cost']) * 100

            # General ROI analysis
            general_roi = self._analyze_general_roi()

            # Effective ROI per department
            effective_roi_department, ineffective_roi_department, department_roi = self._analyze_effective_roi_per_department()

            # Correlation between budget and ROI
            correlation = self._analyze_roi_budget_correlation(department_roi)

            # Compile results
            analysis_results = {
                "general_roi": general_roi,
                "department_roi": department_roi,
                "effective_roi_department": effective_roi_department,
                "ineffective_roi_department": ineffective_roi_department,
                "roi_budget_correlation": correlation,
            }

            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("ROI"))

            return analysis_results

        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("ROI", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _analyze_general_roi(self):
        """
        @brief Analyze general ROI across all projects
        Calculates total ROI and average ROI per project

        @return: Dictionary with total and average ROI
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("general ROI"))

        total_profit = self.completed_projects['financials.profit'].sum()
        total_cost = self.completed_projects['financials.actual_cost'].sum()

        general_roi = (total_profit / total_cost) * 100 if total_cost > 0 else 0

        self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("general ROI"))

        return general_roi
    
    def _analyze_effective_roi_per_department(self):
        """
        @brief Analyze effective ROI per department
        Identifies departments with effective and ineffective ROI

        @return: Tuple with effective and ineffective departments
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("effective ROI per department"))

        self.completed_projects['main_department'] = self.completed_projects['participating_departments'].apply(lambda depts: depts[0]['department_name'] if isinstance(depts, list) and depts else 'Не указан')

        department_roi = self.completed_projects.groupby('main_department')['calculated_roi'].mean().sort_values(ascending=False)

        effective_roi_department = department_roi.index[0]
        ineffective_roi_department = department_roi.index[-1]

        self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("effective ROI per department"))

        return effective_roi_department, ineffective_roi_department, department_roi
    
    def _analyze_roi_budget_correlation(self, department_roi):
        """
        @brief Analyze correlation between budget and ROI
        Calculates correlation coefficient between budget and ROI

        @return: Correlation coefficient value
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("ROI-budget correlation"))

        department_roi_df = department_roi.reset_index()
        department_roi_df.columns = ['name', 'average_roi']

        budget_and_roi = pd.merge(self.departments_df, department_roi_df, on='name')
        correlation = budget_and_roi['budget'].corr(budget_and_roi['average_roi'])

        self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("ROI-budget correlation"))

        return correlation