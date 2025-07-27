class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1: return True
        if word[0].isupper():
            nWord = word.upper() if word[1].isupper() else word.lower()
            if nWord[1:] != word[1:]:
                return False
            return True
        nWord = word.lower()
        if nWord != word:
            return False
        return True