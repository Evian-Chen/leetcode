class Solution:
    def countValidWords(self, sentence: str) -> int:
        punctuation = [",", ".", "!"]
        all_s = sentence.split()
        total = len(all_s)
        for s in all_s:
            hy_count = 0
            for i in range(len(s)):
                if s[i].isdigit():  
                    total -= 1
                    break

                if s[i] in punctuation and i != len(s)-1:
                    total -= 1
                    break

                if s[i] == "-":
                    hy_count += 1
                    if i == 0 or i == len(s)-1:
                        total -= 1 
                        break
                    if hy_count != 1:  # more than 1 hyphan
                        total -= 1
                        break
                    if not s[i-1].isalpha() or not s[i+1].isalpha():
                        total -= 1
                        break
        return total
                    