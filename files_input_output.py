vacationSpots = ["London", "Paris", "New York", "Utah", "Iceland"]

vacationFile = open("vacationPlaces", "w")

for spots in vacationSpots:
    vacationFile.write(spots + "\n")

vacationFile.close()

vacationFile = open("vacationPlaces", "r")

first_line = vacationFile.readline()
print(first_line)

second_line = vacationFile.readline()
print(second_line)

for line in vacationFile:
    print(line, end= "")

# the_whole_file = vacationFile.read()
# print(the_whole_file)
vacationFile.close()

final_spot = "Thailand"

vacationFile = open("vacationPlaces", "a")
vacationFile.write(final_spot)
vacationFile.close()

vacationFile = open("vacationPlaces", "r")
for line in vacationFile:
    print(line, end="")

vacationFile.close()

with open("vacationPlaces", "r") as vacationFile:
    for line in vacationFile:
        print(line)