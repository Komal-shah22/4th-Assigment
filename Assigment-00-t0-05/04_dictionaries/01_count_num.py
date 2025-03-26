counts = {}

while True:
    num = input("Enter a number: ")
    if num == "":
        break 

    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1 

for number, count in counts.items():
    print(f"{number} appears {count} times.")
