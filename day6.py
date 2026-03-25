'''
list_1=[1,2,3,"Python",[1,2,["Python","Java"],"Language"]]
print(list_1[4])
print(list_1[4][2])
print(list_1[4][2][0])
print(list_1[4][2][0][3])

append()---add new ele to list from the last index
syntax-----var_name.append(item)
list_2=[1,2,3,4,5]
print(list_2)
list_2.append(67)
print(list_2)
list_2.append([68,9])  #[68,9] is a item appended in the form of item,it increases the list index value by single item
print(list_2)

extend()----add new elements to the list but only add individual items, it increases the list index value by the num of individuals
syntax---var_name.extend(item)
list_2=[1,2,3,4,5]
print(list_2)
list_2.extend("Navya")
list_2.append("Navya")
print(list_2)

remove()
it wil delete the item or value directly  from the list
syntax-----var_name.remove(item)
list4=[23,45,56,80,"Python"]
print(list4)
list4.remove("Python")
print(list4)

pop()--it will delete the item or value by using the index of the item
syntax----var_name.pop(index_value)'''

list4=[23,45,56,80,"Python"]
print(list4)
list4.pop(4)
print(list4)
