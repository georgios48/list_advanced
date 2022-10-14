current_version = list(map(int, input().split(".")))

current_version[-1] += 1

if current_version[-1] > 9:
    current_version[-2] += 1
    current_version[-1] = 0

    if current_version[-2] > 9:
        current_version[0] += 1
        current_version[-2] = 0


final_version = list(map(str, current_version))

print(".".join(final_version))