''' Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

 

Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length. '''

class Solution(object):
    def maxNumOfSubstrings(self, st):
        """
        :type s: str
        :rtype: List[str]
        """
        letters = {}
        n = len(st)
        for i,a in enumerate(st):
            if a not in letters:
                letters[a] = [i,None]
        for i in range(n-1,-1,-1):
            a = st[i]
            if letters[a][1] is None:
                letters[a][1] = i
        
        for i,a in enumerate(st):
            for k in letters:
                if k==a:continue
                if letters[k][0]<i<letters[k][1]:
                    letters[k][0] = min(letters[k][0],letters[a][0])
                    letters[k][1] = max(letters[k][1],letters[a][1])
        keys = list(letters.keys())
        keys.sort(key = lambda x:letters[x])
        validints = []
        M = len(keys)
        seen = set([])
        res = []
        validints = list(letters.values())
        validints.sort(key = lambda x:x[1]-x[0])
        for s,e in validints:
            possible = True
            for ps,pe in res:
                if not (s > pe or e < ps):
                    possible = False
                    break
            if possible:
                res.append([s,e])
        return [st[a:b+1] for a,b in res]
