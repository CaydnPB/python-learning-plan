# Function to double age of each person
def double_age(person_list):
    updated_list = []
    for person in person_list:
        name, age, country = person
        updated_list.append((name, age * 2, country))
    return updated_list

# Sample list of people
people_data = [
    ("Alice", 25, "USA"),
    ("Bob", 30, "France"),
    ("Charlie", 22, "UK"),
    ("Daniel", 18, "Australia"),
    ("Eve", 21, "UK"),
]

# Print details of each person
print("Details of each person:")
for person in people_data:
    print(f"Name: {person[0]}, Age: {person[1]}, Country: {person[2]}")

# Double age of each person
updated_people = double_age(people_data)
print("\nAge doubled for each person:")
for person in updated_people:
    print(f"Name: {person[0]}, Updated Age: {person[1]}, Country: {person[2]}")

# Check country of each person
specific_country = input("\nWhich country would you like to check for? ")
for person in people_data:
    if person[2] == specific_country:
        print(f"{person[0]} is from {specific_country}")
    else:
        print(f"{person[0]} is not from {specific_country}")

# Create dictionary for each country
people_by_country = {}
for person in people_data:
    name, age, country = person
    if country in people_by_country:
        people_by_country[country].append((name, age))
    else:
        people_by_country[country] = [(name, age)]

# Print the dictionary
print("\nPeople from each country:")
for country, people_list in people_by_country.items():
    print(f"{country}: {people_list}")
