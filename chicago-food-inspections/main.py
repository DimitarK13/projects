import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv('food-inspections.csv')

# Data Cleaning
df.drop(columns=['AKA Name', 'City', 'State', 'Latitude', 'Longitude', 'Location', 'Historical Wards 2003-2015', 'Zip Codes', 'Community Areas', 'Census Tracts', 'Wards'], inplace=True)

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)


# Understanding Data
# print('----------------------------- INFO --------------------------------------')
print(df.info())
# print('-------------------------------- NUNIQUE -----------------------------------')
# print(df.nunique())


# print('----------------------------- RISK VALUE COUNTS --------------------------------------')
# print(df['Risk'].value_counts())
# print('----------------------------- RESULTS VALUE COUNTS --------------------------------------')
# print(df['Results'].value_counts())


# Analysis
print('----------------------------- ANALYSIS --------------------------------------')

# Q: What percentage of inspections passed/failed?
print('Q: What percentage of inspections passed/failed?')

percentage_passed = (df['Results'] == 'Pass').value_counts()[True] / df['Results'].count()
percentage_passed = np.around(percentage_passed * 100, 2)
percentage_failed = (df['Results'] == 'Fail').value_counts()[True] / df['Results'].count()
percentage_failed = np.around(percentage_failed * 100, 2)

# print(f'Percentage of inspections that passed: {percentage_passed}%')
# print(f'Percentage of inspections that failed: {percentage_failed}%')
# print('')

# plt.pie(df['Results'].value_counts(), labels=['Pass', 'Fail', 'Pass w/ Conditions', 'Other', 'Other', 'Other'], autopct="%.2f%%", startangle=90)


# Q: What types of establishments have the highest failure rate?
# print('Q: What types of establishments have the highest failure rate?')

df['Failed'] = df['Results'] == 'Fail'
facility_analysis = df.groupby('Facility Type').agg(
    Inspections=('Facility Type', 'size'),
    failure_rate=('Failed', 'mean')
)

facility_analysis = facility_analysis[
    facility_analysis['Inspections'] >= 50
]

facility_analysis['failure_rate'] = (np.around(facility_analysis['failure_rate'] * 100, 2))

facility_analysis = facility_analysis.sort_values('failure_rate', ascending=False)

# print(f'{facility_analysis.index[0]} with a failure rate of {facility_analysis['failure_rate'].iloc[0]}%')
# print('')

# plot = sns.catplot(data=facility_analysis.head(3), x='Facility Type', y='failure_rate', hue='Facility Type', kind='bar')
# plot.set_axis_labels('Facility Type', 'Failure Rate', labelpad=10)


# Q: How does failure rate change between low/medium/high risk?
print('Q: How does failure rate change between low/medium/high risk?')

risks_analysis = df.groupby('Risk').agg(
    failure_rate=('Failed', 'mean')
)

risks_analysis['failure_rate'] = np.around(risks_analysis['failure_rate'] * 100, 2)
risks_analysis = risks_analysis.sort_values('failure_rate', ascending=False)

for i in range(3):
    print(f"Within {risks_analysis.index[i]}, failure rate is {risks_analysis['failure_rate'].iloc[i]}%.\n")

plot = sns.catplot(data=risks_analysis, x='Risk', y='failure_rate', hue='Risk', kind='bar')
plot.set_axis_labels('Risk Type', 'Failure Rate', labelpad=10)
plt.show()


# Q: Why failure rate is highest in Risk 3 (Low) category?
# print('Q: Why failure rate is highest in Risk 3 (Low) category?')


# print('Risk 3 (Low):')
# print(df[df['Risk'] == 'Risk 3 (Low)']['Facility Type'].value_counts())

# print('Risk 1 (High):')
# print(df[df['Risk'] == 'Risk 1 (High)']['Facility Type'].value_counts())

# print(df[df['Facility Type'] == 'Mobile Food Dispenser'].groupby('Risk')['Failed'].count())

# print(df[df['Facility Type'] == 'Mobile Food Dispenser']['Failed'].mean() * 100)

# print('CONCLUSION: It appears that the disproportionately high failure rate in "Risk 3" is due to "Mobile Food Dispenser"s being classified as "Risk 3". "Mobile Food Dispenser"s are the food facilities with highest failure rate.')