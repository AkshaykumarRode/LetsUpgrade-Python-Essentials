# Data Structure Assignment


# 1. list
lst = ["Akshay", 7, 8.0, 1998.12,"abc"]
print(lst)
j = lst                  # copy method
print(j)
lst.append('Good')    # append method
print(lst)
b = lst.count(8.0)      # count method
print(b)
c = lst.index('Akshay')   # index method
print(c)
lst.insert(2,4.5)    # insert method
print(lst)
new_lst = ['a',22,100.2]
lst.extend(new_lst)     # extend method
print(lst)
f = lst.pop(3)            # pop method
print(f)
g = lst.reverse()       # reverse method
print(lst)
h = lst.remove('Akshay')     # remove method
print(lst)
i = lst.clear()      # clear method
print(lst)


# 2. Dictionaries
dct = {'name':'Akshay', 'age':21, 'email':'akshayrode65@gmail.com', 'dept':'Aeronautical'}
print(dct)
a2 = dct.items()        # items method
print(a2)
b2 = dct.values()       # values method
print(b2)
c2 = dct.pop('age')     # pop method
print(c2, dct)
dct_1 = {'nickname': 'ASR'}
dct.update(dct_1)       # update method
print(dct)
d2 = dct.setdefault('salary') # setdefault method
print(d2, dct)
e2 = dct.popitem()      # popitem method
print(e2, dct)
f2 = dct.keys()         # keys method
print(f2)
print('Name: ', dct.get('name')) # get method
# value is not provided
print('Salary: ', dct.get('salary'))
# value is provided
print('Salary: ', dct.get('salary', 0.0))
print(dct)
keys = {'a', 'e', 'i', 'o', 'u' }   # fromkeys method
value = [1]
vowels = dict.fromkeys(keys, value)
print(vowels)
# updating the value
value.append(2)
print(vowels)
dct_new = dct.copy()    # copy method
print('copied dict: ',dct_new)
dct.clear()             # clear method
print('dct =', dct)


# 3. set
A = {'a','b','c','d','e','f','g'}
B = {'a','b','c','x','y','z'}
A.add('h')      # add method
print(A)
A.remove('g')   # remove method
print(A)
print(A.difference(B)) # difference method
print(B.intersection(A))# intersection method
print(A.pop(),A)      # pop method
print(A.union(B))     # union method


# 4.tuples
tup = (1,5,7,9,1,4,5,3,6,7,9,5,4,2,1,8,6,2,4,1)
print(tup.index(5))     # index method
print(tup.count(1))     # count method


# 5. string
string = "i am Akshaykumar Rode"
print(string.capitalize())  # capitalize method
print(string.center(50))    # center method
print(string.casefold())    # casefold method
print(string.count('a'))    # count method
print(string.endswith('de'))# endswith method
stringnew = 'abc\t123\txyz'
print(stringnew.expandtabs())  # expandtabs method
print(string.find('Rode'))     # find method
