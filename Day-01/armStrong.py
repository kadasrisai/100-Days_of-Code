''' For a given 3 digit number, find whether it is armstrong number or not. 
An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 
Return "Yes" if it is a armstrong number else return "No".
NOTE: 371 is an Armstrong number since 33 + 73 + 13 = 371 '''


class Solution:
    def armstrongNumber (self, n):
        # code here 
        temp=n
        cubes=0
        
        while temp!=0:
            rem=temp%10
            cubes+=(rem**3)
            temp=temp//10
        
        if cubes==n:
            return 'Yes'
        else:
            return 'No'
