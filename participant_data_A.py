participant_number = 5
participant_data = []
registered_participants = 0
output_file = open("participant_data.txt", "w")

while registered_participants < participant_number:
    temp_part_data = []
    name = input("Please Enter Your name: ")
    temp_part_data.append(name)

    country = input("Please Enter Your Country: ")
    temp_part_data.append(country)

    age = int(input("Please Enter Your Age: "))
    temp_part_data.append(age)

    print(temp_part_data)
    participant_data.append(temp_part_data)
    print(participant_data)

    registered_participants += 1

for participant in participant_data:
    for data in participant:
        output_file.write(str(data))
        output_file.write(" ")
    output_file.write("\n")

output_file.close()

input_file = open("participant_data.txt", "r")

input_list = []

for line in input_file:
    tempo_participant = line.strip("\n").split()
    input_list.append(tempo_participant)

age = {}
for part in input_list:
    temp_age = int(part[-1])
    if temp_age in age:
        age[temp_age] += 1
    else:
        age[temp_age] = 1

print(age)

oldest = 0
youngest = 100
most_occuring_age = 0
counter = 0

for temp_age in age:
    if temp_age > oldest:
        oldest = temp_age
    if temp_age < youngest:
        youngest = temp_age
    if age[temp_age] > counter:
        counter = age[temp_age]
        most_occuring_age = temp_age

print(oldest)
print(youngest)
print("the most occuring age is", most_occuring_age, "with", counter, "participant")

input_file.close()
