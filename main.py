from levelup import Levelup
from savedictionnary import save_dictionnary, load_dictionnary
from alarm import alarm_define 
from datetime import datetime, timedelta
import time
if __name__ == '__main__':
    # dictionnary = {'id': 34, 'name': 'Developper', 'last-name': 'Designer'}
    # save_dictionnary('my-file-dictionnary.txt',dictionnary)
    # data=load_dictionnary('my-file-dictionnary.txt') 
   
    alarm_define(time.time()+4,print,"Wake up bro it is time!")