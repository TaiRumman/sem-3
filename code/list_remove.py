fruits=["apple","banana","cherry","mango","kiwi"]

#remove() by value
fruits.remove("banana")
print(fruits)

#pop() return and remove last items
last=fruits.pop()
print(fruits)
print(last)

#delete by index
del fruits[0]
print(fruits)

#clear() emptirs everything
fruits.clear()
print(fruits)
