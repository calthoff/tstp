def capitalize_item(word, word_list):
    for index, item in enumerate(word_list):
        if item == word:
            word_list[index] = word_list[index].capitalize()


def change_letter(word, word_list, old_letter, new_letter):
    for index, item in enumerate(word_list):
        if item == word:
            word_list[index] = word_list[index].replace(old_letter, new_letter)


words = ['Programming', 'is', 'fun']
capitalize_item('Programming', words)
print(words)
change_letter('fun', words, 'u', '$')
print(words)
