#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


# In[38]:


corona_dataset_csv = pd.read_csv("C:/Users/hp/OneDrive/Desktop/covid19_Confirmed_dataset.csv")
corona_dataset_csv


# In[40]:


corona_dataset_csv.drop(["Lat", "Long"],axis=1,inplace=True)


# In[41]:


corona_dataset_aggregate = corona_dataset_csv.groupby("Country/Region").sum()


# In[42]:


corona_dataset_csv


# In[43]:


corona_dataset_aggregate


# In[44]:


corona_dataset_aggregate.shape


# In[45]:


corona_dataset_aggregate.loc["China"].plot()
corona_dataset_aggregate.loc["Italy"].plot()
corona_dataset_aggregate.loc["France"].plot()
plt.legend()


# In[46]:


corona_dataset_aggregate.loc["China"][:3].plot()


# In[47]:


corona_dataset_aggregate.loc["China"].diff().plot()


# In[48]:


corona_dataset_aggregate.loc["China"].diff().max()


# In[50]:


corona_dataset_aggregate.loc["France"].diff().max()


# In[52]:


countries = list(corona_dataset_aggregate.index)
max_infection_rates = []
for c in countries :
    max_infection_rates.append(corona_dataset_aggregate.loc[c].diff().max())
corona_dataset_aggregate["max_infection_rate"] = max_infection_rates


# In[53]:


corona_dataset_aggregate


# In[54]:


final_data= pd.DataFrame(corona_dataset_aggregate["max_infection_rate"])


# In[55]:


final_data.head(5)


# In[59]:


happiness_report = pd.read_csv("C:/Users/hp/OneDrive/Desktop/worldwide_happiness_report.csv")


# In[60]:


happiness_report.head()


# In[61]:


useless_cols =["Overall rank", "Score", "Generosity", "Perceptions of corruption"]


# In[62]:


happiness_report.drop(useless_cols, axis=1, inplace=True)
happiness_report


# In[64]:


happiness_report.set_index("Country or region", inplace=True)


# In[65]:


happiness_report


# In[66]:


data = final_data.join(happiness_report, how="inner" )


# In[67]:


data


# In[68]:


data.corr()


# In[70]:


x= data["GDP per capita"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))


# In[71]:


sns.regplot(x, np.log(y))


# In[72]:


a= data["Healthy life expectancy"]
y = data["max_infection_rate"]
sns.scatterplot(a,np.log(y))


# In[73]:


sns.regplot(a, np.log(y))

