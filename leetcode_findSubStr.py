class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        word_count = {}
        
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        result_indices = []

        for i in range(len(s) - total_length + 1):
            seen = {}
            for j in range(num_words):
                word_index = i + j * word_length
                word = s[word_index:word_index + word_length]
                
                if word not in word_count:
                    break
                
                seen[word] = seen.get(word, 0) + 1
                
                if seen[word] > word_count[word]:
                    break
                
                if j + 1 == num_words:
                    result_indices.append(i)

        return result_indices

solution = Solution()
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
print(solution.findSubstring(s1, words1))  

s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
print(solution.findSubstring(s2, words2))  

s3 = "barfoofoobarthefoobarman"
words3 = ["bar", "foo", "the"]
print(solution.findSubstring(s3, words3))  
