participants = ["Judith", "Joanna", "Emmanuel", "Ibrahim", "Philip"]

position = 1
for name in participants:
    if name == "Emmanuel":
        print("bBout to break")
        break
    print("About to increment")
    position = position + 1

print(position)

# index = 0
for current_index in range(len(participants)):
    print(current_index)
    if participants[current_index] == "Ibrahim":
        print("Have Breaked")
        break
    print("NOt breaked")

print(current_index + 1)

# Number divisible by 3
for number in range(10):
    if number % 3 == 0:
        print(number)
        print("Divisible by 3")
        continue
    print(number)
    print("Not Divisible by 3")