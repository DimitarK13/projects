import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(palette='Greens_d')

pd.set_option('display.max_columns', None)

c_palette = sns.color_palette('Greens_d', 6)

df = pd.read_csv('ardd_fatalities.csv', low_memory=False)

# Understanding the data
# print(df.info())
# print(df.nunique())

# Duplicates
number_of_duplicates = df.duplicated().sum()
percent_of_duplicates = np.around((number_of_duplicates / len(df)) * 100, 2)

# print(f'Number of duplicates: {number_of_duplicates}')
# print(f'Percent of duplicates: {percent_of_duplicates}%')


# Unique values
bus_involvement_unique = df['Bus Involvement'].unique()
rigid_truck_involvement_unique = df['Heavy Rigid Truck Involvement'].unique()
articulated_truck_involvement_unique = df['Articulated Truck Involvement'].unique()
# print(f'Bus involvement: {bus_involvement_unique}')
# print(f'Rigid Truck involvement: {rigid_truck_involvement_unique}')
# print(f'Articulated Truck involvement: {articulated_truck_involvement_unique}')
# 'No', '-9', nan, 'Yes'

road_user_unique = df['Road User'].unique()
gender_unique = df['Gender'].unique()
# print(f'Road User: {road_user_unique}')
# 'Driver', 'Passenger', 'Motorcycle rider', 'Pedestrian', 'Pedal cyclist', 'Other/-9', 'Motorcycle pillion passenger', 'Unknown'
# print(f'Gender: {gender_unique}')
# 'Female', 'Male', 'U', '-9', 'M ', 'Unspecified'

christmas_unique = df['Christmas Period'].unique()
easter_unique = df['Easter Period'].unique()
# print(f'Christmas Period: {christmas_unique}')
# print(f'Easter Period: {easter_unique}')
# 'No', 'Yes'

age_group_unique = df['Age Group'].unique()
# print(f'Age Group: {age_group_unique}')
# '17_to_25', '26_to_39', '40_to_64', '65_to_74', '-9', '75_or_older', '0_to_16'

# Day of week:
# 'Weekend', 'Weekday'
# Time of Day
# 'Night', 'Day'

crash_type_unique = df['Crash Type'].unique()
# print(crash_type_unique)
# ['Single', 'Multiple', nan]


# Data cleaning
df.drop(columns=['National Remoteness Areas', 'SA4 Name 2021', 'National LGA Name 2021', 'National Road Type', 'Unnamed: 23'], inplace=True)
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Replace invalid values
df['Bus Involvement'] = df['Bus Involvement'].replace({'-9': False, pd.NA: False, 'No': False, 'Yes': True})
df['Heavy Rigid Truck Involvement'] = df['Heavy Rigid Truck Involvement'].replace({'-9': False, pd.NA: False, 'No': False, 'Yes': True})
df['Articulated Truck Involvement'] = df['Articulated Truck Involvement'].replace({'-9': False, pd.NA: False, 'No': False, 'Yes': True})

df['Road User'] = df['Road User'].replace('Other/-9', 'Unknown')
df['Gender'] = df['Gender'].replace({'-9': 'Unspecified', 'M ': 'Unspecified'})
df['Crash Type'] = df['Crash Type'].replace(pd.NA, 'Single')

df.drop(df[df['Age Group'] == '-9'].index, inplace=True)

# Convert types
df['Christmas Period'] = df['Christmas Period'].replace({'No': False, 'Yes': True})
df['Easter Period'] = df['Easter Period'].replace({'No': False, 'Yes': True})

df = df.convert_dtypes()


# Analysis
# Q: How do incidents vary by time of day?
grouped_by_time_of_day = df.groupby('Time of day').size()

# print(grouped_by_time_of_day)
# print(f'{np.around(grouped_by_time_of_day / len(df) * 100, 2)}')
# plt.pie(grouped_by_time_of_day, labels=['Day', 'Night'], colors=[c_palette[0], c_palette[4]], autopct='%.2f%%')
# plt.title('Incidents variation by time of day', fontweight='bold')
# plt.legend(loc='lower left')
# plt.show()


# Q: How do patterns differ between states
grouped_by_state = df.groupby('State').size()
grouped_by_state_and_time_of_day = df.groupby(['State', 'Time of day']).size()
grouped_by_state_and_day_of_week = df.groupby(['State', 'Day of week']).size()

# print(grouped_by_state)
# print(np.around((grouped_by_state / len(df)) * 100, 2))

# print(grouped_by_state_and_time_of_day)
# print(grouped_by_state_and_day_of_week)


# Q: How do incidents vary by gender
grouped_by_gender = df.groupby('Gender').size()

print(grouped_by_gender)
print(np.around((grouped_by_gender / len(df)) * 100, 2))

plt.figure(figsize=(10, 6.5))
plt.pie(grouped_by_gender, labels=['Female', 'Male', 'Unspecified'], colors=[c_palette[2], c_palette[4], c_palette[0]], autopct='%.2f%%')
plt.title('Incidents by gender', fontweight='bold')
plt.legend()
plt.show()


# Q: How do incidents vary by age group
grouped_by_age_group = df.groupby('Age Group').size()

# print(grouped_by_age_group)
# print(np.around((grouped_by_age_group / len(df)) * 100, 2))

grouped_by_age_group_and_crash_type = df.groupby(['Age Group', 'Crash Type']).size()
# print(grouped_by_age_group_and_crash_type)


# Q: Have patterns changed over time
grouped_by_year = df.groupby('Year').size()
bus_incidents_per_year = (
    df[df['Bus Involvement'] == True]
    .groupby('Year')
    .size()
    .reset_index(name='Bus Incidents')
    .sort_values('Year')
)

# print(grouped_by_year)
# print(bus_incidents_per_year)


# Q: How patterns vary by road users
grouped_by_road_users = df.groupby('Road User').size()
road_users_and_crash_type = df.groupby(['Road User', 'Crash Type']).size()

# print(grouped_by_road_users)
# print(np.around((grouped_by_road_users / len(df)) * 100, 2))
# print(road_users_and_crash_type)