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
        forward=backward[::-1]
        return backward[::-1]==forward
        
    def sortwords(self,stringtext):
        listes = sorted(stringtext.lower().split(' '))
        return listes
        
    def checkValueInAlist(self, liste,searchvalue):
        if not type(liste,list):
            return searchvalue==liste
        for element in liste:
            if element == type(liste,list):
                self.checkValueInAlist(element, searchvalue)
            else:
                if searchvalue==element:
                    return True
    
    def findelementsinlists(self, searchedvalue,listes): 
        foundsAnswers=[]
        dimension=1
        while type(listes, list):
            for i in range(len(listes)):
                if searchedvalue==listes[i]:
                    foundsAnswers.append(
                        {'dimension':dimension,
                         'ligne':i
                        }
                    )

    def search_in_depth_list(self, searchlist, searched_value):
        indices=[]
        for index, element in enumerate(searchlist):
            if element==searched_value:
                indices.append([index])
            elif type(element)==list:
                for sub_index in self.search_in_depth_list(element, searched_value):
                    indices.append([index]+sub_index)
        return indices
        
program1 = Levelup()
#all_primes_nb = program1.get_all_primes_nb(121) 
#ispalindrome = program1.ispalindrome("ara$#,'") 
#sorteswords = program1.sortwords("Vous pouvez aracher les ecorces'") 
searchevalueitem=6
list_where_the_value_is_searched = [[45,5,[43,5,[56,5,6],0,4],[34,[4,5,3,6],34,1]]]
indices_where_finding_that_value= program1.search_in_depth_list(list_where_the_value_is_searched,searchevalueitem)
print(indices_where_finding_that_value)
 