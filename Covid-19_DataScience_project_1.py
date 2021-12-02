# ******************************Covid 19 Data Science Project 1 using python and python libraies*************************************

# /////we use the 4 python libraries like (numpy, pandas, matplotlib and seaborn)

# ////importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# //////for Data Analysis we importing the covid-19 in itley csv file report
df=pd.read_csv('datasets\\covid19_italy_region.csv')
# print(df)

# ////for checking the first few rows of csv file we use head function
print(df.head())

# ////for checking the below few rows of csv file we use tail function
# print(df.tail())

# ////for checking the columns name we use variable.columns function
# print(df.columns)

# ////for checking all the values of mean, max, min, std we use describe function
# print(df.describe())

# ////to checking the null values we use isnull function in pandas when it shows the false of the fill values and true in the place of non-fill values
# print(df.isnull())
# ////if we count the all non values we use variable.isnull().sum() function
# print(df.isnull().sum())
# ////if we want to show all the nan values as a counted we use variable.isnull().sum().sum()
# print(df.isnull().sum().sum())

# ////notnull is the totally reverse of isnull function
# print(df.notnull())
# print(df.notnull().sum())
# print(df.notnull().sum().sum())

# ////for maximize the figure we use figure function
# plt.figure(figsize=(13,13))

# /////we analysis the data with the use of graph plotting
# ////we use scatterplot in this analysis using seaborn -------we use also matplotlib but now we use seaborn because it is advance as the matplotlib
# sns.scatterplot(x='HospitalizedPatients',y='NewPositiveCases',data=df)
# sns.scatterplot(x='HospitalizedPatients',y='TotalHospitalizedPatients',data=df)
# sns.scatterplot(x='HospitalizedPatients',y='IntensiveCarePatients',data=df)

# /////when we want to comparison the third column than we use hue parameter
# ////and if we want to creat the labels than we use label parameter and also we use legend function otherwise it is not working
# sns.scatterplot(x='HospitalizedPatients',y='IntensiveCarePatients',data=df,hue='TotalPositiveCases')

# //////and if we want to plotting the graph as a line than we use kind parameter
# sns.relplot(x='HospitalizedPatients',y='IntensiveCarePatients',data=df,kind='line')

# ////relplot is the short name of the scatterplot
# sns.relplot(x='HospitalizedPatients',y='IntensiveCarePatients',data=df)

# //////and if we want to show the graph as a category wise in the color than we use catplot function
sns.catplot(x='HomeConfinement',y='Deaths',data=df)

# /////if we want to show all the columns by all columns one by one plotting graph in one figure than we use pairplot function using seaborn library
# sns.pairplot(data=df)

# ////for creating the title and xlabal and y label than we use following these function
# plt.title('Covid-19 Data Analysis')
# plt.xlabel('X-axis values')
# plt.ylabel('Y-axis values')



plt.show()


