#!/usr/bin/env python
# coding: utf-8

# In[1]:


from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry

ENDPOINT = "https://customvisionsagar.cognitiveservices.azure.com/"

# Replace with a valid key
training_key = "e5b9e83d45584b2bbadf381643606187"
prediction_key = "42a301d75dab40cebc9a7dce8739941c"
prediction_resource_id = "/subscriptions/708d3daa-5bc6-4e9f-a645-62b9c155d68a/resourceGroups/SIT788-T1-Student21/providers/Microsoft.CognitiveServices/accounts/CustomVisionSagar-Prediction"

publish_iteration_name = "classifydogvscat"

trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)

# Create a new project
print ("Creating project...")
project = trainer.create_project("catvsdogSDK")


# In[2]:


dog_tag = trainer.create_tag(project.id, "dog")
cat_tag = trainer.create_tag(project.id, "cat")


# In[3]:


print("Adding images...")

image_list = []

for image_num in range(1, 20):
    file_name = "dog.{}.jpg".format(image_num)
    with open("C:/Users/sagar/Documents/engg AI/week5/Compressed/dog vs cat/dataset/training_set/dogs/" + file_name, "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[dog_tag.id]))

for image_num in range(1, 11):
    file_name = "cat.{}.jpg".format(image_num)
    with open("C:/Users/sagar/Documents/engg AI/week5/Compressed/dog vs cat/dataset/training_set/cats/" + file_name, "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[cat_tag.id]))

upload_result = trainer.create_images_from_files(project.id, images=image_list)
if not upload_result.is_batch_successful:
    print("Image batch upload failed.")
    for image in upload_result.images:
        print("Image status: ", image.status)
    exit(-1)


# In[4]:


import time

print ("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    time.sleep(1)

# The iteration is now trained. Publish it to the project endpoint
trainer.publish_iteration(project.id, iteration.id, publish_iteration_name, prediction_resource_id)
print ("Done!")


# In[5]:


from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient


# In[6]:


predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)


# In[7]:


with open("C:/Users/sagar/Documents/engg AI/week5/Compressed/dog vs cat/dataset/test_set/dogs/dog.4001.jpg", "rb") as image_contents:
    results = predictor.classify_image(project.id, publish_iteration_name, image_contents.read())


# In[8]:


for prediction in results.predictions:
        print("\t" + prediction.tag_name +": {0:.2f}%".format(prediction.probability * 100))


# In[ ]:




