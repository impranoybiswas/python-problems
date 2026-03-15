def find_long_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word