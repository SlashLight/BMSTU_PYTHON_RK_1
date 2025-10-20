"""
@brief Company overview module for Financial department
Analyses overall company performance and key metrics
"""

import pandas as pd
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages


class CompanyOverviewAnalyzer(BaseAnalyzer):
    """
    @brief Company overview analysis module
    Analyzes overall company performance and key metrics
    """

    def __init__(self, json_file_path, roi_results):
        """
        @brief Initialize company overview analyzer with data source
        Sets up data loading and logger configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "Company Overview Analysis")
        self.company_overview_dataframe = None
        self.roi_results = roi_results

    def execute_analysis(self):
        """
        @brief Create pandas DataFrame for company overview analysis
        Processes company overview data from loaded JSON

        @return: Dictionary containing company overview analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("Financial Planning"))

        try:
            # Print section header
            print("=" * 70)
            print("FINANCIAL PLANNING ANALYSIS")
            print("=" * 70)
            
            break_even_point = self._calculate_break_even_point()
            
            print(f"\nBreak-Even Point Calculation:")
            total_salary = self.employees_df['work_info.salary'].sum()
            total_maintenance = self.equipment_df['operational_info.maintenance_cost_per_month'].sum()
            fixed_costs_annual = (total_salary + total_maintenance) * 12
            
            print(f"  Annual Fixed Costs:")
            print(f"    Salaries:                   {total_salary * 12:>15,.0f} RUB")
            print(f"    Equipment Maintenance:      {total_maintenance * 12:>15,.0f} RUB")
            print(f"    Total Fixed Costs:          {fixed_costs_annual:>15,.0f} RUB")
            print(f"  Assumed Margin Ratio:                        30.0%")
            print(f"  Break-Even Point:             {break_even_point['break_even_point']:>15,.0f} RUB")

            high_effective_roi_department = self._find_high_effective_roi_department()
            
            print(f"\nHigh Effective ROI Departments (above average):")
            avg_roi = self.roi_results['general_roi']
            print(f"  Company Average ROI: {avg_roi:.2f}%")
            print(f"\n  Departments exceeding average:")
            dept_roi_sorted = high_effective_roi_department.sort_values(ascending=False)
            count = 0
            for dept_name, roi_value in dept_roi_sorted.items():
                if roi_value > avg_roi and count < 10:
                    print(f"    {dept_name:40s} {roi_value:>8.2f}%")
                    count += 1
            
            print(f"\nRECOMMENDATIONS:")
            print(f"• Increase investment in top 3 high-ROI departments")
            print(f"• Develop support programs for underperforming departments")
            print(f"• Set quarterly ROI targets for all departments")
            print(f"• Monitor break-even point quarterly to track profitability")

            # Compile results
            analysis_results = {
                "break_even_point": break_even_point,
                "high_effective_roi_department": high_effective_roi_department
            }

            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("Financial Planning"))

            return analysis_results

        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("Financial Planning", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _calculate_break_even_point(self):
        """
        @brief Calculate the break-even point for the company
        Uses financial data from the company overview DataFrame

        @return: Dictionary with break-even point details
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("break-even point"))

        total_salary_fund_month = self.employees_df['work_info.salary'].sum()
        total_maintenance_cost_month = self.equipment_df['operational_info.maintenance_cost_per_month'].sum()

        fixed_costs_annual = (total_salary_fund_month + total_maintenance_cost_month) * 12

        margin_ratio = 0.30

        break_even_point = fixed_costs_annual / margin_ratio if margin_ratio > 0 else 0

        self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("break-even point"))
        return {"break_even_point": break_even_point}
    
    def _find_high_effective_roi_department(self):
        """
        @brief Find the department with the highest effective ROI
        Uses ROI results to determine the department with the highest effective ROI

        @return: Dictionary with department name and effective ROI
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("high effective ROI department"))

        department_roi = self.roi_results['department_roi']
        average_roi = department_roi.mean()
        high_roi_departments = department_roi[department_roi > average_roi]
        
        self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("high effective ROI department"))

        return department_roi