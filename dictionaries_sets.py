# sets = {"Element1", "Element2", "Element1", "Element4"}
# print(sets)
# if "Element1" in sets:
#     print("Yes")

# set
country_list = []
for i in range(5):
    country = input("Please Enter Your country: ")
    country_list.append(country)

country_set = set(country_list)

print(country_list)
print(country_set)

if "Brazil" in country_set:
    print("Attended")

# Dictionary the deference between a dictionary and a set is that a dictionary kad a key and a value
country_dictionary = {}

for country in country_list:
    if country in country_dictionary:
        country_dictionary[country] += 1
    else:
        country_dictionary[country] = 1

print(country_dictionary)