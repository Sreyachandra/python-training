dict={}
dict['a'] = 'ab'
dict['b'] = 'cd'
dict['c'] = 'mn'
dict['d'] = 'op'
print(dict)                                      #{'a': 'ab', 'b': 'cd', 'c': 'mn', 'd': 'op'}
print(dict['b'])                                 #cd
for key in dict: print(key)                      #a
                                                  b
                                                  c
                                                  d
for key in dict.keys(): print(key)                #exactly the same as above

print(dict.keys())                                #dict_keys(['a', 'b', 'c', 'd'])
print(dict.values())                              #dict_values(['ab', 'cd', 'mn', 'op'])
for key in sorted(dict.keys()):
 print(key , dict[key])                           #a ab
                                                  b cd
                                                  c mn
                                                  d op
 #nested dictionary
a={1:'dictionary',2:'for', 3:{'A':'welcome','B':'to','c':'lab'}}
print(a)                                                            #{1: 'dictionary', 2: 'for', 3: {'A': 'welcome', 'B': 'to', 'c': 'lab'}}
#method
list=['a' , 'b' , 'c']
del list[0]
print(list)                                                          #['b', 'c']
#function(clear())
a={
 "car": "hgj" ,
 "model": "asd" ,
 "year": 2000
}
a.clear()
print(a)                                                               #{}
#function(copy())
old={1:'one' , 2: 'two'}
new= old.copy()
print('old: ', old)
print('new: ', new)                                                      #old:  {1: 'one', 2: 'two'}
                                                                         new:  {1: 'one', 2: 'two'}
#function(values)
a = {'anu': 1, 'anju' : 2, 'arya' : 4}
print(a.values())                                                         #dict_values([1, 2, 4])
#function(pop())
a = {'anu': 1, 'anju' : 2, 'arya' : 4}
element =a.pop('anu')
print('the poped element is:',element)
print('the dictionary is:',a)                                              #the poped element is: 1
                                                                           the dictionary is: {'anju': 2, 'arya': 4}
#function(setdefault())
a = { 'name': 'anu'}
age=a.setdefault('age',23)
print('a=',a)
print('age = ',age)                                                          #a= {'name': 'anu', 'age': 23}
                                                                               age =  23
