import math
class Levelup:
    def get_all_primes_nb(self,nb):
        def __init__():
            pass
        if not isinstance(nb,int):
            raise ValueError("THE TYPE ISNT CONVENIENT")
        allprimesnumbers=[]
        
        for number in range(2,nb):
            for factor in range(2,int(math.sqrt(number))+1): 
                if number % factor == 0:
                    break ## we stop the for-loop
            else: 
                allprimesnumbers.append(number)
        return allprimesnumbers
                
program1= Levelup()
answers =program1.get_all_primes_nb(630)
print(answers)
