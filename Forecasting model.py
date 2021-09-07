#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


# In[3]:


from keras.models import Sequential


# In[4]:


from keras.layers import Input,Dense,Dropout, LSTM, GRU, SimpleRNN


# In[5]:


from keras.optimizers import Adam


# In[6]:


from keras.utils import plot_model


# In[30]:


dataset = pd.read_csv("C:/Users/sagar/Documents/engg AI/dataset/tv-sales-forecasting/data.csv")
train_x=dataset


# In[45]:


train_x.head()


# In[46]:


dataset.head()


# In[32]:


train_x = train_x.iloc[::-1]


# In[33]:


train_x.head()


# In[34]:


print(train_x)


# In[35]:


plt.figure(figsize =(12,4))


# In[36]:


plt.plot(range(train_x.shape[0]), train_x['Count'], color='blue', label= 'count')
#plt.plot(range(train_x.shape[0]),train_x['High'], color='red',label='high')
plt.xticks(range(0,train_x.shape[0],10),train_x['Date'].iloc[::10],rotation=45)
#plt.xticks(train_x['Date'])
plt.ylabel('count')
plt.legend()
plt.show()


# In[14]:


from sklearn import preprocessing
le=preprocessing.LabelEncoder()
train_x.iloc[:,1]=le.fit_transform(train_x.iloc[:,1].values)


# In[15]:


scaler = MinMaxScaler()


# In[16]:


train_x.iloc[:,1:]=scaler.fit_transform(train_x.iloc[:,1:].values)


# In[43]:


train_size = int(len(dataset) * 0.67)
test_size = len(dataset) - train_size
print(train_size)


# In[41]:


test_size = len(dataset) - train_size
print(test_size)


# In[44]:


dataset


# In[17]:


plt.plot(range(train_x.shape[0]), train_x['Count'], color='blue', label= 'count')
#plt.plot(range(train_x.shape[0]),train_x['Model'], color='red',label='high')
plt.xticks(range(0,train_x.shape[0],10),train_x['Date'].iloc[::10],rotation=45)
#plt.xticks(train_x['Date'])
plt.ylabel('count')
plt.legend()
plt.show()


# In[18]:


win_size=30
x_train=[]
y_train=[]
for i in range(win_size,len(train_x)):
    x_train.append(train_x.iloc[i-win_size:i,1:].values)
    y_train.append(train_x.iloc[i,-1])
x_train,y_train=np.array(x_train),np.array(y_train).reshape(-1,1)
print(x_train.shape)
print(y_train.shape)


# In[19]:


print(x_train)


# In[20]:


reg=Sequential()
print("x=",x_train.shape[1])


# In[21]:


reg.add(SimpleRNN(units=100, input_shape=(x_train.shape[1],x_train.shape[2]),name='simple_RNN'))
reg.add(Dropout(0.5,name = 'drp1'))
reg.add(Dense(units=10,name = 'fc1'))
reg.add(Dropout(0.2,name = 'drp2'))
reg.add(Dense(units=1,name='output'))

adm=Adam(lr=0.0001)
reg.compile(optimizer=adm, loss='mae')
reg.summary()
model=reg.fit(x_train,y_train,epochs=30,batch_size=100,validation_split=0.20)


# In[ ]:





# In[22]:


plt.plot(model.history['loss'], label=['train'])
plt.plot(model.history['val_loss'],label=['test'])
plt.legend()
plt.show()


# In[23]:


pred=reg.predict(x_train)
err=np.mean(np.abs(y_train-pred))
print("MAE error for standard averaging:",err)


# In[24]:


reg=Sequential()
print("x=",x_train.shape[1])
reg.add(LSTM(units=100, input_shape=(x_train.shape[1],x_train.shape[2]),name='LSTM'))
reg.add(Dropout(0.5,name = 'drp1'))
reg.add(Dense(units=10,name = 'fc1'))
reg.add(Dropout(0.2,name = 'drp2'))
reg.add(Dense(units=1,name='fc2'))
adm=Adam(lr=0.0001)
reg.compile(optimizer=adm, loss='mae')
reg.summary()
model=reg.fit(x_train,y_train,epochs=30,batch_size=100,validation_split=0.20)


# In[ ]:





# In[25]:


plt.plot(model.history['loss'], label=['train'])
plt.plot(model.history['val_loss'],label=['test'])
plt.legend()
plt.show()


# In[26]:


pred=reg.predict(x_train)
err=np.mean(np.abs(y_train-pred))
print("MAE error for standard averaging:",err)


# In[27]:


reg=Sequential()
print("x=",x_train.shape[1])
reg.add(GRU(units=100, input_shape=(x_train.shape[1],x_train.shape[2]),name='GRU'))
reg.add(Dropout(0.5,name = 'drp1'))
reg.add(Dense(units=10,name = 'fc1'))
reg.add(Dropout(0.2,name = 'drp2'))
reg.add(Dense(units=1,name='fc2'))
adm=Adam(lr=0.0001)
reg.compile(optimizer=adm, loss='mae')
reg.summary()
model=reg.fit(x_train,y_train,epochs=30,batch_size=100,validation_split=0.20)


# In[28]:


plt.plot(model.history['loss'], label=['train'])
plt.plot(model.history['val_loss'],label=['test'])
plt.legend()
plt.show()


# In[29]:


pred=reg.predict(x_train)
err=np.mean(np.abs(y_train-pred))
print("MAE error for standard averaging:",err)


# In[ ]:





# In[ ]:





# In[ ]:




