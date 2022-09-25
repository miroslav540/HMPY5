list_languages = ['python', 'c#', 'c+', 'java']
list_len_lang = [i for i in range(1, len(list_languages) + 1)]


def get_list_tuple(list_1, list_2):
    list_2_ch = [i.upper() for i in list_2]
    result = list(zip(list_1, list_2_ch))
    return result


def filter(list_tuple):
    new_list_len_lang = []
    new_list_lenguages = []
    for i in list_tuple:
        order, languages = i
        sum_bal = 0
        for j in languages:
            sum_bal += ord(j)
        if not sum_bal % order:
            new_list_len_lang.append(sum_bal)
            new_list_lenguages.append(languages)
    new_list_tuple = list(zip(new_list_len_lang, new_list_lenguages))
    return new_list_tuple


list_tuple = get_list_tuple(list_len_lang, list_languages)
print(list_tuple)
