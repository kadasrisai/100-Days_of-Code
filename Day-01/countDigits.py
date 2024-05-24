''' 
Given a number N. Count the number of digits in N which evenly divide N.
Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.
 
'''

class Solution:
    def evenlyDivides (self, N):
        # code here
        count=0
        temp=N
        
        while temp!=0:
            rem=temp%10
            if rem!=0:
                if N%rem==0:
                    count+=1
            temp=temp//10
            
        return count