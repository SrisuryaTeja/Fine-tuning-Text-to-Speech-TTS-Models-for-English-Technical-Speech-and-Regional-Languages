import requests
from bs4 import BeautifulSoup
import csv

urls_list=["https://www.geeksforgeeks.org/api-testing-interview-questions/",
      "https://www.whizlabs.com/blog/nvidia-interview-questions/",
      "https://interviewprep.org/oauth-interview-questions/",
      "https://medium.com/neuralspace/text-to-speech-101-the-ultimate-guide-9a4b10e20fef",
      "https://www.interviewbit.com/rest-api-interview-questions/"]

content=[]

for urls in urls_list:
    response=requests.get(urls)
    soup=BeautifulSoup(response.text,'html.parser')
    content.extend(soup.find_all(['p','h1','h2','h3','h4','h5','h6','blockquote']))

technical_terms=['API','OAuth','REST','CUDA','HTTP','TTS']

technical_terms_lower=[term.lower() for term in technical_terms]

filtered_sentences=[paragraph.get_text().lower() for paragraph in content 
                    if any(term in paragraph.get_text().lower() for term in technical_terms_lower)]

with open('tech_dataset.csv',mode='w',newline='') as file:

    writer=csv.writer(file)
    writer.writerow(['Sentence','Technical_terms'])

    for sentence in filtered_sentences:
        terms=[term for term in technical_terms_lower if term in sentence]
        term_string=', '.join(terms)
        writer.writerow([sentence,term_string])






