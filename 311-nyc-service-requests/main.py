import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

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

# print(grouped_by_problem)
# A: 
# 1. Illegal Parking            272373
# 2. Noise - Residential        166117
# 3. Noise - Street/Sidewalk    113564
# 4. Blocked Driveway            80485
# 5. UNSANITARY CONDITION        66874

# plot = sns.barplot(x=grouped_by_problem.values[:5], y=grouped_by_problem.index[:5], hue=grouped_by_problem.values[:5])

# plt.xlabel('Number of Requests')
# plt.xlabel('Type of Problem')
# plt.title('What types of problems generate the most requests?')
# plt.tight_layout()
# plt.show()


# Q: Which agencies receive the most requests?
grouped_by_agency = df.groupby('Agency').size().sort_values(ascending=False)

print(grouped_by_agency)
# A:
# 1. NYPD     794057
# 2. HPD      274892
# 3. DSNY     147244
# 4. DOT      120404
# 5. DEP      113016

sns.barplot(x=grouped_by_agency.values[:5], y=grouped_by_agency.index[:5], hue=grouped_by_agency[:5])

plt.xlabel('Number of Requests')
plt.ylabel('Types of Agencies')
plt.title('Which agencies receive the most requests?')
plt.legend(title='# of Requests')
plt.tight_layout()
plt.show()


# Q: How do requests vary by month
df['Month'] = df['Created Date'].dt.month_name()
grouped_by_month = df.groupby('Month').size().sort_values(ascending=False)

# print(grouped_by_month)
# A:
# 1. July         343133
# 2. June         334834
# 3. August       328908
# 4. September    323624


# Q: Which complaint types take longest to resolve
df['Time To Resolve'] = df['Closed Date'] - df['Created Date']
df_time_to_resolve = df[['Problem', 'Time To Resolve', 'City']].sort_values(by='Time To Resolve', ascending=False)

df_time_to_resolve.dropna(inplace=True)

grouped_by_time_to_resolve = df_time_to_resolve.groupby('Problem')['Time To Resolve'].mean().sort_values(ascending=False)

# print(df_time_to_resolve.head())
# print(grouped_by_time_to_resolve)
# A:
# The longest it took to solve a single problem (Overgrown Tree/Branches) was 154 days, 21 hours and 39 seconds in Brooklyn
# 
# Complaint Types that took longest to solve on average:
# 1. For Hire Vehicle Report    111 days 09:26:22.750000
# 2. Calorie Labeling            60 days 00:16:20.333333
# 3. Mobile Food Vendor          60 days 00:14:46.548996
# 4. Tattooing                   60 days 00:14:17.611940
# 5. Non-Residential Heat        59 days 17:53:58.533333


# Q: How do patterns differ geographically
grouped_by_location = df.groupby(['City', 'Problem']).size()

top_3_cities = df['City'].value_counts().head(3).index

# print(grouped_by_location.loc[top_3_cities].sort_values(ascending=False).head(10))
# 1. BROOKLYN         507795
# - Illegal Parking            98342
# - Noise - Residential        52097
# - Blocked Driveway           28580
# 2. BRONX            313676
# - Noise - Residential        40327
# - Illegal Parking            38050
# - Noise - Street/Sidewalk    36150
# 3. NEW YORK         288406
# - Illegal Parking            29973
# - Noise - Street/Sidewalk    27561
# - Noise - Residential        25433
