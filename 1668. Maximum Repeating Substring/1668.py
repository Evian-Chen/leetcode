class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        maxi_count = 0
        index = 0
        while sequence.find(word, index) != -1:
            cur_index = index
            while cur_index < len(sequence):
                print(sequence[cur_index : cur_index+len(word)])
                if sequence[cur_index : cur_index+len(word)] != word:
                    break
                else:
                    cur_index += len(word)
                    count += 1
            maxi_count = max(maxi_count, count)
            count = 0
            index += 1
        return maxi_count