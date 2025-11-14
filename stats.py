def word_count(text):
    words = text.split()
    return len(words)

def char_count(word):
    words = word.lower()
    running_count = {}
    for char in words:
        if char in running_count:
            running_count[char] += 1
        else:
            running_count[char] = 1
    return running_count

def sorted_dict(char_count):
    list_of_dicts = []
    new_list = []
    for i in sorted(char_count, key=lambda x: char_count[x], reverse=True):
        if i.isalpha():
            list_of_dicts.append({"char": i, "num": char_count[i]})
            new_list.append(i +": "+ str(char_count[i]))
    return  new_list


