counter = 1
sum = 0

while counter <= 10:
    print(counter)
    sum = sum + counter
    counter = counter + 1

print(sum)

letters = ["a", "b", "c", "d", "e"]
index = 5
while index < len(letters):
    print(index)
    print(letters[index])
    index = index + 1

print("===========================")

height = 5000
velocity = 50
time = 0
while height > 0:
    height = height - velocity
    time = time + 10

print(height)
print(time)
