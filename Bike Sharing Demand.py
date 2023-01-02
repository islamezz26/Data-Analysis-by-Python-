# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 13:48:51 2023

@author: eslam
"""
#Diabetes Problem

import pandas as pd
import numpy as np
import seaborn as sns

#Knowing Data

df=pd.read_csv('train.csv')
print(df.head())
df.info()
print(df.describe())

#Data_Analysis
##Make Profit Feature

def calculate_profit (x):
    registered_customar= x['registered']
    casual_customar= x['casual']
    registered_price_per_hour = 5 
    casual_price_per_hour = 20                                                                                                        
    texes_percent = .14
    maintenance_per_hour= 1500/(365*24)
    profit_cash = registered_customar*registered_price_per_hour + casual_price_per_hour * casual_customar
    Profit_withTaxes = profit_cash-(profit_cash*texes_percent)
    TotalProfit = Profit_withTaxes- maintenance_per_hour
    return TotalProfit

df['Profit'] = df[['registered', 'casual']].apply(calculate_profit, axis=1)
print(df)

##distrbution rental_bike_count & profit
sns.displot(df['count'], kde = False, color= 'm')
sns.displot(df['Profit'], kde = False, color= 'm')
sns.jointplot (x='Profit',y='count',data= df)

##profit for each day par week
df['datetime']= pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
df['year']= df['datetime'].dt.year
df['month']= df['datetime'].dt.month_name()
df['day par week']= df['datetime'].dt.day_name()
df['hour']= df['datetime'].dt.hour
print(df)
groupbyDay = df.groupby('day par week').describe()[['Profit']].transpose()
print(groupbyDay)

##which season has more registerated & Profit?
groupbySeason = df.groupby('season').describe()[['Profit']].transpose()
print(groupbySeason)

##which weather has more registerated & Profit?
groupbyWeather = df.groupby('weather').describe()[['Profit']].transpose()
print(groupbyWeather)

##Corrilation between all feature and count& profit
cor=df.corr()[['Profit','count']]
print(cor)
sns.heatmap(cor, annot = True)

##count & profit during rush hour 7-9 & 15-17?
def Rush_Hour(hour):
    return 1 if hour in [7,8,9,15,16,17] else 0 
df['RushHour']= df['hour'].apply(Rush_Hour)
print(df)
groupbyRushHour = df.groupby('RushHour').describe()[['Profit']].transpose()
print(groupbyRushHour)

##profit in 2011 & season num 1 & Saturday?
sat=df[(df['season']== 1) & (df['year']== 2011) & (df['day par week']== 'Saturday')]['Profit'].sum()
print(sat)
#Data Visualization

##Numerical Features - univariate
sns.displot(df['temp'], kde= False, color= 'm')
sns.displot(df['humidity'], kde= False, color= 'm')
sns.displot(df['casual'], kde= False, color= 'm')
sns.displot(df['registered'], kde= False, color= 'm')
sns.displot(df['count'], kde= False, color= 'm')
sns.displot(df['Profit'], kde= False, color= 'm')

##Numerical Features - bivariate
sns.jointplot(x= 'temp', y= 'Profit',data= df, color= 'm')
sns.jointplot(x= 'humidity', y= 'Profit',data= df, color= 'm')
sns.jointplot(x= 'casual', y= 'Profit',data= df, color= 'm')
sns.jointplot(x= 'registered', y= 'Profit',data= df, color= 'm')
sns.jointplot(x= 'count', y= 'Profit',data= df, color= 'm')

##Categorical Features - univariate
sns.countplot(x= 'season', data=df, palette= 'viridis')
sns.countplot(x= 'holiday', data=df, palette= 'viridis')
sns.countplot(x= 'workingday', data=df, palette= 'viridis')
sns.countplot(x= 'weather', data=df, palette= 'viridis')
sns.countplot(x= 'atemp', data=df, palette= 'viridis')
sns.countplot(x= 'windspeed', data=df, palette= 'viridis')
sns.countplot(x= 'year', data=df, palette= 'viridis')

##Categorical Features - bivariate
sns.boxplot(x= 'season',y='Profit', data=df, palette= 'viridis')
sns.boxplot(x= 'holiday',y='Profit', data=df, palette= 'viridis')
sns.boxplot(x= 'workingday',y='Profit', data=df, palette= 'viridis')
sns.boxplot(x= 'weather',y='Profit', data=df, palette= 'viridis')
sns.boxplot(x= 'atemp',y='Profit', data=df, palette= 'viridis')
sns.boxplot(x= 'windspeed',y='Profit', data=df, palette= 'viridis')
sns.boxplot(x= 'year',y='Profit', data=df, palette= 'viridis')