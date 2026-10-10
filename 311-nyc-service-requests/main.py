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

print(df.info())
print(df.nunique())