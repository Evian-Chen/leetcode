from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned.append("")
        ans = defaultdict(int)
        word = ""
        
        for ch in paragraph:
            if ch.isalpha() and ch != " ":
                word += ch.lower()
            else:
                if word not in banned:
                    print("word: ", word)
                    ans[word] += 1
                word = ""
        ans[word] += 1
        ans = sorted(ans.items(), key = lambda time: time[1], reverse=True)
        return next(iter(ans))[0]