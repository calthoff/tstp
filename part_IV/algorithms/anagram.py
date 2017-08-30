

def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

print(is_anagram("iceman", "cinema"))
print(is_anagram("leaf", "tree"))
