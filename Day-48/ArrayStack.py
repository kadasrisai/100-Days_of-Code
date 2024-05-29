''' Implementation of stack using array '''


''' Stack ADT :
1.len()
2.isEmpty()
3.push()
4.pop()
5.top()'''


class StacksArray:
    def __init__(self):
        self._data=[]

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def push(self,e):
        self._data.append(e)

    def pop(self):
        if self.isempty():
            print('stack is empty')
            return
        return self._data.pop()

    def top(self):
        if self.isempty():
            print('Stack is empty ')
            return
        return self._data[-1]


S = StacksArray()
S.push(5)
S.push(6)
print(S._data)
print('Length : ',len(S))
print(S.pop())
print(S.isempty())
print(S.top())
print(S.pop())
print(S.isempty())

