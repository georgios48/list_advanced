rooms_number = int(input())

visitors_x = []
visitors_number = []
list_input = []

chairs_needed = 0
chairs_left = 0
no_game = False

ppl = 0
chairs = 0

for room in range(1, rooms_number + 1):
    list_input = input().split(" ")
    visitors_x.append(list_input[0])
    visitors_number.append((list_input[1]))
    map(int, visitors_number)

    ppl = visitors_number[0]
    chairs = visitors_x[0]

    ppl = int(ppl)
    chairs = int(len(chairs))

    if chairs > ppl:
        chairs_left += chairs - ppl
    if ppl > chairs:
        chairs_needed += ppl - chairs
        print(f"{chairs_needed} more chairs needed in room {room}")
        no_game = True
        chairs_needed = 0
    del visitors_x[0]
    del visitors_number[0]

if not no_game:
    print(f"Game On, {chairs_left} free chairs left")