'''Consider a sample space S consisting of all perfect squares starting from 1, 4, 9 and so on. 
You are given a number N, you have to output the number of integers less than N in the sample space S.
 '''


 class Solution:
    def countSquares(self, N):
        return math.ceil(math.sqrt(N))-1  #Formula to calculate perfect squares less then N

    