number = {21, 34, 54, 12}

print('Initial Set:', number)

#using add() method
number.add(32)
print('Updated set:', number)

companies = {'Lacoste', 'Ralph Lauran'}
techCompanies = ['apple', 'google', 'apple']
#using update()
companies.update(techCompanies)
print(companies)

#remove from set
removedValue= companies.discard('Lacoste')
print('Set after remove()', companies)

fruits = {"apple", "Peach", "Mango"}
#for loop to access each fruits
for fruit in fruits:
    print(fruit)

print(len(fruits))

A = {1,3,5}
B = {0,1,2,4}
#union operation using |
print("Union  using | :",A|B)
print("Union using union():", A.union(B))

#perform intersection using &
print("Untersection using &: ",A&B)
#intersection using intersection()
print("Untersection using intersection(): ",A.intersection(B))
