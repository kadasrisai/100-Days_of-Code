''' You are given N operations and your task is to Implement a Stack in which you can get a minimum element in O(1) time.

Example 1:

Input:
push(2)
push(3)
pop()
getMin()
push(1)
getMin()
Output: 2 1
Explanation: In the first test case for
query 
push(2)  Insert 2 into the stack.
         The stack will be {2}
push(3)  Insert 3 into the stack.
         The stack will be {2 3}
pop()    Remove top element from stack 
         Poped element will be 3 the
         stack will be {2}
getMin() Return the minimum element
         min element will be 2 
push(1)  Insert 1 into the stack.
         The stack will be {2 1}
getMin() Return the minimum element
         min element will be 1'''


class stack:
    def __init__(self):
        self.s=[]
        self.minele = []
        self.top = None

    def push(self,x):
        #CODE HERE
        if self.s == []:
            self.s.append(x)
            self.minele.append(x)
        else:
            self.s.append(x)
            self.minele.append(min(x , self.minele[-1]))

    def pop(self):
        #CODE HERE
        if self.s == []:
            return -1
        else:
            ele = self.s[-1]
            self.s.pop()
            self.minele.pop()
            return ele
        

    def getMin(self):
        #CODE HERE
        if self.minele == []:
            return -1
        else:
            return self.minele[-1]