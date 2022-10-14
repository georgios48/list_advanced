all_list = list(map(int, input().split(", ")))

positive = [positive for positive in all_list if positive >= 0]

negative = [negative for negative in all_list if negative < 0]

even = [even for even in all_list if even % 2 == 0]

odd = [odd for odd in all_list if odd % 2 != 0]

positive = list(map(str, positive))
print(f"Positive: {', '.join(positive)}")

negative = list(map(str, negative))
print(f"Negative: {', '.join(negative)}")

even = list(map(str, even))
print(f"Even: {', '.join(even)}")

odd = list(map(str, odd))
print(f"Odd: {', '.join(odd)}")