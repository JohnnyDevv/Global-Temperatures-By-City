#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pandas package
import pandas as pd

#import dataset
df = pd.read_csv('GlobalLandTemperaturesByCity.csv', header=0, sep=',')

#print first 5 records
print(df.head())


# In[2]:


#check info of dataset
df.info()


# In[3]:


#check number of null values in each column
df.isna().sum()


# In[4]:


#number of records
df.shape[0]


# In[5]:


#delete records with null values
df.dropna(axis=0, inplace=True)


# In[6]:


df.shape[0]
#successfully dropped 364,130 records of null data


# In[7]:


#rename 'dt' column to 'Date'
df.rename(columns={'dt':'Date'}, inplace=True)
df.head()


# In[8]:


df.info()


# In[14]:


# change datatype of 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])
df.info()


# In[23]:


df.head()


# In[ ]:


#export cleaned and modified data to CSV file
df.to_csv(r'C:\Users\John Uzoma\Documents\DBS_MASTERS\miscellaneous\data_science\analytic_projects\earth_surface_temperature\cleaned_GlobalLandTemperaturesByCity.csv', index=False)


# In[ ]:




