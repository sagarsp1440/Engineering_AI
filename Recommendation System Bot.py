#!/usr/bin/env python
# coding: utf-8

# In[1]:


from telegram.ext import Updater
from telegram.ext import CommandHandler
from  telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import MessageHandler, Filters
import requests
import json
import urllib
from sklearn import preprocessing
import pandas as pd


# In[2]:


#My token---------------------------
updater=Updater("1098370882:AAGzikwhEg19iH48siCKWC33-O0crdFrtOI")

# URL for the web service
scoring_uri = 'https://ussouthcentral.services.azureml.net/workspaces/66cb815fce7440669590ac04c18a3e59/services/c2d46cc95e6f4e2a9282141c9e1ad5cd/execute?api-version=2.0&details=true'
# If the service is authenticated, set the key or token
key = 'o3EJnrfJu7bTb8hPWUHm3DtmligbFFLMR7VUoOlyWD2CaD5XmvLbCRIbS3xjJ89xiQ+OOQyTr5dcY73ElX78eA=='


# In[3]:


def start(bot , update):
    
    
    chat_id=update.message.chat_id
    
      

    global status
    status=0
    global question_id
    question_id=0
    global answer_id
    answer_id=0
    
    global responses
    responses=[]
    
    nextquestion(chat_id,bot)


# In[4]:


def contQuestions(bot,update):
    
    chat_id=update.message.chat_id
    text=update.message.text
    
   
    global status
    global answer_id
    global question_id
    print('contQuestions')
    print('status:',status,'question_id:',question_id,'answer_id:',answer_id)

    if answer_id == 0:
        answer_id=answer_id+1
        status=status+1 
        nextquestion(chat_id,bot)
        #updater.dispatcher.remove_handler(consQuestion_handler)
        
    elif answer_id == 1:
       
        answer_id=answer_id+1
        status=status+1  
        nextquestion(chat_id,bot)
        #updater.dispatcher.remove_handler(consQuestion_handler)


    elif answer_id == 2:
        answer_id=answer_id+1
        status=status+1  
        nextquestion(chat_id,bot)
        #updater.dispatcher.remove_handler(consQuestion_handler)
        
    elif answer_id == 3:
        answer_id=answer_id+1
        status=status+1  
        nextquestion(chat_id,bot)
        #updater.dispatcher.remove_handler(consQuestion_handler)
        
    elif answer_id == 4:
        answer_id=answer_id+1
        status=status+1 
        nextquestion(chat_id,bot)
        #updater.dispatcher.remove_handler(consQuestion_handler)
    elif answer_id == 5:
        answer_id=answer_id+1
        status=status+1 
        nextquestion(chat_id,bot)
        #updater.dispatcher.remove_handler(consQuestion_handler)
    elif answer_id == 6:
        answer_id=answer_id+1
        status=status+1 
        nextquestion(chat_id,bot)
        #updater.dispatcher.remove_handler(consQuestion_handler)
    elif answer_id == 7:
        answer_id=answer_id+1
        status=status+1 
        nextquestion(chat_id,bot)
        #updater.dispatcher.remove_handler(consQuestion_handler)
    elif answer_id == 8:
        answer_id=answer_id+1
        status=status+1 
        nextquestion(chat_id,bot)
        #updater.dispatcher.remove_handler(consQuestion_handler)
    elif answer_id == 9:
        answer_id=answer_id+1
        status=status+1 
        nextquestion(chat_id,bot)
        #updater.dispatcher.remove_handler(consQuestion_handler)
        
    elif answer_id == 10:
        answer_id=answer_id+1
        status=status+1  
        nextquestion(chat_id,bot)
        #updater.dispatcher.remove_handler(consQuestion_handler) 

        
    elif answer_id == 11:
        answer_id=answer_id+1
        status=status+1 
        nextquestion(chat_id,bot)
        #updater.dispatcher.remove_handler(consQuestion_handler)   

        


# In[5]:


def button_maker(chat_id,bot,text1, keyboard1):
    
    bot.sendChatAction(chat_id, action = 'typing' , timeout=None)
    bot.send_message(chat_id = chat_id ,text = text1 ,reply_markup=InlineKeyboardMarkup(keyboard1))
    global question_id
    question_id=question_id+1
    


# In[6]:


def messager(chat_id,bot,text1):
   
    print("messager")
    # the below function is explained in this link : https://python-telegram-bot.readthedocs.io/en/stable/telegram.bot.html#telegram.Bot.send_chat_action
    bot.sendChatAction(chat_id, action = 'typing' , timeout=None)
    bot.send_message(chat_id = chat_id ,text = text1)
    global question_id
    question_id=question_id+1
    
   


# In[7]:


def myCallbacks(bot,update):
    
    query=update.callback_query
    data = query.data
    chat_id = query.message.chat_id
    message_id=query.message.message_id
    #userData= update.effective_user

   
    
    global status
    global question_id    
    global answer_id
    
    print('callback')
    print('status:',status,'question_id:',question_id,'answer_id:',answer_id)
#---------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------           
    if status==1:  
        if answer_id==1: 
            answer_id=answer_id+1
            status=status+1     
            nextquestion(chat_id,bot)
            
#---------------------------------------------------------------------------------------------------------------           
    elif status==3:
        if answer_id==3: 
            answer_id=answer_id+1
            status=status+1           
            nextquestion(chat_id,bot)
#---------------------------------------------------------------------------------------------------------------  
    elif status==5:
    
        if answer_id==5:
            answer_id=answer_id+1
            status=status+1
           
                
            nextquestion(chat_id,bot)
#---------------------------------------------------------------------------------------------------------------  
    elif status==6:
       
        if answer_id==6: 
            answer_id=answer_id+1
            status=status+1
            nextquestion(chat_id,bot)
#---------------------------------------------------------------------------------------------------------------  
    elif status==7:
   
        if answer_id==7: 
            
            answer_id=answer_id+1
            status=status+1
            nextquestion(chat_id,bot)
#---------------------------------------------------------------------------------------------------------------  
    elif status==8:
           
        if answer_id==8: 
            
            answer_id=answer_id+1
            status=status+1              
            nextquestion(chat_id,bot)
#---------------------------------------------------------------------------------------------------------------  
    elif status==9:

        if answer_id==9: 
           
            answer_id=answer_id+1
            status=status+1
            nextquestion(chat_id,bot)      
#---------------------------------------------------------------------------------------------------------------           
    elif status==10:
        if answer_id==13:
            
            answer_id=answer_id+1
            status=status+1
            #end(chat_id,bot)
            updater.dispatcher.remove_handler(myCallbacks)
            updater.dispatcher.remove_handler(consQuestion_handler)
            
#---------------------------------------------------------------------------------------------------------------           
    


# In[8]:


def nextquestion(chat_id,bot):
    #import pdb; pdb.set_trace()
   
   
    
    global status
    global question_id    
    global answer_id
    print('nextquestion')
    print('status:',status,'question_id:',question_id,'answer_id:',answer_id)
#---------------------------------------------------------------------------------------------------------------    
    if status==0:
        if question_id==0:
            text ="Are you 18 and above?"
            messager(chat_id,bot,text)        
#---------------------------------------------------------------------------------------------------------------           
    elif status==1:
        
        if question_id==1:
            text = "Choose fixed acidity value in range 5-8:"
            
            messager(chat_id,bot,text)      
                
        
#---------------------------------------------------------------------------------------------------------------           
    elif status==2:
        if question_id==2:
            text = "Choose volatile acidity value in range 0.1-0.5:"   
            messager(chat_id,bot,text)                  
#---------------------------------------------------------------------------------------------------------------           
    elif status==3:
        if question_id==3:
            text = "Choose citric acidity value in range 0.2-0.8:"         
            
            messager(chat_id,bot,text)  
          
       
 #---------------------------------------------------------------------------------------------------------------           
    elif status==4:
        if question_id==4:
            text = "Choose residual sugar value in range 1-25:"   
            messager(chat_id,bot,text)                  
#---------------------------------------------------------------------------------------------------------------  
    elif status==5:
        if question_id==5:    
            text = "Choose chlorides value in range 0.0-0.1:"
            
            messager(chat_id,bot,text)  
        

#---------------------------------------------------------------------------------------------------------------  
    elif status==6:
        if question_id==6:    
            text = "Choose free sulphur dioxide value in range 10-50:"  
          
            messager(chat_id,bot,text)  
        
#---------------------------------------------------------------------------------------------------------------  
    elif status==7:
        if question_id==7: 
            text = "Choose total sulphur dioxide value in range 0-300:"  
            
            messager(chat_id,bot,text)  
     
        
#---------------------------------------------------------------------------------------------------------------  
    elif status==8:
        if question_id==8: 
            text = "Select density in range 0.0 -2.0"  
            
            messager(chat_id,bot,text)
            
        
#---------------------------------------------------------------------------------------------------------------  
    elif status==9:
        if question_id==9: 
            text = "Choose pH in range 2-5"  
            
            messager(chat_id,bot,text)

 #---------------------------------------------------------------------------------------------------------------           
    elif status==10:
        if question_id==10:
            text = "Choose sulphates in range 0.0-1.0"   
            messager(chat_id,bot,text)                
           
 #---------------------------------------------------------------------------------------------------------------           
    elif status==11:
        if question_id==11:
            text = "Choose alchohol percentage in range 5-20"   
            messager(chat_id,bot,text)  
#---------------------------------------------------------------------------------------------------------------           
   


# In[9]:


def transformation(X,ij,z):
    #this function is used to transform dataset to numerical value
    labelencoder = preprocessing.LabelEncoder()
    labelencoder.fit(X[:, ij])
    print(list(labelencoder.classes_))
    print(z)
    res=labelencoder.transform([z])
    print(res)
    #print(res[0])
    return(str(res[0]))


# In[10]:


def end(chat_id,bot):
    print('end')
    bot.sendChatAction(chat_id, action = 'typing' , timeout=None)
    bot.send_message(chat_id = chat_id ,text = "Please wait...")
   
  

    array1=responses
    
    global db
    X=db
    array2=["","","","","","","","","","","","","",""]
    array2[0]=array1[0]
    array2[1]=transformation(X,1,array1[1])
    array2[2]=array1[2]
    array2[3]=transformation(X,3,array1[3])
    array2[4]=array1[4]
    array2[5]=transformation(X,5,array1[5])
    array2[6]=transformation(X,6,array1[6])
    array2[7]=transformation(X,7,array1[7])
    array2[8]=transformation(X,8,array1[8])
    array2[9]=transformation(X,9,array1[9])
    array2[10]=array1[10]
    array2[11]=array1[11]
    array2[12]=array1[12]
    array2[13]=transformation(X,13,array1[13])

    print(array2)
           
   
    data = {

        "Inputs": {

            "input1":
                {
                    "ColumnNames": ["fixedacidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide",
                                    "total sulfur dioxide", "density", "pH", "sulphates", "alchohol"],
                    "Values": [array2,array2,]
                }, },
        "GlobalParameters": {
        }
    }
    print(data)
    body = str.encode(json.dumps(data))
    # body=json.dumps(data)
    # print(data['Inputs']['input1'])

    # print(body)

    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + key)}

    # req = urllib.Request(url, body, headers)
    #help in opening URLs (mostly HTTP) in a complex world 
    req = urllib.request.Request(scoring_uri, body, headers)

    try:

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        response = urllib.request.urlopen(req)
        result = response.read()
        
       
        encoding = response.info().get_content_charset('utf-8')
        JSON_object = json.loads(result.decode(encoding))
        print(JSON_object['Results']['output1']['value']['Values'][0][0])
       
        if JSON_object['Results']['output1']['value']['Values'][0][0] == '1':
            bot.sendChatAction(chat_id, action = 'typing' , timeout=None)
            bot.send_message(chat_id = chat_id ,text = "You have choosen a great wine")
          
           

        elif JSON_object['Results']['output1']['value']['Values'][0][0] == '0':
            bot.sendChatAction(chat_id, action = 'typing' , timeout=None)
            bot.send_message(chat_id = chat_id ,text = "You have choosen a bad wine")
  

    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))



    #command


# In[ ]:


url = r"C:\Users\sagar\Documents\engg AI\dataset\data1.csv"
dataset = pd.read_csv(url)
df = dataset.infer_objects() 
    #print(df.dtypes[0]) 
for ij in range (0,14):
    if df.dtypes[ij]!='int64':
        dataset.iloc[:,ij] = dataset.iloc[:,ij].map(lambda x: x.strip())
            #print(dataset.iloc[:,ij])                                    
array = dataset.values
X = array[:,0:14]
Y = array[:,14]
print(X)
global db
db=X

# listen to get infor from user

command_start= CommandHandler('start',start)
#when the use push the button
callback_Handler=CallbackQueryHandler(myCallbacks)
#when the user enter the text
consQuestion_handler = MessageHandler(Filters.text, contQuestions)
 
#updater
updater.dispatcher.add_handler(command_start)
updater.dispatcher.add_handler(callback_Handler)
updater.dispatcher.add_handler(consQuestion_handler)

print('listening.....')


updater.start_polling()
updater.idle()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




