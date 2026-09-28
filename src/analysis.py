import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('covid_19_clean_complete.csv')
print(df.head(10))

print(df.info())

print(df.shape)

df.rename(columns={'Province/State':'State','Country/Region':'Country'},inplace=True)

print(df['Date'].max())

top=df[df['Date']=='2020-07-27']

print(top.head(10))

top.groupby('Country')[['Confirmed','Deaths','Recovered','Active']].sum().reset_index()

confirmed=df.groupby('Date')['Confirmed'].sum().reset_index()
print(confirmed)


plt.figure(figsize=(20,5))
sns.lineplot(data=confirmed,x='Date',y='Confirmed')
plt.xticks(rotation=90)
plt.show()

recovered=df.groupby('Date')['Recovered'].sum().reset_index()
print(recovered)

plt.figure(figsize=(20,5))
sns.lineplot(data=recovered,x='Date',y='Recovered')
plt.xticks(rotation=90)
plt.show()

top_10_recovered=df.groupby('Country')['Recovered'].sum().sort_values(ascending=False).head(10).reset_index()
print(top_10_recovered)

plt.figure(figsize=(20,7))
sns.barplot(data=top_10_recovered,x='Country',y='Recovered')
plt.title('Top 10 Countries with the most Recovered')

top_10_deaths=df.groupby('Country')['Deaths'].sum().sort_values(ascending=False).head(10).reset_index()
print(top_10_deaths)

plt.figure(figsize=(20,7))
sns.barplot(data=top_10_deaths,x='Country',y='Deaths')
plt.title('Top 10 Countries with the Most Deaths Cases')
plt.show()

US=df[df['Country']=='US']
print(US.head(10))

US=US.groupby('Date')[['Confirmed','Deaths','Recovered','Active']].sum().reset_index()
print(US)

India=df[df['Country']=='India']
print(India)

India=India.groupby('Date')[['Confirmed','Deaths','Recovered','Active']].sum().reset_index()
print(India)

#Create the dataset for China
China=df[df['Country']=='China']
print(China)

China=China.groupby('Date')[['Confirmed','Deaths','Recovered','Active']].sum().reset_index()
print(China)

plt.figure(figsize=(20,5))
sns.pointplot(x=US.index,y=US.Recovered,color='Red')
sns.pointplot(x=China.index,y=China.Recovered,color='Blue')
sns.pointplot(x=India.index,y=India.Recovered,color='Green')

plt.xlabel('No of Days',fontsize=20)
plt.ylabel('No of Recovered Cases',fontsize=20)

plt.show()

plt.figure(figsize=(20,5))
sns.pointplot(x=US.index,y=US.Deaths,color='Red')
sns.pointplot(x=China.index,y=China.Deaths,color='Blue')
sns.pointplot(x=India.index,y=India.Deaths,color='Green')

plt.xlabel('No of Days',fontsize=20)
plt.ylabel('No of Recovered Cases',fontsize=20)

plt.show()

df=pd.read_csv('covid_19_clean_complete.csv',parse_dates=['Date'])

print(df.head(10))

print(df.info())

confirmed=df.groupby('Date')['Confirmed'].sum().reset_index()
print(confirmed)

confirmed.columns=['ds','y']
print(confirmed)

from prophet import Prophet

model=Prophet()

model.fit(confirmed)

future=model.make_future_dataframe(periods=7)
forecast=model.predict(future)
forecast

model.plot(forecast)
plt.show()

import plotly
import plotly.express as px

world=df.groupby('Country/Region')[['Confirmed','Deaths','Active','Recovered']].sum().reset_index()
print(world)

figure=px.choropleth(world,locations='Country/Region',locationmode='country names',color='Active',hover_name='Country/Region',range_color=[1,20000],color_continuous_scale='reds',title='Countries with Active Cases')
figure.show()


