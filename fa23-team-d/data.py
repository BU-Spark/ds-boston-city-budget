import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('fy24-capital-budget-plan-recommended.csv')
df['Total_Project_Budget'] = df['Total_Project_Budget'].str.replace(',', '')
df['Total_Project_Budget'] = df['Total_Project_Budget'].astype(float)

# Remove "Multiple Neighborhoods" and "Citywide" from the data
df = df[df['Neighborhood'] != 'Multiple Neighborhoods']
df = df[df['Neighborhood'] != 'Citywide']

budget_by_areas = df.groupby('Neighborhood')['Total_Project_Budget'].sum()

# Create a plot
budget_by_areas.plot(kind='bar', title='FY24 Boston Capital Budget Plan by Areas')
plt.ylabel('Total Budget (USD)')
plt.xlabel('Areas')
plt.tight_layout()
plt.gcf().set_size_inches(10, 6)
plt.show()
