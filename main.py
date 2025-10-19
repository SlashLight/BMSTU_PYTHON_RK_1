"""
@brief Main execution script for IT Infrastructure Analysis System
Orchestrates all analysis modules and generates comprehensive reports
"""

import os
import sys
from analyzers.budget_analyzer import BudgetAnalyzer
from analyzers.salary_analyzer import SalaryAnalyzer
from analyzers.roi_analyzer import RoiAnalyzer
from analyzers.cost_optimization_analyzer import CostOptimizationAnalyzer
from analyzers.financial_planning_analyzer import CompanyOverviewAnalyzer
from config.messages import LogMessages, ReportMessages

class FinancialAnalysisOrchestrator:
    """
    @brief Main orchestrator for IT infrastructure analysis system
    Coordinates execution of all analysis modules and compiles results
    """
    
    def __init__(self, json_data_file_path):
        """
        @brief Initialize analysis orchestrator with data source
        Sets up all analyzer instances and configuration
        
        @param json_data_file_path: Path to company data JSON file
        """
        self.json_data_file_path = json_data_file_path
        self.analysis_results_collection = {}
        
        # Verify file exists before initializing analyzers
        self._verify_data_file_exists()

        # Initialize analyzer instances
        self.budget_analysis_module = BudgetAnalyzer(json_data_file_path)
        self.salary_analysis_module = SalaryAnalyzer(json_data_file_path)
        self.roi_analysis_module = RoiAnalyzer(json_data_file_path)
        self.cost_analysis_module = CostOptimizationAnalyzer(json_data_file_path)
        self.company_overview_module = CompanyOverviewAnalyzer(json_data_file_path, self.roi_analysis_module.execute_analysis())

    def _verify_data_file_exists(self):
        """
        @brief Verify that the data file exists before analysis
        Provides clear error message if file is not found
        """
        if not os.path.exists(self.json_data_file_path):
            error_message = f"Data file not found: {self.json_data_file_path}"
            print(f"ERROR: {error_message}")
            print("Please ensure the JSON data file exists in the specified path")
            raise FileNotFoundError(error_message)

    def execute_comprehensive_analysis(self):
        """
        @brief Execute complete IT infrastructure analysis
        Runs all analysis modules and compiles comprehensive results

        @return: Dictionary containing all analysis results
        """
        print("INITIATING COMPREHENSIVE IT INFRASTRUCTURE ANALYSIS")
        print("=" * 70)

        try:
            # Execute all analysis modules
            print("\nEXECUTING BUDGET ANALYSIS...")
            budget_analysis_results = self.budget_analysis_module.execute_analysis()
            
            self.analysis_results_collection['budget'] = budget_analysis_results

            print("\nEXECUTING SALARY ANALYSIS...")
            salary_analysis_results = self.salary_analysis_module.execute_analysis()
            self.analysis_results_collection['salary'] = salary_analysis_results

            print("\nEXECUTING ROI ANALYSIS...")
            roi_analysis_results = self.roi_analysis_module.execute_analysis()
            self.analysis_results_collection['roi'] = roi_analysis_results

            print("\nEXECUTING COST ANALYSIS...")
            cost_analysis_results = self.cost_analysis_module.execute_analysis()
            self.analysis_results_collection['cost'] = cost_analysis_results

            print("\nEXECUTING COMPANY OVERVIEW ANALYSIS...")
            company_overview_results = self.company_overview_module.execute_analysis()
            self.analysis_results_collection['company_overview'] = company_overview_results

            # Generate final comprehensive report
            self._generate_comprehensive_summary_report()

            return self.analysis_results_collection

        except Exception as comprehensive_analysis_error:
            print(f"\nCOMPREHENSIVE ANALYSIS FAILED: {str(comprehensive_analysis_error)}")
            raise comprehensive_analysis_error

    def _generate_comprehensive_summary_report(self):
        """
        @brief Generate final comprehensive summary report
        Compiles key findings and recommendations from all analyses
        """
        print("\n" + "=" * 70)
        print("COMPREHENSIVE FINANCIAL ANALYSIS SUMMARY")
        print("=" * 70)

        # Extract key metrics from all analyses
        budget_analysis_results = self.analysis_results_collection['budget']
        salary_analysis_results = self.analysis_results_collection['salary']
        roi_analysis_results = self.analysis_results_collection['roi']
        cost_analysis_results = self.analysis_results_collection['cost']
        company_overview_results = self.analysis_results_collection['company_overview']

        print(f"\nKEY PERFORMANCE INDICATORS:")
        print(f"• Total Budget: {budget_analysis_results['total_budget']} RUB")
        print(f"• Salary Distribution: {salary_analysis_results['salary_distribution']} RUB")
        print(f"• Highest Budget Department: {budget_analysis_results['highest_budget_department']['name']} ({budget_analysis_results['highest_budget_department']['budget']} RUB)")
        print(f"• Lowest Budget Department: {budget_analysis_results['lowest_budget_department']['name']} ({budget_analysis_results['lowest_budget_department']['budget']} RUB)")
        print(f"• Salary Outliers Identified: {salary_analysis_results['salary_outliers']}")
        print(f"• General ROI: {roi_analysis_results['general_roi']}%")
        print(f"• Effective ROI Department: {roi_analysis_results['effective_roi_department']}")
        print(f"• Ineffective ROI Department: {roi_analysis_results['ineffective_roi_department']}")
        print(f"• ROI-Budget Correlation: {roi_analysis_results['roi_budget_correlation']}")
        print(f"• Total monthly maintenance cost: {cost_analysis_results['general_costs']['total_monthly_cost']}")
        print(f"• Total annual maintenance cost: {cost_analysis_results['general_costs']['total_annual_cost']}")
        print(f"• Total monthly maintenance cost: {cost_analysis_results['general_costs']['total_monthly_cost']}")
        print(f"• Total equipment cost: {cost_analysis_results['general_costs']['total_purchase_cost']}")
        print(f"• Top spender department: {cost_analysis_results['high_operational_cost_departments']['top_spender_department']} spends {cost_analysis_results['high_operational_cost_departments']['top_spender_amount']} RUB")
        print("RECOMMENDATIONS")
        print(f"1. Audit {cost_analysis_results['high_operational_cost_departments']['top_spender_department']}")
        print(f"2. Consider cost-saving measures for {cost_analysis_results['most_expensive_equipment']['name']} equipment, which has the highest monthly maintenance cost of {cost_analysis_results['most_expensive_equipment']['operational_info.maintenance_cost_per_month']} RUB/month")
        print(f"\n• Break-even Point: {company_overview_results['break_even_point']['break_even_point']} RUB")
        print(f"RECOMMENDATIONS")
        print(f"• Increase financial investment in High Effective ROI Departments: {company_overview_results['high_effective_roi_department']}")

        print("\n" + "=" * 70)

def main():
    """
    @brief Main execution function for IT Infrastructure Analysis
    Handles command line arguments and orchestrates analysis execution
    """
    # Configuration - update this path to match your JSON file
    company_data_json_file_path = "company.json"  # Changed from company_data_detailed.json

    try:
        # Initialize and execute analysis
        analysis_orchestrator = FinancialAnalysisOrchestrator(company_data_json_file_path)
        comprehensive_analysis_results = analysis_orchestrator.execute_comprehensive_analysis()

        print(f"\nANALYSIS COMPLETED SUCCESSFULLY!")
        print(f"Log files generated in 'logs/' directory")

    except FileNotFoundError as file_error:
        print(f"\nFILE ERROR: {str(file_error)}")
        print("Please check the file path and ensure the JSON file exists")
        sys.exit(1)
    except Exception as main_execution_error:
        print(f"\nCRITICAL ERROR DURING ANALYSIS EXECUTION: {str(main_execution_error)}")
        sys.exit(1)

if __name__ == "__main__":
    main()