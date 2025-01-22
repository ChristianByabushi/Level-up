from levelup import Levelup
from savedictionnary import save_dictionnary, load_dictionnary
if __name__ == '__main__':
    dictionnary = {'id': 34, 'name': 'Developper', 'last-name': 'Designer'}
    # save_dictionnary('my-file-dictionnary.txt',dictionnary)
    data=load_dictionnary('my-file-dictionnary.txt')