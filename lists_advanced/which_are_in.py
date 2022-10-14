short_list = list(input().split(", "))

long_list = list(input().split(", "))

final_list = list()

for first_word in short_list:
    for second_word in long_list:
        if first_word in second_word and first_word not in final_list:
            final_list.append(first_word)


print(final_list)