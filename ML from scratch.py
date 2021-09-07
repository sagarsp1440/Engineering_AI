#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split


# Loading dataset

# In[2]:


wine = pd.read_csv('winequality-white.csv',sep =';')


# In[19]:


wine.head()


# Preprocessing by creating bins followed by labelencoder

# In[4]:


bins = (2, 5,7, 10)
group_names = ['bad','moderate','good']
wine['quality'] = pd.cut(wine['quality'], bins = bins, labels= group_names)


# In[5]:


wine['quality'].unique()


# In[6]:


label_quality = LabelEncoder()


# In[7]:


wine['quality'] = label_quality.fit_transform(wine['quality'])


# In[22]:


wine.head(15)


# In[8]:


wine['quality'].value_counts()


# Creating test and train split

# In[9]:


X = wine.drop('quality', axis =1)
y = wine['quality']


# In[10]:


X_train , X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)


# In[11]:


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#  RandomForestClassifier

# In[12]:



rc = RandomForestClassifier(n_estimators=500)
rc.fit(X_train, y_train)
predictrc = rc.predict(X_test)


# In[13]:


print(confusion_matrix(y_test,predictrc))


# In[14]:


print(accuracy_score(y_test, predictrc))


# DecisionTreeClassifier

# In[20]:


DT=DecisionTreeClassifier(criterion="entropy",max_depth=11)


# In[21]:


DT=DT.fit(X_train,y_train)


# In[22]:


y_predict=DT.predict(X_test)


# In[24]:


print(accuracy_score(y_test,y_predict))
print(confusion_matrix(y_test,y_predict))

