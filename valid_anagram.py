class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            #return sorted(s)==sorted(t)
            return collections.Counter(s)==collections.Counter(t)
