#List
fruits=['apple', 'mango', 'banana', 'grapes', 'orange']
print(fruits)
fruits.append('kiwi')
print(fruits)
print(fruits[2])
fruits[2]='papaya'
print(fruits)
print(fruits[1:4])
print(len(fruits))

#Tuple
colors=('red', 'green', 'blue', 'yellow')
print(colors)
print(colors[-2])
#colors[1]='orange' #This will give an error because tuples are immutable
type(colors)
print(type(colors))