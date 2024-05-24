''' For a given number N check if it is prime or not. 
A prime number is a number which is only divisible by 1 and itself.   '''


class Solution:
    def isPrime (self, N):
        # code here
        count=0
        if N==1:
            return 0
        for i in range(1,int(sqrt(N))+1):
            if N%i==0:
                if N//i!=i:
                    count+=2
                else:
                    count+=1
        if  count>2:
            return 0
        else:
            return 1
