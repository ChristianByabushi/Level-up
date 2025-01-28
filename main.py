from levelup import Levelup
from savedictionnary import save_dictionnary, load_dictionnary
from alarm import alarm_define 
from datetime import datetime, timedelta
import time
from sendemail import send_email 
from roldice import run_dice 
from generatepassword import get_passwords_from_words  
from mergecsv import mergefiles
if __name__ == '__main__':
    pass
    # dictionnary = {'id': 34, 'name': 'Developper', 'last-name': 'Designer'}
    # save_dictionnary('my-file-dictionnary.txt',dictionnary)
    # data=load_dictionnary('my-file-dictionnary.txt') 
   
    # alarm_define(time.time()+4,print,"Wake up bro it is time!")
    # send_email('thereceiver@gmail.com','TEST MAIL',"Nous sommes entrain de tester les choses")
    # run_dice(6,4,3,2)
    # get_passwords_from_words(5) 
    fieldnames=mergefiles(["firstcsv.csv",  "secondcsv.csv" ], "out.csv")