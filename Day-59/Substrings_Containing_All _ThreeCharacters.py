'''Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1'''

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_cnt={'a':0,'b':0,'c':0}
        n=len(s)
        left=0
        res=0

        for right in range(len(s)):
            dict_cnt[s[right]]+=1
            while(dict_cnt['a'] and dict_cnt['b']  and dict_cnt['c']):
                res+=n-right
                dict_cnt[s[left]]-=1
                left+=1

        return res
        