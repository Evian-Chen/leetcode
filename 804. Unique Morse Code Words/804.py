class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()

        for word in words:
            temp_ans = ""
            for w in word:
                temp_ans += morse[ord(w)-97]
            ans.add(temp_ans)

        return len(ans)
        