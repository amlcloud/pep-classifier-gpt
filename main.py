import os
import openai
import csv
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_with_name(param):
    prompt_builder = "Classify the PEP(Politically Exposed Person) in these persons:\n"+param+"\nIf the person is PEP (Politically Exposed Person):"
    print("1. Classify_with_name")
    prompt_text_davinci_003(prompt_builder)
    return

def classify_with_name_dob(param):
    prompt_builder = "Classify the PEP(Politically Exposed Person) based on person's name and DOB (date of birth) in these persons:\n"+param+"\nIf the person is PEP (Politically Exposed Person):"
    print("\n2. Classify_with_name_dob")
    prompt_text_davinci_003(prompt_builder)
    return 
    
def classify_with_name_dob_country(param):
    prompt_builder = "Classify the PEP(Politically Exposed Person) based on person's name and DOB (date of birth) in these persons:\n"+param+"\nIf the person is PEP (Politically Exposed Person):"
    print("\n3. Classify_with_name_dob_country")
    prompt_text_davinci_003(prompt_builder)
    return

def classify_with_name_list(param):
    prompt_builder = "Classify the PEP(Politically Exposed Person) in these persons:\n"+param+"\nIf the person is PEP (Politically Exposed Person):"
    print("4. Classify_with_name")
    prompt_text_davinci_003(prompt_builder)
    return

def classify_with_name_dob_list(param):
    prompt_builder = "Classify the PEP(Politically Exposed Person) based on person's name and DOB (date of birth) in these persons:\n"+param+"\nIf the person is PEP (Politically Exposed Person):"
    print("\n5. Classify_with_name_dob")
    prompt_text_davinci_003(prompt_builder)
    return 
    
def classify_with_name_dob_country_list(param):
    prompt_builder = "Classify the PEP(Politically Exposed Person) based on person's name and DOB (date of birth) in these persons:\n"+param+"\nIf the person is PEP (Politically Exposed Person):"
    print("\n6. Classify_with_name_dob_country")
    prompt_text_davinci_003(prompt_builder)
    return

def classify_with_name_dob_country_list(param):
    prompt_builder = "Classify the PEP(Politically Exposed Person) based on person's name and DOB (date of birth) in these persons:\n"+param+"\nIf the person is PEP (Politically Exposed Person):"
    print("\n6. Classify_with_name_dob_country")
    prompt_text_davinci_003(prompt_builder)
    return

def get_snippet(param):
    prompt_builder = "Q: Who is "+param+"?\nA:"
    print("\n7. Get_snippet")
    prompt_text_davinci_003(prompt_builder, 0, 100, 1, 0.0, 0.0, ["\n"])
    return

def prompt_text_davinci_003(prompt,temperature=0, max_tokens=60, top_p=1.0, frequency_penalty=0.5, presence_penalty=0.0, stop=None):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop = stop
    )

    currResponse = response['choices'][0]['text']
    
    print(currResponse)

if __name__ == '__main__':
    print("If the person is PEP (Politically Exposed Person):\n")
    classify_with_name("Scott Morrison")
    classify_with_name_dob("Scott Morrison, 13 May 1968")
    classify_with_name_dob_country("Scott Morrison, 13 May 1968, Australia")

    print("\n--------------------\n")

    classify_with_name("Nandin-Erdene Batsaikhan")
    classify_with_name_dob("Nandin-Erdene Batsaikhan, 7 September 1960")
    classify_with_name_dob_country("Nandin-Erdene Batsaikhan, 7 September 1960, Mongolia")

    print("\n--------------------\n")

    classify_with_name_list("Scott Morrison\nNandin-Erdene Batsaikhan\nJacinda Ardern\nRobert Chipman\n习近平")
    classify_with_name_dob_list("Scott Morrison, 13 May 1968\nNandin-Erdene Batsaikhan, 7 September 1960\nJacinda Ardern, 26 July 1980\nRobert Chipman,\n习近平, 15 June 1953")
    classify_with_name_dob_country_list("Scott Morrison, 13 May 1968, Australia\nNandin-Erdene Batsaikhan, 7 September 1960, Mongolia\nJacinda Ardern, 26 July 1980, New Zealand\nRobert Chipman, Australia,\n习近平, 15 June 1953, China")

    print("\n--------------------\n")

    print("Who is ..... ? \n")
    get_snippet("Scott Morrison")
    get_snippet("Nandin-Erdene Batsaikhan")