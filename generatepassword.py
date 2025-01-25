import collections 
import secrets

def get_passwords_from_words(numberofwords,):
    with open('words.txt','r') as file:
        allwords=file.readlines()
        wordstoreturn=[(secrets.choice(allwords)).strip() for _ in range(numberofwords)]
        return ' '.join(wordstoreturn) 
    
print((get_passwords_from_words(5)))