def find_index(word, word_list):
    for index, item in enumerate(word_list):
        if item == word:
            return index


def upper(word, word_list):
    index = find_index(word, word_list)
    word_list[index] = word_list[index].upper()


def change_letter(word, word_list, old_letter, new_letter):
    index = find_index(word, word_list)
    word_list[index] = word_list[index].replace(old_letter, new_letter)
