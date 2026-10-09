import pandas as pd

df = pd.read_csv('service-requests.csv', low_memory=False)

# Understanding the data
print(df.shape)
print(df.info())
print(df.columns)
