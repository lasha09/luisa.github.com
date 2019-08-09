list =[]
print("initial blank list")
print(list)

list =("geeksforgeeks")
print("\nlist with the use of string:")
print(list)

list = ["geeks", "for", "geeks"]
print("\nlist containing multiple values: ")
print(list[0])
print(list[2])

list = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print( "\nlist with the use of numbers: ")

list = [1, 2, 'geeks' , 4, 'for', 6, 'geeks']
print("\nlist with the use of the mixed values: ")
print(list)

name = ["luisa", "estella", "sam", "paola", "elise", "pheonix"]
print("\nlist containing multiple names: ")
print(name[0])
print(name[5])

print("*********")
listA = []
print("initial blank list: ")
print(listA)
listA.append(1)
listA.append(2)
listA.append(4)
print("\nlist after addition of three elements: ")
print(listA)

for i in range(1, 5):
    listA.append(i)
print("\nlist after addition of elements from 1-3: ")
print(listA)

listA.append((5, 6))
print("\nlist after addition of a tuple: ")
print(listA)

list2 = ['for', 'geeks']
listA.append(list2)
print("\nlist after additon of a list")
print(listA)

listA.insert(3, 12)
list2.insert(0, 'geeks')
print("\nlist after preforming insert operation")
print(listA)

list3 = [ 1, 2, 3]
list3.extend('geeks')
print(list3)

listA = []
list2 = ['for','geeks']
listA.extend(list2)
print(listA)
