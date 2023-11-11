#!/usr/bin/env python
# coding: utf-8

# # **Project Name: Diwali sales Analysis**

# In[1]:


#importing libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv('Diwali Sales Data.csv',encoding='unicode_escape')
#to avoid the encoding error


# In[3]:


df.shape
#to get the number of rows and number of columns


# In[4]:


df.head()
#to display first 5 rows


# In[5]:


df.info()
# to get descripitive information about the data frame.


# In[6]:


#drop unrelated/blank columns
df.drop(['Status','unnamed1'],axis=1,inplace=True)
#we use (axis=1) when we are travelling through the columns & (axis=0) when we are travelling through the rows.
#we used (inplace=true) for the confirmation of the changes.


# In[7]:


df.info()
#we deleted the status and unnamed1 columns.


# In[8]:


pd.isnull(df)
#it gives true or false for null values.


# In[9]:


pd.isnull(df).sum()
#to calculate the number of null values.


# In[10]:


#to drop null values
df.dropna(inplace=True)


# In[11]:


df.shape


# In[12]:


df.columns
#to display all columns in dataframe.


# In[13]:


#to get the idea of descriptive statistics(eg. mean ,median,standard deviation)
df.describe()


# In[14]:


#use describe for specific columns
df[['Age','Orders','Amount']].describe()


# ***Exploratory Data Analysis***

# #Gender

# In[15]:


df.columns


# In[16]:


#to display the bargarph of genders.
ax=sns.countplot(x='Gender',data=df)

#to get the actual values of each gender.
for bars in ax.containers:
    ax.bar_label(bars)


# In[17]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
#here we grouped the genders and calculated the amount spends by each gender.


# In[18]:


sns.barplot(x='Gender',y='Amount',data=sales_gen)
#this is the bargraph between the genders and the amount spent by them.


# *From above most of the buyers are females and even the purchasing power of females are greate then males*

# #Age

# In[19]:


df.columns


# In[20]:


sns.countplot(data=df,x='Age Group')
#we are getting only Ages but we can not find the genders.


# In[21]:


sns.countplot(data=df,x='Age Group',hue='Gender')
#now we get ages with their genders.


# In[22]:


ax=sns.countplot(data=df,x='Age Group',hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[23]:


sales_age=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
#here we grouped the Ages and calculated the amount spends by each Age.


# In[24]:


sns.barplot(x='Age Group',y='Amount',data=sales_age)
#this is the bargraph between the ages and the amount spent by them.


# *From above graph we can see that most of the buyers are of age group between 26-35 yrs females.*

# #State

# In[25]:


df.columns


# In[26]:


#total number of orders from top 10 states.
sales_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state,x='State',y='Orders')


# In[27]:


#total number of Amount from top 10 states.
sales_state=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state,x='State',y='Amount')


# *From above graphs we can see that unexpecteadly most of the order are from uttar pradesh,maharashtra,karnataka respectively but total sales/amount is from uttar pradesh ,karnataka and then maharashtra.*

# Marital status

# In[28]:


df.columns


# In[29]:


ax=sns.countplot(data=df,x='Marital_Status')
sns.set(rc={'figure.figsize':(5,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[33]:


sales_m=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data=sales_m,x='Marital_Status',y='Amount',hue='Gender')


# *From above graphs we can see that most of the buyers are married (women) and they have high purchasing power.*

# occupation

# In[34]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[35]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# *From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector*

# product categories

# In[37]:


sns.set(rc={'figure.figsize':(25,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[40]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# *From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category*

# product ID

# In[41]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[43]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion:

# *Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category*

# **Thank you!**
