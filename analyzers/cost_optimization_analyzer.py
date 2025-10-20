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
        @brief Create pandas DataFrame for cost optimization analysis
        Processes cost data from loaded JSON

        @return: Dictionary containing cost optimization analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("Cost Optimization"))
        try:
            # Print section header
            print("=" * 70)
            print("COST OPTIMIZATION ANALYSIS")
            print("=" * 70)
            
            general_costs_data = self._calculate_general_costs()
            print(f"\nEquipment Cost Summary:")
            print(f"  Total Purchase Cost:          {general_costs_data['total_purchase_cost']:>15,.0f} RUB")
            print(f"  Total Monthly Maintenance:    {general_costs_data['total_monthly_cost']:>15,.0f} RUB")
            print(f"  Total Annual Maintenance:     {general_costs_data['total_annual_cost']:>15,.0f} RUB")
            
            maintenance_ratio = (general_costs_data['total_annual_cost'] / general_costs_data['total_purchase_cost'] * 100)
            print(f"  Maintenance/Purchase Ratio:   {maintenance_ratio:>14.1f}%")
            
            high_cost_depts_data = self._find_high_operational_cost_departments()
            print(f"\nDepartments with Highest Operational Costs (Top 10):")
            top_10_depts = high_cost_depts_data['full_rating'].head(10)
            for dept_name, monthly_cost in top_10_depts.items():
                print(f"  {dept_name:40s} {monthly_cost:>12,.0f} RUB/month")
            
            most_expensive_eq_data = self._find_most_expensive_equipment()
            print(f"\nMost Expensive Equipment (by maintenance cost):")
            print(f"  Name: {most_expensive_eq_data['name']}")
            print(f"  Type: {most_expensive_eq_data['type']}")
            print(f"  Department: {most_expensive_eq_data['department_name']}")
            print(f"  Monthly Maintenance: {most_expensive_eq_data['operational_info.maintenance_cost_per_month']:,.0f} RUB")
            print(f"  Annual Cost: {most_expensive_eq_data['operational_info.maintenance_cost_per_month'] * 12:,.0f} RUB")
            
            print(f"\nRECOMMENDATIONS FOR COST OPTIMIZATION:")
            print(f"1. Audit equipment usage in {high_cost_depts_data['top_spender_department']} (highest costs)")
            print(f"2. Review maintenance contracts - current ratio of {maintenance_ratio:.1f}% is high")
            print(f"3. Consider consolidating or replacing high-maintenance equipment")
            print(f"4. Implement preventive maintenance program to reduce costs")

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
            'full_rating': department_costs
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

