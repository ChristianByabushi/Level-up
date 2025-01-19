import math


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

program1 = Levelup()
answers = program1.get_all_primes_nb(121) 
print(answers)
