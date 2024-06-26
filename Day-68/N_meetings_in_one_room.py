''' There is one meeting room in a firm. There are n meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time? Return the maximum number of meetings that can be held in the meeting room.

 

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.


Examples :

Input: n = 6, start[] = {1,3,0,5,8,5}, end[] =  {2,4,6,7,9,9}
Output: 4
Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2),(3, 4), (5,7) and (8,9)
Input: n = 3, start[] = {10, 12, 20}, end[] = {20, 25, 30}
Output: 1
Explanation: Only one meetings can be held with given start and end timings. '''

class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        meet=[meeting(start[i],end[i],i+1) for i in range(n)]
        meet=sorted(meet, key=lambda x: (x.end,x.pos))
        answer=[]
        limit= meet[0].end
        answer.append(meet[0].pos)
        for i in range(1,n):
            if meet[i].start>limit:
                limit=meet[i].end
                answer.append(meet[i].pos)
        return len(answer)
        