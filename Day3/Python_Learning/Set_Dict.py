#set
numbers={1,2,3,4,5}
print(type(numbers))
numbers.add(6)
print(numbers)
numbers.remove(3)
print(numbers)
#print(numbers[4]) #This will give an error because sets are unordered and do not support indexing

#dictionary
person={'name':'kaarthik', 'age':25, 'city':'chennai'}
print(person)
print(person['name'])
print(type(person))
print(person.keys())
print(person.values())
person['age']=26
print(person)
person.pop('city')
print(person)
person.update({'country':'India'})
print(person)
