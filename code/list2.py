fruits=["apple","banana"]

#append() - add one iteams

fruits.append("cherry")
print(fruits)

#insert() - add one item at the specified index
fruits.insert(1,"mango")
print(fruits)

#extend() - merge another list this one
more_fruits=["kiwi", "grape"]
fruits.extend(more_fruits)
print(fruits)