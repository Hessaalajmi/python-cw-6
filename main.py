# write your code here
person = {
            "name" : "hessa",
            "age" : 14,
            "hobbies" : ['coding', 'archery', 'swimming']
}

print(person.get('name'))
print(person.get('age'))

person['age'] = 15
person['country'] = 'kuwait'
print(person)
length = len(person)
print(length)

person['hobbies']

def check_hobbies(person):
    if len(person['hobbies']) >= 3:
        print('YOU ARE AMAZING')
    else:
        False

check_hobbies(person)
