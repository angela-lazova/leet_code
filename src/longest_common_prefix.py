"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Solution:
Runtime: 45 ms
Memory: 13.9 MB
"""

def longestCommonPrefix(self, strs: List[str]) -> str:
    smallest_word_lenght = 999999999999999
    smallest_word = ''
    for word in strs:
        if len(word) < smallest_word_lenght:
            smallest_word_lenght = len(word)
            smallest_word = word

    first_word = smallest_word
    for words in strs:
        for idx, letter in enumerate(words):
            if idx > len(first_word) -1:
                break
            elif letter == first_word[idx]:
                continue
            else:
                first_word = first_word[0:idx:]


    return first_word

