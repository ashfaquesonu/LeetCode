s = 'hello'
new = 'H' + s[1:]
print(new)

#indexing and slicing
print(s[-1])

#string Methods
print(s.count('l'))

#strip  string
s1='   hejame  '
print(s1.strip())

#repeat multiple time
print(s1 * 4)

# f string:An f-string is a way to format strings in Python using curly braces {} to insert expressions directly within the string(it can include variable directly.
name = 'alice'
age = 20
print(f"my name is {name} and age is {age}")

#accesing list elements
list = [1,2,6,4,5]
print('list elmnt is:')
print(list[:3])

#add element end of the list => .append()
list.append(11)
print(list)
#remove
list.remove(1)
print(list)

#concatinate two list
l1 = [1,2,3]
l2 = [4,5,6]
print(l1 + l2)

#check if elemnt is in list
print(2 in l1)

##Tuple Bsics =>Tuples are immutable, meaning their contents cannot be changed after they are created.
t = (1,2,3)
print(t[0])
#ffind the index of an element in a tuple

print(t.index(2))

#unpacking:Tuple unpacking is the process of assigning the elements of a tuple to individual variables.
a,b,c = t
print(a,b,c)

##set:A set is an unordered collection of unique elements.
set = {1,2,3,3}
print(set)# Output: {1, 2, 3}  # Duplicates are removed
set.add(4)
print(set)
#set method:using union()
set1 = {3,4,5}
print(set.union(set1))
#frozen set:A frozenset is an immutable version of a set. Once created, it cannot be modified.
frozen = frozenset([1,2,3])
