lst = [0, 1, 2, 3]
print(lst) # [0, 1, 2, 3]
lst.insert(2, 9)
print(lst) # [0, 1, 9, 2, 3]
lst.insert(0, 17)
print(lst) # [17, 0, 1, 9, 2, 3]
lst.insert(10, 5)
print(lst) #[17, 0, 1, 9, 2, 3, 5]
lst.insert(-10, 5)
print(lst) # [5, 17, 0, 1, 9, 2, 3, 5]

lst1 = [0, 1, 2, 3]
lst2 = [5, 6]
print(lst1) # [0, 1, 2, 3]
lst1.append(5)
print(lst1) # [0, 1, 2, 3, 5]
lst1.append(-6)
print(lst1) # [0, 1, 2, 3, 5, -6]
lst1.append(lst2)
print(lst1) # [0, 1, 2, 3, 5, -6, [5, 6]]

lst = [0, 1, 2, 3, 4, 5, 3]
lst.remove(6)
print(lst)
#loi