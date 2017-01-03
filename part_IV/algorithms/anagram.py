# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

print(is_anagram("iceman", "cinema"))
print(is_anagram("leaf", "tree"))
