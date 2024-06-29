''' 
Given a set of N jobs where each jobi has a deadline and profit associated with it.

Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job. Deadline of the job is the time before which job needs to be completed to earn the profit.


Example 1:

Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60
Explanation:
Job1 and Job3 can be done with
maximum profit of 60 (20+40).
Example 2:

Input:
N = 5
Jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
Output:
2 127
Explanation:
2 jobs can be done with
maximum profit of 127 (100+27). '''




class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,arr,n):
        
        # code here
        arr.sort(key=lambda x: x.profit, reverse=True)
        
        # Find the maximum deadline
        maxDeadline = max(job.deadline for job in arr)
        
        # Initialize the array for storing job deadlines
        deadline = [-1] * (maxDeadline + 1)
        
        count = 0
        maxProfit = 0
        
        # Iterate over each job
        for job in arr:
            # Try to schedule the job on or before its deadline
            for k in range(job.deadline, 0, -1):
                if deadline[k] == -1:
                    deadline[k] = job.id
                    count += 1
                    maxProfit += job.profit
                    break
        
        return [count, maxProfit]