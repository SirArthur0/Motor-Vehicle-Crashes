import pandas as pd
from pandas import read_csv

pd.options.display.max_rows = 10
pd.options.display.max_columns = 20


file_name = 'Motor Vehicle Crash.csv'

df = pd.read_csv(file_name)

# Convert from Military Time to AM/PM format
df['Time AMPM'] = pd.to_datetime(df['Time'], format='%H:%M').dt.strftime('%I:%M %p')
df.drop(columns='Time', inplace=True)
df.rename(columns={'Time AMPM':'Time'}, inplace=True)

# Concat NY to correctly locate County in PBI Map
df['County Name'] = df['County Name'] + ', NY'

# --- Remove comment to check data info  --- #

# See df general info
#print(df.info())

# Checking first rows and columns
print(df.head)

# See df shape
#print(df.shape)

# Sum of null by column
#pd.options.display.max_rows = 18
#print(df.isnull().sum())

# Period range
#print("From:", df['Date'].min(), "To:", df['Date'].max())

# Save df into new csv file 
df.to_csv("M V C.csv", index = False)
