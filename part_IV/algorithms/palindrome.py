F YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

def is_palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(is_palindrome("Mother"))
print(is_palindrome("Mom"))
