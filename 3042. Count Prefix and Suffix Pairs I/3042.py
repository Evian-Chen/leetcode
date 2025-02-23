class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[i]) <= len(words[j]):
                    fix = words[i]
                    if words[j][:len(fix)] == fix and words[j][-len(fix):] == fix:
                        ans += 1
        return ans
        