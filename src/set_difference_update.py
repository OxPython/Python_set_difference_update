'''
Created on Jul 9, 2014

@author: viejoemer

HowTo remove element from a set that are in others?

¿Cómo eliminar los elemento de un conjunto que se encuentran en otros?

difference_update(other, ...)
set -= other | ...
Update the set, removing elements found in others.
'''

#Create a set with values.
s_1 = set([0,1,2,3])
print("set one", s_1)

s_2 = set([1,6])
print("set two", s_2)

s_3 = set([2,6])
print("set three", s_3)

#Using difference_update
s_1.difference_update(s_2)
print("set one difference_update",s_1)

#For several sets
s_3.difference_update(s_1,s_2)
print("set two difference_update",s_3)

s_1 = set([0,1,2,3])
s_2 = set([1,6])
s_3 = set([2,6,13])
#Another way is set -= other | ...
s_3 -= s_1 | s_2
print("set two difference_update",s_3)