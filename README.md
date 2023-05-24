# Predicting-Traffic-Patterns-using-various-time-series-models

Data Source:
UCI Machine Learning Repository - “Metro Interstate Traffic Volume Data Set”
(https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume)

The goal of this project is to develop an accurate forecasting model that can predict future traffic volume, leading to improved traffic management and planning. The project utilizes the "Metro Interstate Traffic Volume Data Set" from the UCI Machine Learning Repository as the primary data source.

The dataset contains several variables that describe different aspects related to traffic volume, weather conditions, and date-time information. These variables include:

holiday: Categorical feature indicating US national holidays, regional holidays, and the Minnesota State Fair.

temp: Numeric feature representing the average temperature in Kelvin.

rain_1h: Numeric feature indicating the amount of rain in millimeters that occurred in the hour.

snow_1h: Numeric feature indicating the amount of snow in millimeters that occurred in the hour.

clouds_all: Numeric feature representing the percentage of cloud cover.

weather_main: Categorical feature providing a short textual description of the current weather.

weather_description: Categorical feature providing a longer textual description of the current weather.

date_time: DateTime feature indicating the hour of the data collection in local CST time.

traffic_volume: Numeric feature representing the hourly reported westbound traffic volume on I-94 ATR 301.

To achieve the objective of accurate traffic volume forecasting, the project evaluates different families of time series models. These include:
Naive and Seasonal Naive: Simple models that rely on historical traffic volume data to make predictions.
ARIMA family: Autoregressive Integrated Moving Average models that consider the time series properties and past observations to make forecasts.
ARIMAX: An extension of the ARIMA model that incorporates exogenous variables such as weather conditions to improve the forecasting accuracy.
LSTM: Long Short-Term Memory models, which are a type of recurrent neural network (RNN) specifically designed for sequential data, such as time series.

By evaluating and comparing the performance of these different models, the project aims to identify the most effective approach for accurately predicting future traffic volume. This information can then be utilized for traffic management and planning purposes, allowing for better resource allocation and decision-making to optimize traffic flow and mitigate congestion.
