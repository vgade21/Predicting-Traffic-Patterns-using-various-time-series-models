# -*- coding: utf-8 -*-
"""
Created on Fri May 19 19:48:14 2023

@author: vamsh
"""
import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data = pandas.read_csv('C:\\Users\\vamsh\\Documents\\Uni\\UChicago\\Spring 2023\\MSCA 31006_IP03 - Time Series Analysis and Forecasting\\Project\\Metro_Interstate_Traffic_Volume.csv')

data.head()

print("Shape of Data:\n", data.shape)

data.dtypes

data.info() # No null value is present in the data.

data.describe()

# Describing the binary or categorical variables
data.describe(include='object')

# Checking date range
print("max date :" +data.date_time.max())
print("min date :" +data.date_time.min()) # data is collected over 6 years

# Plotting frequency of each category in holiday column
plt.figure(figsize = (8,6))
sns.countplot(y='holiday', data = data)
plt.title("Distribution plot for holiday")
plt.show()

# Plotting rain_1h variable
plt.figure(figsize=(6,4))
sns.distplot(data.rain_1h)
plt.ylabel("Count")
plt.title("Distribution plot for rain_1h") # Most times have zero rainfall
plt.show()

#P lotting observations with values less than 1mm rain shows that more than 40000 observations are around 0.
plt.hist(data.rain_1h.loc[data.rain_1h<1])
plt.ylabel("Count")
plt.xlabel("Rainfall in mm less than 1")
plt.title("Distribution plot for rain_1h less than 1mm") 
plt.show()

# Plotting frequency of each category in snow_1h column
plt.hist(data.snow_1h) # that data is again skewed and most of the observations have value close to 0
plt.ylabel("Count")
plt.xlabel("Snowfall in mm")
plt.title("Distribution plot for snow_1h")
plt.show()

# Correlation between different numeric variables. 
# Plot shows some correlation between temp and clouds_all. Best to remove clouds_all.
# No strong correlation between traffic_volume and other variables
sns.heatmap(data.corr(), annot=True)
plt.title("Correlation Heatmap of continuous variables")
plt.show()

# Creating a copy of the data
data_features = data.copy()

# Extracting features from date_time variable
# Monday is 0 and Sunday is 6
data_features['date_time'] = pandas.to_datetime(data_features.date_time)
data_features['weekday'] = data_features.date_time.dt.weekday
data_features['date'] = data_features.date_time.dt.date
data_features['hour'] = data_features.date_time.dt.hour
data_features['month'] = data_features.date_time.dt.month
data_features['year'] = data_features.date_time.dt.year

data_features.head()

# Traffic volume plotted against weekday. Weekends show less traffic volume.
weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
plt.figure(figsize=(8,6))
sns.boxplot(x='weekday', y='traffic_volume', data = data_features)
plt.title("Traffic Volume distribution by Day of Week")
plt.xticks(range(7), weekday_names)
plt.show()

# Plot of Average Traffic Volume per year
df_date_traffic = data_features.groupby('year').aggregate({'traffic_volume':'mean'})
plt.figure(figsize=(8,6))
sns.lineplot(x = df_date_traffic.index, y = df_date_traffic.traffic_volume, data = df_date_traffic)
plt.title("Average Traffic Volume per year")
plt.show()

# Encoding the holidays as TRUE and none Holidays as FALSE since a holiday is sparse compared to no holidays 
def modify_holiday(x):
    if x == 'None':
        return False
    else:
        return True
data_features['holiday'] = data_features['holiday'].map(modify_holiday)

#Traffic volume difference during holiday and non holiday
plt.figure(figsize=(8,6))
sns.barplot(x='holiday', y='traffic_volume', data = data_features)
plt.title("Average Traffic Volume on Holiday vs No Holiday")
plt.show()

# Similary encoding the snow_1h and rain_1h since these events are sparse too 
def modify_snow(x):
    if x == 0:
        return "Not Snowing"
    else:
        return "Snowing"
data_features['snow_1h'] = data_features['snow_1h'].map(modify_snow)

#Traffic volume difference during holiday and non holiday
plt.figure(figsize=(8,6))
sns.barplot(x='snow_1h', y='traffic_volume', data = data_features)
plt.title("Average Traffic Volume when Snowing vs not Snowing")
plt.show()

def modify_rain(x):
    if x == 0:
        return "Not Raining"
    else:
        return "Raining"
data_features['rain_1h'] = data_features['rain_1h'].map(modify_rain)
                                                        
#Traffic volume difference during holiday and non holiday
plt.figure(figsize=(8,6))
sns.barplot(x='rain_1h', y='traffic_volume', data = data_features)
plt.title("Average Traffic Volume when Raining vs not Raining")
plt.show()