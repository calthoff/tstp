# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

def find_index(word, word_list):
    for index, item in enumerate(word_list):
        if item == word:
            return index


def upper(word, word_list):
    for index, item in enumerate(word_list):
        if item == word:
            word_list[index] = word_list[index].upper()
    return word_list


def change_letter(word, old_letter, new_letter, word_list):
    for index, item in enumerate(word_list):
        if item == word:
            word_list[index] = \
                word_list[index].replace(old_letter, new_letter)
    return word_list

print(upper('Programming', ['Programming', 'is', 'fun']))
print(change_letter('fun', 'u', '$', ['Programming', 'is', 'fun']))
