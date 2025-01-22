import json
import pickle
def save_dictionnary(filepath, dictionnary):
    with open(filepath,'wb') as file:
        file.write(pickle.dumps(dictionnary)) 
        
def load_dictionnary(filepath):
    with open(filepath, 'rb') as file:
        return pickle.load(file)
    