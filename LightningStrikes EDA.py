# importing libraries

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt


# Read 2018 lightning strike dataset.
df = pd.read_csv('eda_using_basic_data_functions_in_python_dataset1.csv')


# Look at the first 10 rows.
df.head(10)


# Determine how many rows and columns of data there are
df.shape


# Get more information about the data, including data types 
df.info()

# Convert the date column to datetime
# Converting datetime using the pandas
df['date']= pd.to_datetime(df['date'])


# Calculate the days with the most strikes
# top 10 days of 2018 with the most number of lightning strikes using the `groupby()`, `sum()`, and `sort_values()` functions from pandas.
df.groupby(['date']).sum().sort_values('number_of_strikes', ascending=False).head(10) 


# Extract the month data
# Create a new `month` column
df['month'] = df['date'].dt.month
df.head()


# Calculate the number of strikes per month
# sorting the values by most strikes per month. Use `groupby()`, `sum()` and `sort_values()` from pandas.
df.groupby(['month']).sum().sort_values('number_of_strikes', ascending=False).head(12)


# Convert the month number to text 
# Create a new `month_txt` column.
df['month_txt'] = df['date'].dt.month_name().str.slice(stop=3)
df.head()


# Create a new dataframe
# to plot the total number of strikes per month as a bar graph, we create a new dataframe called `df_by_month`
df_by_month = df.groupby(['month','month_txt']).sum().sort_values('month', ascending=True).head(12).reset_index()
df_by_month


# Making a bar chart
plt.bar(x=df_by_month['month_txt'],height= df_by_month['number_of_strikes'], label="Number of strikes")
plt.plot()

plt.xlabel("Months(2018)")
plt.ylabel("Number of lightning strikes")
plt.title("Number of lightning strikes in 2018 by months")
plt.legend()
plt.show()