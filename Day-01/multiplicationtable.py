''' Create the multiplication table of a given number N and return the table as an array.'''

class Solution:
    def getTable(self,N):
        # code here
        lis=[]
        for i in range(1,11):
            lis.append(N*i)
            
        return lis
