#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as np
import os


# In[2]:


#upload data to jupyter
extra2 = pd.read_csv(r'C:\Users\Azra\Documents\Shopee Project\20200530 BestCoder Project\2. Prepared Data\20200530 Pre-Tretiary\ptr-rd1\Extra_material_2.csv')
extra3 = pd.read_csv(r'C:\Users\Azra\Documents\Shopee Project\20200530 BestCoder Project\2. Prepared Data\20200530 Pre-Tretiary\ptr-rd1\Extra_material_3.csv')
extra3 = extra3.rename(columns={'shopid':'shop_id'})


# In[3]:


#check each head of data
#extra2.head()
#extra3.head()


# In[4]:


#delete data that don't have date time in extra3
extra3_new = extra3[pd.notnull(extra3.date_id)]
#checking
extra3_new


# In[5]:


#changing type for date, orderid, itemid in extra3_new
extra3_new['date_id'] = pd.to_datetime(extra3_new['date_id'], format='%d/%m/%Y')
extra3_new['orderid'] = extra3_new['orderid'].astype(int)
extra3_new['itemid'] = extra3_new['itemid'].astype(int)
extra3_new['shop_id'] = extra3_new['shop_id'].astype(int)

#changing type for date, orderid, itemid in extra2
extra2['shop_id'] = extra2['shop_id'].astype(int)
extra3_new.info


# In[6]:


extra2['shop_id'].dtype


# In[7]:


#selecting a range of date in extra_3_new (10-31 May 2019)
extra3_new_1=extra3_new[(extra3_new.date_id>='2019-05-10') & (extra3_new.date_id<='2019-05-31')]
extra3_new_1


# In[8]:


#combining both data into one dataframe
combined=pd.merge(left = extra2,right = extra3_new_1,how='left',left_on='shop_id',right_on='shop_id')


# In[9]:


combined = combined.reset_index()
combined


# In[10]:


#combined[combined['itemid']=='-2115884395']
combined['shop_id'].dtype


# In[11]:


#counting brand again 
combined.brand.value_counts()


# In[12]:


combined[pd.isnull(combined['date_id'])]
#kesimpulan = there are brand that is not selling items in this range of date


# In[13]:


# bikin kolom baru mengenai gross value
combined['gross'] = combined['amount'] *combined['item_price_usd']
combined


# In[14]:


#total gross for every itemid grouped by brand
new =combined.groupby(['brand','itemid']).gross.sum().reset_index()


# In[15]:


#sorted data from highest gross to lowest
fixed_data = new.sort_values(by=['brand','gross'],ascending=False).groupby('brand').head(3)


# In[16]:


fixed_data


# In[17]:


#include all brand in fixed data
##create a series of brand
brands = pd.Series(extra2['brand'])


# In[18]:


##merging fixed data with brands
fixed=pd.merge(left = fixed_data,right = brands,how='outer',left_on='brand',right_on='brand')


# In[19]:


fixed


# In[20]:


#drop duplicates
fixed_1 = fixed.drop_duplicates(subset=['brand','itemid', 'gross'], keep='first')


# In[21]:


fixed_1


# In[22]:


fixed_1.itemid=fixed_1.itemid.fillna(0)
fixed_1.itemid=fixed_1.itemid.astype(int)
fixed_1.itemid=fixed_1.itemid.astype(str)
fixed_1.itemid=fixed_1.itemid.replace('0','N.A')


# In[23]:


fixed_1


# In[24]:


fixed_2=fixed_1.groupby('brand')['itemid'].apply(', '.join).reset_index()
fixed_2['Answers'] = fixed_2['brand'].str.cat(fixed_2['itemid'],sep=", ")


# In[25]:


fixed_2[fixed_2['brand']=='Anker']


# In[26]:


extra3[extra3['orderid']==1332946287]


# In[27]:


fixed_2[fixed_2['brand']=='Colgate']


# In[28]:


jawaban = pd.Series(fixed_2['Answers']).reset_index()


# In[29]:


jawaban


# In[30]:


jawaban.to_csv(r'C:\Users\Azra\Documents\Shopee Project\20200530 BestCoder Project\3. Uploaded Data\jawaban.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




