def word_frequency(strings):
    word_count ={} # empty dictionary

    for string in strings:
        words = string.lower().split() # split string into words

        for word in words:
            if word in word_count:
                word_count[word]+=1

            else:
                word_count[word]=1

    return word_count
# Example usage
strings = [
    "The quick brown fox",
    "jumps over the lazy dog",
    "The lazy dog jumps over the fence"
]
print(word_frequency(strings))
