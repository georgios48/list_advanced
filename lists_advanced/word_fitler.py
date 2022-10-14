given_words = list(input().split(" "))

even_lenght = [x for x in given_words if len(x) % 2 == 0]

for element in even_lenght:
    print(element)