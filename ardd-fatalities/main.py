import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

df = pd.read_csv('ardd_fatalities.csv')

# Understanding the data
print(df.info())
print(df.nunique())

# Duplicates
number_of_duplicates = df.duplicated().sum()
percent_of_duplicates = np.around((number_of_duplicates / len(df)) * 100, 2)

print(f'Number of duplicates: {number_of_duplicates}')
print(f'Percent of duplicates: {percent_of_duplicates}%')


# Unique values
bus_involvement_unique = df['Bus Involvement'].unique()
rigid_truck_involvement_unique = df['Heavy Rigid Truck Involvement'].unique()
articulated_truck_involvement_unique = df['Articulated Truck Involvement'].unique()

print(f'Bus involvement: {bus_involvement_unique}')
print(f'Rigid Truck involvement: {rigid_truck_involvement_unique}')
print(f'Articulated Truck involvement: {articulated_truck_involvement_unique}')
# 'No', '-9', nan, 'Yes'

road_user_unique = df['Road User'].unique()
gender_unique = df['Gender'].unique()

print(f'Road User: {road_user_unique}')
# 'Driver', 'Passenger', 'Motorcycle rider', 'Pedestrian', 'Pedal cyclist', 'Other/-9', 'Motorcycle pillion passenger', 'Unknown'
print(f'Gender: {gender_unique}')
# 'Female', 'Male', 'U', '-9', 'M ', 'Unspecified'

christmas_unique = df['Christmas Period'].unique()
easter_unique = df['Easter Period'].unique()

print(f'Christmas Period: {christmas_unique}')
print(f'Easter Period: {easter_unique}')
# 'No', 'Yes'

age_group_unique = df['Age Group'].unique()

print(f'Age Group: {age_group_unique}')
# '17_to_25', '26_to_39', '40_to_64', '65_to_74', '-9', '75_or_older', '0_to_16'

# Day of week:
# 'Weekend', 'Weekday'
# Time of Day
# 'Night', 'Day'