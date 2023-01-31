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

def prompt_handling(prompt):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt,
    temperature=0,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
  return response.choices[0]["text"].strip()

def pep_by_name(name, query_list):
    prompt = ''
    for index, query in enumerate(query_list):
        #each new prompt will be inherited from the previous prompt and the new querry
        query_adjusted = response + "/n" + re.sub("XYZ", name, query)  #replace XYZ with real name if query need to mention real name
        
        #callout openai api
        response = prompt_handling(query_adjusted)
        print(index, ':', response)

def pep_by_name_categories(name, category_list):
    for category in category_list:
      query_adjusted = 'Do you know any {1} named {0}?'.format(name, category)
      # print(query_adjusted)
      response = prompt_handling(query_adjusted)
      print(name, "-", category, "\n", response)
    
#init prompt querries


query_list = [] #create querry list to ask multiple question to openai api

sample_names =["Anthony Albanese"
,"Jenny Morrison"
, "Serge Ivo"
, "Robert Chipman"
]
names = sample_names

#PEP categories list

pep_categories =["Senior government officials"
,"Members of political parties"
,"Senior executives in government-owned commercial firms or international organisations"
,"Relatives and close associates to government officials"
]


#ask openai to list all people name XYZ and their background
pep_query_1 = "List all people named XYZ and their family background"

query_list.append(pep_query_1)

#ask openai to judge base on the people information if any of them are political exposed person
pep_query_2 = "Who above can be considered as a political exposed person (PEP)?"
query_list.append(pep_query_2)

pep_query_3 = "If yes, tell me about the person's name and their background"
query_list.append(pep_query_3)
        
# ##################
# querying by pep categories


###############
        

#connect with openai to detect pep
# for name in names:
#     prompt_handling(name, query_list)
#     print('\n')

#detect pep with pep categories
pep_by_name_categories(name = "Jenny Morrison", category_list= pep_categories)


    