def read_words_starting_with_WA(text):
    words = text.split()
    words_starting_with_WA = []

    for word in words:
        if word.startswith('W') or word.startswith('A'):
            words_starting_with_WA.append(word)

    return words_starting_with_WA


# Test the function
text = "We went for a walk in the woods and saw an amazing waterfall."
result = read_words_starting_with_WA(text)
print(result)
