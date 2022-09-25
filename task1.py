text = input('text: ')
sub_string = input('sub_string: ')

list_text = text.split()
text_new = ' '.join(filter(lambda x: sub_string not in x,list_text))
print(
    f'initial text -> {text}\nSub string - > {sub_string}\nNew text -> {text_new}')
