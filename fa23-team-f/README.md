# Project Overview
Boston, a city of profound economic and demographic diversity, presents a unique landscape for budget analysis. Renowned for its high economic mobility across various racial and gender groups, highlighting the need for inclusive budgeting that addresses diverse community needs​​ is crucial for Boston. Boston has a dynamic economic environment, further enriched by its robust healthcare sector and significant contributions from world-class universities​​. (footnote: https://www.britannica.com/place/Boston/Economy) Understanding Boston's socio-economic fabric is essential in analyzing how the city allocates its budget, ensuring that it effectively supports and reflects the needs of its diverse population and vibrant economy.

The overall goal of this project is to analyze the budget of the City of Boston. In the analysis, we will try and understand how the budget is spread across various categories like departments and geography and showcase how it has changed over time.
This project is important because it has the potential to have an impact on the lives of millions of people. This data-driven approach not only ensures efficient use of public funds but also engages citizens in the budgetary process, fostering trust in government and promoting informed governance practices.
This is what motivated our team to opt for this project. It will provide transparency and help demand accountability from the budget planners. By analyzing spending patterns across departments, budget categories, geography, and programs, we can make informed decisions, identify disparities, and evaluate program effectiveness.

# BASE  ANALYSIS
Showcase how Boston city budget is distributed across Cabinets, Departments and Geography 
Portray how it has changed over time 
Evaluate city’s financial management 
Providing valuable insights that can help the stakeholders make decisions 
Suggest ideas which can help distribute budget in a way which empowers and helps more boston residents


# Dataset descriptions 

## Dataset 1: FY24 RECOMMENDED CAPITAL BUDGET PLAN
https://data.boston.gov/dataset/capital-budget/resource/c62d666e-27ea-4c03-9cb1-d3a81a1fb641

The provided dataset details Boston’s FY24 Recommended Capital Budget Plan, outlining various infrastructure projects, their statuses, scopes, and budget allocations. Key columns include the department responsible, project name, scope of work, current status, and budget details, such as authorizations, grants, and total budget. For instance, the dataset includes projects like BCYF Security and Technology Upgrades with a total budget of $2,000,000, and BCYF North End Community Center with an $88,000,000 budget, indicating the city's diverse investment in infrastructure developments.
 
Brief descriptions of the columns:
* Department: Indicates the city department managing the project.
* Project Name: The title or name of the specific infrastructure project.
* Scope Of Work: A brief outline of the project's objectives and tasks.
* PM Department: Department overseeing project management.
* Project Status: The current status or phase of the project.
* Neighborhood: The city area or neighborhood where the project is located.
* Authorization Existing/FY/Future: Funds allocated currently, in the fiscal year, and anticipated in the future.
* Grant Existing/FY/Future: Grant funds allocated currently, in the fiscal year, and anticipated future grants.
* GO Expended: The amount of Government Obligation funds already spent.
* Capital Year 0/1/25: Projected capital expenditures for the current, next, and 25 years ahead.
* Grant Year 0/1/25: Projected grant expenditures for the current, next, and 25 years ahead.
* External Funds: Funding from non-city budget sources.
* Total Project Budget: The combined total of all funding sources for the project.
 
 
## Dataset 2: FY24 RECOMMENDED OPERATING BUDGET
https://data.boston.gov/dataset/operating-budget/resource/8f2971f0-7a0d-401d-8376-0289e3b810ba
 
The dataset outlines the FY24 Recommended Operating Budget for the city of Boston, totaling $4.28 billion, a 6.8% increase from FY23. It contains detailed records of projected expenses for various city departments and programs, derived from the City's General Fund, for the fiscal year starting July 1, 2023, and ending June 30, 2024. Each row represents a unique combination of department, program, and expense category, showcasing a clear breakdown of where and how funds are allocated and spent. The data allows for a detailed analysis of the financial planning and allocations across different city departments and services.
 
Brief descriptions of each column in the dataset:
* Cabinet: The top-level organizational unit, often associated with city governance.
* Dept: The specific department within the cabinet responsible for a program or service.
* Program: Individual programs or initiatives managed by the department.
* Expense Category: The type of expense, such as personnel services, contractual services, etc.
* FY21 Actual Expense: The actual expenses incurred during Fiscal Year 2021.
* FY22 Actual Expense: The actual expenses incurred during Fiscal Year 2022.
* FY23 Appropriation: The budget allocated for expenses in Fiscal Year 2023.
* FY24 Recommended: The proposed budget for expenses in Fiscal Year 2024.

## Dataset 3: ​​FY24 ADOPTED REVENUE BUDGET
https://data.boston.gov/dataset/revenue-budget/resource/9c58a0c8-02c3-4712-850b-7b06f16e8fd5

This dataset provides information on the budget adopted for FY24 by a city and how it compares to the budget and actual revenues of previous fiscal years (FY21, FY22, FY23). It includes details of both recurring and non-recurring revenues and breaks them down into different categories and accounts.
 
A brief description of each column in the  dataset:
 
* Revenue Category: Describes the type of revenue, such as Property Tax Levy.
* Account: Specifies the particular account under each revenue category, like Real Estate Taxes, Personal Property Tax, etc. 
* Cabinet: Indicates the higher-level organizational entity or section of the city government overseeing the revenue accounts, in this case, Finance.
* Department: The specific department within the cabinet that is responsible for the account, such as the Assessing Department.
* FY21 Actual: The actual revenue collected under each account during Fiscal Year 2021. 
* FY22 Actual:  - The actual revenue collected under each account during Fiscal Year 2022.
* FY23 Appropriation: The anticipated or budgeted revenue for each account for Fiscal Year 23; it may not be the actual collected amount.
* FY24 Adopted: The adopted or finalized budget for each account for Fiscal Year 24, indicating planned or expected revenues.
 
Each row in the dataset provides detailed information for a specific account, including the actual revenues from past fiscal years, the appropriated budget for FY23, and the adopted budget for FY24, organized by the responsible cabinet and department.

# DATA CLEANING 
We have removed rows that had even 1 column value that was missing or erroneous. 
Changed column names - remove spaces 
Remove extra spaces from values 
Replace #missing with Nulls 

# Graphs and Analysis
Check the deliverable_4.pdf file and Jupyter Notebooks on the fa23-team-f folder to look at the data cleaning and base analysis with the data in its respective folder. The extension is broken down in various notebooks on the extension folder. We also included the slides, deliverables, and scrum reports in their own folders. 

# Conclusion

In conclusion, our comprehensive analysis of the City of Boston's budget, enriched by the extension projects and comparative study with Philadelphia, has provided valuable insights into municipal financial management during challenging times. The datasets from both cities allowed us to delve deeply into how budget allocations and revenue generation strategies adapt in response to economic fluctuations.Our investigation into the impact of revenue on budget allocations revealed a complex relationship between departmental revenue generation and budget adjustments. This understanding is crucial for future fiscal planning, ensuring that investment in city departments is both effective and efficient. The demographic analysis of the budget highlighted the importance of equitable resource distribution, ensuring that all communities within Boston are adequately served. This aspect of our study is particularly significant in promoting fair and inclusive governance.

Comparing Boston’s financial strategies with those of Philadelphia has been instrumental in uncovering best practices and potential improvement areas. This comparative approach provided a broader perspective on urban financial management, offering insights that could be beneficial for both cities in refining their budgeting processes.

The lessons learned from this analysis can guide future budgeting decisions, promoting the efficient use of public funds and the well-being of city residents. The insights gleaned from this project should be seen as a stepping stone towards more informed, responsive, and responsible urban fiscal policies.



