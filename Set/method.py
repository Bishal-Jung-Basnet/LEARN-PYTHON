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