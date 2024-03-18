#!/usr/bin/env python
# coding: utf-8

# In[35]:


from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd

# Load the dataset
data_set = pd.read_excel('D:\\Black Coffer\\kolkata_cars.xlsx')
data_set


# In[45]:


#Checking for null values
null_rows = data_set.isnull()
null_rows


# In[46]:


#There are no null values
null_rows.isnull().any()


# In[168]:


#Body type, model, ownerNo, modelYear, fuel type,
data_set["new_car_detail"][0]


# In[ ]:





# In[190]:


#Appending relevant features to new Dataset
new_data_set = {'Model':[], 'Body Type': [], 'Owner No:':[], 'modelYear':[], "Fuel Type":[], "Kms Driven":[]}
 
for x in data_set["new_car_detail"].items():
    dict1 = eval(x[1])  # Convert string to dictionary
    new_data_set['Body Type'].append(dict1['bt'])
    new_data_set['Model'].append(dict1['model'])
    new_data_set['Owner No:'].append(dict1['ownerNo'])
    new_data_set['modelYear'].append(2023-dict1['modelYear'])
    new_data_set["Fuel Type"].append(dict1['ft'])
    new_data_set["Kms Driven"].append(dict1['km'])
print(pd.DataFrame(new_data_set))


# In[188]:


data_set["new_car_overview"][1]


# In[196]:


#Mileage, Features
h=eval(data_set["new_car_feature"][0])
h


# In[205]:


h=eval(data_set["new_car_specs"][0])
h['top'][0]['value']


# In[208]:


#Mileage
new_data_set = {'Model':[], 'Body Type': [], 'Owner No:':[], 'modelYear':[], "Fuel Type":[], "Kms Driven":[], "Mileage":[]}
for x in data_set["new_car_specs"].items():
    dict1 = eval(x[1])  # Convert string to dictionary
    new_data_set["Mileage"].append(dict1['top'][0]['value'])
for x in data_set["new_car_detail"].items():
    dict1 = eval(x[1])  # Convert string to dictionary
    new_data_set['Body Type'].append(dict1['bt'])
    new_data_set['Model'].append(dict1['model'])
    new_data_set['Owner No:'].append(dict1['ownerNo'])
    new_data_set['modelYear'].append(2023-dict1['modelYear'])
    new_data_set["Fuel Type"].append(dict1['ft'])
    new_data_set["Kms Driven"].append(dict1['km'])
print(pd.DataFrame(new_data_set))


# In[ ]:





# In[ ]:




