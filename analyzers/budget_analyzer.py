"""
@brief Budget analysis module for IT infrastructure
Analyses budget allocation and departmental spending
"""

import pandas as pd
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages

class BudgetAnalyzer(BaseAnalyzer):
    """
    @brief Budget analysis module for IT infrastructure
    Analyzes budget allocation and departmental spending
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize budget analyzer with data source
        Sets up data loading and logger configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "Budget Analysis")
        self.budget_dataframe = None

    def execute_analysis(self):
        """
        @brief Create pandas DataFrame for budget analysis
        Processes budget data from loaded JSON

        @return: Dictionary containing budget analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("budget"))

        try:
            # Print section header
            print("=" * 70)
            print("BUDGET ANALYSIS")
            print("=" * 70)
            
            # Total budget analysis
            total_budget, budget_per_department = self._analyse_budget()
            print(f"\nTotal Budget: {total_budget:,.0f} RUB")
            print(f"\nBudget Distribution by Department (Top 10):")
            top_departments = budget_per_department.nlargest(10, 'budget')
            for idx, row in top_departments.iterrows():
                print(f"  {row['name']:40s} {row['budget']:>12,.0f} RUB")
            print(
                f"\nWhich is {top_departments['budget'].sum() * 100 / total_budget:,.2f}% of total budget")
            # Department with highest budget
            highest_budget_department, lowest_budget_department = self._analyse_department_budget()
            print(f"\nDepartment Budget Efficiency:")
            print(f"  Highest Budget/Employee: {highest_budget_department['name']}")
            print(f"    Budget per Employee: {highest_budget_department['budget_per_employee']:,.0f} RUB")
            print(f"  Lowest Budget/Employee: {lowest_budget_department['name']}")
            print(f"    Budget per Employee: {lowest_budget_department['budget_per_employee']:,.0f} RUB")

            # Analyze budget utilization rate for departments
            budget_utilization = self._analyse_budget_utilization()
            util_df = pd.DataFrame(budget_utilization)
            print(f"\nAverage budget utilization rate across departments: {util_df['financial_metrics.budget_utilization'].mean():,.2f}%")
            print(f"\nBudget Utilization by Department (Top 10):")
            top_util = util_df.nlargest(10, 'financial_metrics.budget_utilization')
            low_util = util_df.nsmallest(3, 'financial_metrics.budget_utilization')
            for idx, row in top_util.iterrows():
                print(f"  {row['name']:40s} {row['financial_metrics.budget_utilization']:>6.1f}%")
            print("\nLowest Budget Utilization Departments:")
            for idx, row in low_util.iterrows():
                print(f"  {row['name']:40s} {row['financial_metrics.budget_utilization']:>6.1f}%")
            # Compile results
            analysis_results = {
                "total_budget": total_budget,
                "budget_per_department": budget_per_department,
                "highest_budget_department": highest_budget_department,
                "lowest_budget_department": lowest_budget_department,
                "budget_utilization": budget_utilization
            }

            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("budget"))

            return analysis_results
        
        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("budget", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _analyse_budget(self):
        """
        @brief Calculate total budget from data
        Sums up all budget allocations

        @return: Total budget amount
        """
        self.logger.info(LogMessages.TOTAL_BUDGET_ANALYSIS_START)

        total_budget = self.departments_df['budget'].sum()
        department_budgets = self.departments_df[['name', 'budget']]

        self.logger.info(LogMessages.ANALYSIS_COMPLETE.format(total_budget))
        return total_budget, department_budgets
    
    def _analyse_department_budget(self):
        """
        @brief Identify department with highest budget allocation

        @return: Dictionary with department name and budget amount
        """
        self.logger.info(LogMessages.ANALYSIS_START)

        employee_counts = self.employees_df.groupby('work_info.department_id').size().reset_index(name='employee_count')
        
        merged_df = pd.merge(self.departments_df, employee_counts, left_on='id', right_on='work_info.department_id')

        merged_df['budget_per_employee'] = merged_df['budget'] / merged_df['employee_count']

        budget_per_employee_sorted = merged_df.sort_values(by='budget_per_employee', ascending=False)

        highest_budget_department = budget_per_employee_sorted.iloc[0]
        lowest_budget_department = budget_per_employee_sorted.iloc[-1]
        self.logger.info(LogMessages.ANALYSIS_COMPLETE.format(
            highest_budget_department['name'], highest_budget_department['budget'],
            lowest_budget_department['name'], lowest_budget_department['budget']
        ))

        return highest_budget_department.to_dict(), lowest_budget_department.to_dict()

    def _analyse_budget_utilization(self):
        """
        @brief Calculate budget utilization rate for each department

        @return: Dictionary with budget utilization rates
        """
        self.logger.info(LogMessages.ANALYSIS_START)

        # Calculate budget utilization rate
        merged_df = pd.merge(self.departments_df, self.kpi_metrics_df, left_on='id', right_on='department_id')

        utilization_rates = merged_df[['name', 'financial_metrics.budget_utilization']].sort_values(by='financial_metrics.budget_utilization', ascending=False)

        self.logger.info(LogMessages.ANALYSIS_COMPLETE)
        return utilization_rates.to_dict()