class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        total = len(words)
        for word in words:
            word = set(word)
            for ch in word:
                if ch not in allowed:
                    total -= 1
                    break
        return total
        