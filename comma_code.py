shopping_list = []
while True:
    print('Enter an item for your list, or leave blank')
    item = input()
    if item == '':
        break
    shopping_list += [item]

print(shopping_list)


def sentence_creator(list):
    shopping_string = ''
    for item in list[:-1]:
        shopping_string += item + ', '
    shopping_string += 'and ' + shopping_list[-1]
    print(shopping_string)

sentence_creator(shopping_list)