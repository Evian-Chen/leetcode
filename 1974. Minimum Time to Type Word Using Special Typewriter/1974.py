class Solution:
    def minTimeToType(self, word: str) -> int:
        total = min(abs(ord('a') - ord(word[0])), 26-abs(ord('a') - ord(word[0])))
        for i in range(1, len(word)):
            dist = abs(ord(word[i])-ord(word[i-1]))
            total += min( dist, 26-dist )
        total += len(word)
        return total