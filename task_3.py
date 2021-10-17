percentage_step = 1
percentage_list = []
while percentage_step < 101:
    percentage_list.append(percentage_step)
    if percentage_step < 5:
        declension_word = '% Процента'
    else:
        declension_word = '% Процентов'
    print(percentage_list[percentage_step - 1], declension_word)
    percentage_step = percentage_step + 1


