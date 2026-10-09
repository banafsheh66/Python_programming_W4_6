print("Program starting.")

Number = int(input("Insert a positive integer: "))
Steps = 0
print(Number, end="")

while Number != 1:
    if Number % 2 == 0:
        Number = Number // 2
    else:
        Number = Number * 3 + 1
    print(" -> ", Number, sep="", end="")
    Steps += 1

print()
print(f"Sequence had {Steps} total steps.")
print()
print("Program ending.")