"""
@brief Salary analysis module for Financial department
Analyses salary distribution and employee compensation
"""
import pandas as pd
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages

class CostOptimizationAnalyzer(BaseAnalyzer):
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
        super().__init__(json_file_path, "CostOptimizationAnalysis")
        self.cost_df = None

    def execute_analysis(self):
        """
        @brief Create pandas DataFrame for ROI analysis
        Processes ROI data from loaded JSON

        @return: Dictionary containing ROI analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("Cost Optimization"))
        try:    

            general_costs_data = self._calculate_general_costs()
            high_cost_depts_data = self._find_high_operational_cost_departments()
            most_expensive_eq_data = self._find_most_expensive_equipment()

            analysis_results = {
                'general_costs': general_costs_data,
                'high_operational_cost_departments': high_cost_depts_data,
                'most_expensive_equipment': most_expensive_eq_data
            }
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("Cost Optimization"))
        
            return analysis_results
        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("Cost Optimization", str(analysis_error))
            self.logger.error(error_message)
            return {"error": error_message}

    def _calculate_general_costs(self):
        """
        @brief Analyze general costs across all projects
        Calculates total costs and average costs per project

        @return: Dictionary with total and average costs
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("cost optimization"))

        total_purchase_cost = self.equipment_df['purchase_info.cost'].sum()
        total_monthly_cost = self.equipment_df['operational_info.maintenance_cost_per_month'].sum()
        total_annual_cost = total_monthly_cost * 12

        self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("general costs"))

        return {
            'total_purchase_cost': total_purchase_cost,
            'total_monthly_cost': total_monthly_cost,
            'total_annual_cost': total_annual_cost
        }

    def _find_high_operational_cost_departments(self):
        """
        @brief Analyze general costs across all projects
        Calculates total costs and average costs per project

        @return: Dictionary with total and average costs
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("cost optimization"))

        department_costs = self.equipment_df.groupby('department_name')['operational_info.maintenance_cost_per_month'].sum().sort_values(ascending=False)
            
        top_spender_department = department_costs.index[0]
        top_spender_amount = department_costs.iloc[0]

        self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("cost optimization"))
        return {
            'top_spender_department': top_spender_department,
            'top_spender_amount': top_spender_amount,
            'full_rating': department_costs # Сохраняем полный рейтинг для отчета
        }

    def _find_most_expensive_equipment(self):
        """
        @brief Find the most expensive equipment based on maintenance costs
        @return: DataFrame with the most expensive equipment
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("most expensive equipment"))

        most_expensive_equipment = self.equipment_df.sort_values('operational_info.maintenance_cost_per_month', ascending=False).iloc[0]
        self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("most expensive equipment"))
        return most_expensive_equipment

