import json

# Convert dictionary to JSON
person_dict = { 'name': 'Luciano', 'age': 33 }
print(f"My name is {person_dict['name']} and I am {person_dict['age']} years old")

# Nested dictionaries and converting to JSON
person_dict['languages'] = { 'speciality': [], 'experience': [] }
person_dict['languages']['speciality'] = ['JavaScript', 'C#']
person_dict['languages']['experience'] = ['Python', 'SQL Server']
print(json.dumps(person_dict))

# Looping through values
print("My specialities are:")
for s in person_dict['languages']['speciality']:
    print(s)
print("I have experience in:")
for e in person_dict['languages']['experience']:
    print(e)