class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # return lambda max(sentence.split(" ")) : sentence in sentences
        max_length = 0
        for sentence in sentences:
            max_length = max(max_length, len(sentence.split(" ")))
        return max_length    