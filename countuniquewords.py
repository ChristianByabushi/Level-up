
import re
from collections import Counter
def get_text_from_the_file(pathTextFile):
    try:
        with open(pathTextFile,'r') as file:
            textfound=file.read()
            return textfound
        
    except FileNotFoundError:
        print(f'The file at {pathTextFile} wasn\'t found')
    except IOError:
        print(f'file doesnt work for io processing')
    
def count_uniques_words(words) -> None: 
    answers={} 
    split_pattern ="[^a-zA-Z0-9\-',\+]"
    sanitize_text = re.split(split_pattern,words) 
    
    for word in sanitize_text:
        if answers.get(word,0):
           answers[word] +=1
        else:
            answers[word] = 1 
    return answers 

text= count_uniques_words(get_text_from_the_file('myfiletoopen.text'))
print(text)
