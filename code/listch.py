fruits=["apple", "banana", "cherry"]

#change single items:-
fruits[1]="mango"
print(fruits)

#replace a slice:-
fruits[0:2]=["kiwi", "grape"]
print(fruits)#kiwi grap cherry.

#replace with more items then you removed:-
fruits[1:2]=["fig","date","plum"]
print(fruits)

