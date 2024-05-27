'''155. Min Stack
Medium

13927

866

Add to List

Share
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 '''
 class MinStack(object):

    def __init__(self):
        self.s = []
        
    def push(self, val):
        if len(self.s) > 0:
            lastSmallest = self.s[-1][1]
        else:
            lastSmallest = None
        if lastSmallest == None or lastSmallest > val:
            self.s.append((val,val))
        else:
            self.s.append((val, lastSmallest))

    def pop(self) :
        v = self.s.pop(-1)   

    def top(self):
        return self.s[-1][0]

    def getMin(self):
        return self.s[-1][1]
        