import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_csv('service-requests.csv', low_memory=False)

# Data Cleaning
df = df[['Unique Key', 'Created Date', 'Closed Date', 'Agency', 'Agency Name', 'Problem (formerly Complaint Type)', 'Problem Detail (formerly Descriptor)', 'Location Type', 'Incident Address', 'Street Name', 'City', 'Status', 'Due Date', 'Resolution Description', 'Resolution Action Updated Date']]

df['Problem'] = df['Problem (formerly Complaint Type)']
df['Problem Detail'] = df['Problem Detail (formerly Descriptor)']

df.drop(columns=['Problem Detail (formerly Descriptor)', 'Problem (formerly Complaint Type)'], inplace=True)

df['Created Date'] = pd.to_datetime(df['Created Date'], format='%m/%d/%Y %I:%M:%S %p' ,errors='coerce')
df['Closed Date'] = pd.to_datetime(df['Closed Date'], format='%m/%d/%Y %I:%M:%S %p' ,errors='coerce')
df['Resolution Action Updated Date'] = pd.to_datetime(df['Resolution Action Updated Date'], format='%m/%d/%Y %I:%M:%S %p' ,errors='coerce')

df.dropna(subset=[
    'Unique Key',
    'Created Date',
    'Agency',
    'Problem',
    'Status'
], inplace=True)

df.drop_duplicates(inplace=True)


# Analysis

# Q: What types of problems generate the most requests?
grouped_by_problem = df.groupby('Problem').size().sort_values(ascending=False)

print(grouped_by_problem)
# A: 
# 1. Illegal Parking            272373
# 2. Noise - Residential        166117
# 3. Noise - Street/Sidewalk    113564
# 4. Blocked Driveway            80485
# 5. UNSANITARY CONDITION        66874


# Q: Which agencies receive the most requests?
grouped_by_agency = df.groupby('Agency').size().sort_values(ascending=False)

print(grouped_by_agency)
# A:
# 1. NYPD     794057
# 2. HPD      274892
# 3. DSNY     147244
# 4. DOT      120404
# 5. DEP      113016