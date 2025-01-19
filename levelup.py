import math
import re

class Levelup:

    def get_all_primes_nb(self,number):
        if not isinstance(number,int):
           raise ValueError("Integer values only are considered")
        factors=[]
        mydivisor=2
        while mydivisor <= number:
            if number % mydivisor==0:
                factors.append(mydivisor) 
                number = number // mydivisor
            else :
               mydivisor += 1 # I can't jump to a next while its divisor didn't work
                                      # that the principle.
        return factors              

    def ispalindrome(self, stringtext):
        if not isinstance(stringtext, str):
           raise ValueError('only text are accepted')  
        backward= ''.join(re.findall(r'[a-z]+', stringtext.lower())) 
        foward=backward[::-1]
        return backward[::-1]==foward
        
        
        
program1 = Levelup()
#all_primes_nb = program1.get_all_primes_nb(121) 
ispalindrome = program1.ispalindrome("ara$#,'") 
print(ispalindrome)

