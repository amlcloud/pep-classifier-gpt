# -*- coding: utf-8 -*-
"""
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
pep_query_1 = "List all people named XYZ and their family background"
query_list.append(pep_query_1)

#ask openai to judge base on the people information if any of them are political exposed person
pep_query_2 = "Who above can be considered as a political exposed person (PEP)?"
query_list.append(pep_query_2)

pep_query_3 = "If yes, tell me about the person's name and their background"
query_list.append(pep_query_3)
        
        

#connect with openai to detect pep
for name in names:
    prompt_handling(name, query_list)
    print('\n')
    
    