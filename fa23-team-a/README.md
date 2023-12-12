Add your name to the team info page!

At the end of the semester update this README with information on how to run your project. 

# City Budget - Team A

## Overview

The City of Boston annually collects data on its operating and capital budgets to allocate resources for essential services and infrastructure development. The operating budget encompasses day-to-day expenditures supporting vital roles such as teachers, police officers, and firefighters, along with services like housing, recycling, and transportation. On the other hand, the capital budget, funded through various sources including bonds, city funds, and grants, focuses on acquiring or enhancing physical assets and financing associated projects. The current project is dedicated to a comprehensive analysis of budget distribution across different departments, neighborhoods, and aims to discern trends within funded projects. By scrutinizing datasets covering department and category spending, as well as the proposed operating budget for FY24, the analysis delves into the evolution of funding patterns from 2021 to 2024. The investigation includes a breakdown of spending allocation among diverse departments and programs, an assessment of financial disbursements to various locations, and a calculation of per capita expenditure for different programs. 


## Prerequisites

Before you run the project, make sure you have the following prerequisites installed:

- Python
- Required Python libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn

## Setup

1. Clone the repository to your local machine:

    ```bash
    git clone git@github.com:BU-Spark/ds-boston-city-budget.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ds-boston-city-budget
    ```

## Data

To run the project, you need to have a "data" folder with the following CSV files:

- census.csv
- fy24-adopted-operating-budget.csv
- fy24-capital-budget-plan-recommended.csv
- projects_by_location.csv

## Running Jupyter Notebooks

The project consists of several Jupyter Notebooks. You can run these to see information regarding the 
city spending:

1. CapitalBudgetPlan.ipynb: Extended data analysis on FY24 Capital Budget Plan used for neighborhood/location data in base project and extension project
2. Dataset2.ipynb: Initial data analysis on FY24 Capital Budget Plan
3. census.ipynb: Data analysis on demographics of different neighborhoods used for extension project
4. project.ipynb: Data analysis on FY24 Operating Budget used for program, department and budget category data as well as trends from 2021-2024 in base project
5. visual.ipynb: Compilation of some visuals used in final report

## Troubleshooting

If you encounter any issues or errors during the setup or execution, please send an email to one of the team members.
