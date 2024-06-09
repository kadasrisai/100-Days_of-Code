''' Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.'''

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # a string to store the final answer string
        answerString = ''
        # a dictionary that stores the frequency of each character
        hashMap = defaultdict(int)
        for i in s:
            hashMap[i] = hashMap[i] + 1
        # sorting the dictionary based on the values in descending order
        sortedHashMap = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        # multiply the char with the frequency
        for char, frequency in sortedHashMap:
            answerString = answerString + char * frequency

        return answerString
        