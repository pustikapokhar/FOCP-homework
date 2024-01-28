'''Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line'''
def letters_in_either(word1, word2):
    return sorted(set(word1.lower() + word2.lower()))

def letters_in_both(word1, word2):
    return sorted(set(char.lower() for char in word1 if char.isalpha()) & set(char.lower() for char in word2 if char.isalpha()))

def letters_in_either_not_both(word1, word2):
    return sorted(set(char.lower() for char in word1 if char.isalpha()) ^ set(char.lower() for char in word2 if char.isalpha()))

# Test the functions
word1 = "hello"
word2 = "world"

print("Letters in at least one word:", letters_in_either(word1, word2))
print("Letters in both words:", letters_in_both(word1, word2))
print("Letters in either word, but not in both:", letters_in_either_not_both(word1, word2))
