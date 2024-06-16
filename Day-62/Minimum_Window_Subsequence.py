'''Given strings str1 and str2, find the minimum (contiguous) substring W of str1, so that str2 is a subsequence of W.

If there is no such window in str1 that covers all characters in str2, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.
 

Example 1:

Input: 
str1: geeksforgeeks
str2: eksrg
Output: 
eksforg
Explanation: 
"eksforg" satisfies all required conditions. str2 is its subsequence and it is longest and leftmost among all possible valid substrings of str1.
Example 2:

Input: 
str1: abcdebdde 
str2: bde 
Output:  bcde 
Explanation:  "bcde" is the answer and "deb" is not a smaller window because the elements in the window must occur in order.'''


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n = len(s1)
        m = len(s2)
        mini = float('inf')
        start = -1

        for i in range(n - m + 1):
            if s1[i] != s2[0]:
                continue
            else:
                p = i
                j = 0
                while p < n and j < m:
                    if s1[p] == s2[j]:
                        j += 1
                    p += 1
                p -= 1
                cur = p - i + 1
                if j == m and cur < mini:
                    mini = cur
                    start = i

        if start == -1:
            return ""
        return s1[start:start + mini]
        