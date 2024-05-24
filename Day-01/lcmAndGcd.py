''' Given two numbers A and B. The task is to find out their LCM and GCD.'''

class Solution:
    
    def lcmAndGcd(self, A , B):
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        def lcm(a,b):
            return (a//gcd(a,b))*b
        gcd1=gcd(A,B)
        lcm1=lcm(A,B)
        return lcm1,gcd1
