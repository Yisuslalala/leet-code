def merge_string(word1, word2):
    merged = ''
    max_length = max(len(word1), len(word2))
    print(max_length)
    for i in range(max_length):
        if i < len(word1):
            merged += word1[i]
        if i < len(word2):
            merged += word2[i]

    print(merged)


word1 = 'ab'
word2 = 'pqrs'
merge_string(word1, word2)
