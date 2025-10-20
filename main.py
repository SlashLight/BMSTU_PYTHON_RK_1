"""
@brief Main execution script for Financial Analysis System
Orchestrates all analysis modules and generates comprehensive reports
"""

import os
import sys
import warnings
import pandas as pd

# Suppress pandas warnings for cleaner output
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=pd.errors.SettingWithCopyWarning)

from analyzers.budget_analyzer import BudgetAnalyzer
from analyzers.salary_analyzer import SalaryAnalyzer
from analyzers.roi_analyzer import RoiAnalyzer
from analyzers.cost_optimization_analyzer import CostOptimizationAnalyzer
from analyzers.financial_planning_analyzer import CompanyOverviewAnalyzer
from config.messages import LogMessages, ReportMessages

import pandas as pd

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
            self.company_overview_module = CompanyOverviewAnalyzer(self.json_data_file_path,
                                                                  roi_analysis_results)

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
        budget_results = self.analysis_results_collection['budget']
        salary_results = self.analysis_results_collection['salary']
        roi_results = self.analysis_results_collection['roi']
        cost_results = self.analysis_results_collection['cost']
        planning_results = self.analysis_results_collection['company_overview']

        print(f"\nKEY PERFORMANCE INDICATORS:")
        print(f"• Total Budget: {budget_results['total_budget']:,.0f} RUB")
        print(f"• Highest Budget/Employee Dept: {budget_results['highest_budget_department']['name']}")
        print(f"  Budget per Employee: {budget_results['highest_budget_department']['budget_per_employee']:,.0f} RUB")
        print(f"• Lowest Budget/Employee Dept: {budget_results['lowest_budget_department']['name']}")
        print(f"  Budget per Employee: {budget_results['lowest_budget_department']['budget_per_employee']:,.0f} RUB")
        
        # Salary metrics
        if not salary_results['salary_outliers']:
            print(f"• Salary Outliers Identified: 0 employees")
        else:
            print(f"• Salary Outliers Identified: {len(salary_results['salary_outliers'])} employees")
        
        # ROI metrics
        print(f"• General ROI: {roi_results['general_roi']:.2f}%")
        print(f"• Most Effective ROI Department: {roi_results['effective_roi_department']}")
        print(f"• Least Effective ROI Department: {roi_results['ineffective_roi_department']}")
        print(f"• ROI-Budget Correlation: {roi_results['roi_budget_correlation']:.3f}")
        
        # Cost metrics
        print(f"• Total Equipment Purchase Cost: {cost_results['general_costs']['total_purchase_cost']:,.0f} RUB")
        print(f"• Total Annual Maintenance Cost: {cost_results['general_costs']['total_annual_cost']:,.0f} RUB")
        print(f"• Total Monthly Maintenance Cost: {cost_results['general_costs']['total_monthly_cost']:,.0f} RUB")
        print(f"• Highest Operational Cost Dept: {cost_results['high_operational_cost_departments']['top_spender_department']}")
        print(f"  Monthly Spending: {cost_results['high_operational_cost_departments']['top_spender_amount']:,.0f} RUB")
        
        # Planning metrics
        print(f"• Break-Even Point: {planning_results['break_even_point']['break_even_point']:,.0f} RUB")

        print(f"\nCRITICAL FINDINGS:")
        print(f"1. Budget Allocation: Wide variance in per-employee budget allocation")
        print(f"2. ROI Performance: Correlation of {roi_results['roi_budget_correlation']:.3f} between budget and ROI")
        print(f"3. Cost Concerns: Annual maintenance represents {(cost_results['general_costs']['total_annual_cost'] / cost_results['general_costs']['total_purchase_cost'] * 100):.1f}% of equipment value")
        
        print(f"\nSTRATEGIC RECOMMENDATIONS:")
        print(f"1. Increase investment in high-ROI department: {roi_results['effective_roi_department']}")
        print(f"2. Audit equipment spending in: {cost_results['high_operational_cost_departments']['top_spender_department']}")
        print(f"3. Review budget allocation for departments with low per-employee ratios")
        print(f"4. Optimize maintenance contracts to reduce annual costs")
        if salary_results['salary_outliers']:
            print(f"5. Review salary structure for {len(salary_results['salary_outliers'])} identified outliers")

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