#!/usr/bin/env python
# coding: utf-8

# In[1]:


from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time


# In[2]:


subscription_key="21a177ddce0f47be92fa6549dd73be41"
endpoint= "https://computervisionsagar.cognitiveservices.azure.com/"
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


# In[3]:


remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-python-sdk-samples/master/samples/vision/images/Face/Family1-Dad1.jpg"


# In[4]:


remote_image_url


# In[6]:



print("Detect Faces ")

remote_image_features = ["faces"]

detect_faces_results_remote = computervision_client.analyze_image(remote_image_url, remote_image_features)


print("Faces in the remote image: ")
if (len(detect_faces_results_remote.faces) == 0):
    print("No faces detected.")
else:
    for face in detect_faces_results_remote.faces:
        print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age,face.face_rectangle.left, face.face_rectangle.top,  face.face_rectangle.left + face.face_rectangle.width, face.face_rectangle.top + face.face_rectangle.height))


# In[ ]:




