'''
dictionary{key:value}
we can store data as key:value pair
key--keys are unique we can't add duplicate with the same variable
value--allow duplicate values and all data types mutable and immutable
metods
keys()---this method is used to access all keys of a dict
values()---this method is used to access all values of a dict
clear()--is used clear or empty the dict

sbi_navya={"Name":"Navya","Role":"mentor","sal":6555}
print(sbi_navya)
print(sbi_navya.keys())
print(sbi_navya.values())
sbi_navya.clear()
print(sbi_navya)

set--- set data type is a unordered collection and it never allows duplicates.
methods
union()---this is used to add or get 2 differnt sets without duplicate
intersection()---this is used to get common values in both the sets
difference()---this is used to get the difference b/w 2 sets
'''
set_1={1,2,3,4}
set_2={4,5,5,6,7,8}
print(set_1)
print(set_2)
print(set_1.union(set_2))
print(set_1.intersection(set_2))
print(set_1.difference(set_2))
print(set_2.difference(set_1))
set_1.pop()
print(set_1)
 
