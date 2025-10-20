"""
@brief Salary analysis module for Financial department
Analyses salary distribution and employee compensation
"""

import pandas as pd
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages


class SalaryAnalyzer(BaseAnalyzer):
    """
    @brief Salary analysis module for Financial department
    Analyzes budget allocation and departmental spending
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize salary analyzer with data source
        Sets up data loading and logger configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "Salary Analysis")
        self.salary_dataframe = None

    def execute_analysis(self):
        """
        @brief Create pandas DataFrame for salary analysis
        Processes salary data from loaded JSON

        @return: Dictionary containing salary analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("salary"))

        try:
            # Print section header
            print("=" * 70)
            print("SALARY ANALYSIS")
            print("=" * 70)
            
            # Salary distribution analysis
            salary_distribution = self._analyze_salary_distribution()
            print(f"\nSalary Distribution Statistics:")
            for idx, row in salary_distribution.iterrows():
                print(f"  {row['Metric']:15s} {row['Value']:>15,.0f} {"RUB" if row['Metric'] != 'count' else ""}")

            # Salary per department analysis
            salary_per_department = self._analyze_salary_per_department()
            print(f"\nTotal Salary Fund: {sum(salary_per_department.values()):>12,.0f} RUB")
            print(f"\nTotal Salary Fund by Department (Top 10):")
            sorted_depts = sorted(salary_per_department.items(), key=lambda x: x[1], reverse=True)[:10]
            for dept_name, total_salary in sorted_depts:
                print(f"  {dept_name:40s} {total_salary:>12,.0f} RUB")

            # Identify salary outliers
            salary_outliers = self._identify_salary_outliers()
            if isinstance(salary_outliers, list) and len(salary_outliers) == 0:
                print(f"\nSalary Outliers: None identified")
            else:
                print(f"\nSalary Outliers Identified: {len(salary_outliers)} employees")
                print(f"  (Employees with salaries significantly above or below normal range)")

            # Compile results
            analysis_results = {
                "salary_distribution": salary_distribution,
                "salary_per_department": salary_per_department,
                "salary_outliers": salary_outliers,
            }

            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("salary"))

            return analysis_results

        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("salary", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _analyze_salary_distribution(self):
        """
        @brief Analyze salary distribution across all employees
        Calculates average, median, and standard deviation of salaries

        @return: Dictionary with salary statistics
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("salary distribution"))

        salary_distribution = self.employees_df['work_info.salary'].describe()

        self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("salary distribution"))
        salary_distribution_df = salary_distribution.reset_index()
        salary_distribution_df.columns = ['Metric', 'Value']
        return salary_distribution_df

    def _analyze_salary_per_department(self):
        """
        @brief Calculate average salary per department
        Groups employees by department and calculates average salary

        @return: DataFrame with average salary per department
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("salary per department"))
        salary_per_department = self.employees_df.groupby('work_info.department_name')['work_info.salary'].sum()

        self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("salary per department"))

        return salary_per_department.to_dict()
    
    def _identify_salary_outliers(self):
        """
        @brief Identify salary outliers based on IQR method
        Uses Interquartile Range (IQR) to find employees with unusually high or low salaries

        @return: DataFrame with outlier employees
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("salary outliers"))

        Q1 = self.employees_df['work_info.salary'].quantile(0.25)
        Q3 = self.employees_df['work_info.salary'].quantile(0.75)
        IQR = Q3 - Q1

        # Define outlier thresholds
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = self.employees_df[
            (self.employees_df['work_info.salary'] <= lower_bound) |
            (self.employees_df['work_info.salary'] >= upper_bound)
        ]

        self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("salary outliers"))

        if outliers.empty:
            self.logger.info("No salary outliers found")
            return []

        return outliers