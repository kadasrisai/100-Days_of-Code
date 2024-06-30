''' 
Given weights and values of n items, we need to put these items in a knapsack of capacity w to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item here. 

Example 1:

Input:
n = 3 
w = 50
value[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.000000
Explanation:
Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20=80, so the total value becomes 60+100+80.0=240.0
Thus, total maximum value of item we can have is 240.00 from the given capacity of sack. 
Example 2:

Input:
n = 2
w = 50
value[] = {60,100}
weight[] = {10,20}
Output:
160.000000
Explanation:
Take both the items completely, without breaking.
Total maximum value of item we can have is 160.00 from the given capacity of sack.'''


class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        
        # code here
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        
        max_value = 0.0
        curr = 0
        
        while W > 0 and curr < n:
            item = arr[curr]
            if item.weight <= W:
                W -= item.weight
                max_value += item.value
            else:
                max_value += item.value * (W / item.weight)
                W = 0
            curr += 1
        
        return max_value 

