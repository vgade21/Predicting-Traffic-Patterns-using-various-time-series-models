# Predicting-Traffic-Patterns-using-various-time-series-models

The objective of this project is to develop a forecasting model that accurately predicts future traffic volume, enabling better traffic
management and planning.

Data Source:
UCI Machine Learning Repository - “Metro Interstate Traffic Volume Data Set”
(https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume)

Variables Description:
● holiday: Categorical US National holidays plus regional holiday, Minnesota State Fair

● temp: Numeric Average temp in kelvin

● rain_1h: Numeric Amount in mm of rain that occurred in the hour

● snow_1h: Numeric Amount in mm of snow that occurred in the hour

● clouds_all: Numeric Percentage of cloud cover

● weather_main: Categorical Short textual description of the current weather

● weather_description: Categorical Longer textual description of the current weather

● date_time: DateTime Hour of the data collected in local CST time

● traffic_volume: Numeric Hourly I-94 ATR 301 reported westbound traffic volume

Following are the family of time series models evaluated:
1. Naive and Seasonal Naive
2. ARIMA family
3. ARIMAX
4. LSTM
