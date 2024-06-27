''' Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.

Examples:

Input: n = 6, arr[] = {0900, 0940, 0950, 1100, 1500, 1800}, 
            dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
Output: 3
Explanation: There are three trains during the time 0940 to 1200. So we need minimum 3 platforms.
Input: n = 3, arr[] = {0900, 1235, 1100}, 
            dep[] = {1000, 1240, 1200}
Output: 1
Explanation: All train times are mutually exlusive. So we need only one platform
Input: n = 3, arr[] = {1000, 0935, 1100}, 
            dep[] = {1200, 1240, 1130}
Output: 3
Explanation: All 3 trains have to be their from 11:00 to 11:30 '''

import heapq

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        timings = [(arr[i], dep[i]) for i in range(n)]
        
        # Sort the timings based on the arrival time
        timings.sort(key=lambda x: x[0])
        
        # Min-heap to track the minimum departure time
        min_heap = []
        
        # Initialize the number of platforms needed
        platforms = 0
        
        # Iterate over each train's timing
        for i in range(n):
            a, d = timings[i]
            
            # Remove all trains that have already departed
            while min_heap and a > min_heap[0]:
                heapq.heappop(min_heap)
                
            # Add the current train's departure time to the min-heap
            heapq.heappush(min_heap, d)
            
            # Update the number of platforms needed
            platforms = max(platforms, len(min_heap))
        
        return platforms
        