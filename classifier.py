# -*- coding: utf-8 -*-
"""
Spyder Editor

HuyPham - AML CLOUD

PEP classification"
"""


import os
import openai
import re

#provide api_key
openai.api_key = "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"


"""
API connectionn template

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= insert_prompt_here,
  temperature=0,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
  )
"""

def prompt_handling(name, query_list):
    prompt = ''
    for query in query_list:
        #each new prompt will be inherited from the previous prompt and the new querry
        query_adjusted = prompt + "/n" + re.sub("XYZ", name, query)  #replace XYZ with real name if query need to mention real name
        
        #callout openai api
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt= query_adjusted,
          temperature=0,
          max_tokens=100,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
          )
        
        #update prompt based on open ai reponse
        prompt = response.choices[0]["text"].strip()
        print(prompt)
    
    
        
#init prompt querries


query_list = [] #create querry list to ask multiple question to openai api

sample_names = ["Anthony Albanese","Jenny Morrison", "Serge Ivo", "Robert Chipman"]

names = sample_names


#ask openai to list all people name XYZ and their background
pep_queries_1 = "List all people named XYZ and their family background"
query_list.append(pep_queries_1)

#ask openai to judge base on the people information if any of them are political exposed person
pep_queries_2 = "Who above can be considered as a political exposed person (PEP)?"
query_list.append(pep_queries_2)
        
        

#connect with openai to detect pep
for name in names:
    prompt_handling(name, query_list)
    