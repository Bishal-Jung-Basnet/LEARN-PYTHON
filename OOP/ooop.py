# def main():
#  print("change counter\n")
#  print("please enter the count of each coin type")
#  quarters= int (input("quarters:"))
#  dime= int (input("dimes:"))
#  nickels= int (input("nikels:"))
#  pennies =  int (input("pennies:"))
#  total = quarters * 25 + dime * 10 + nickels * 5 + pennies
#  print ("the total value of your change is ${0}.{1:0>2}".format(total//100, total%100))



# main()

# list = list(range(1,11))
# print("List of int:",list)
# repList = list*2
# print("repeated list:",repList)
# for i in list:
#     print(i)
# element = list[2]
# lastElement = list[-1]
# print(f"First element: {element}, Last elementL {lastElement}")
# sliceList = list[2:6]
# print("Slice from index 2:5",sliceList)

# lastElementelement = list[-3:]
# print("Prints last three element: ",lastElement)

# list = list(range(1,11))
# print("List of int:",list)
# repList = list*2
# print("repeated list:",repList)
# for i in list:
#     print(i)
# element = list[2]
# lastElement = list[-1]
# print(f"First element: {element}, Last elementL {lastElement}")
# sliceList = list[2:6]
# print("Slice from index 2:5",sliceList)
# lastElementelement = list[-3:] 
# print("Prints last three element: ",lastElement)
# sqlist = [x**2 for x in list]
# print("List of sqr:", list)
# evenList = [x for x in list if x%2==0]
# print("List of even number:",evenList)
# matrix = [
#     [1,2,3],
#     [4,3,7],
#     [3,5,7]
# ]
# element = matrix[1][2]
# print("Element in second row, third column",element)
# print(" Matrix")
# for row in matrix:
#     print(row)



# file= open("py.txt","r")
# print (file.read())

# file= open("py.txt","r")

# for each in file :
#     print(each)

# file=open('hridaya.txt','w')
# file.write("This is the write command\n")
# file.write("It allows us to write in a particular file\n")
# file.write("Abhinav is gay\n")
# file.close

# file=open('hridaya.txt','a')
# file.write("Nishant is gay\n")
# file.write("shahil is gay\n")
# file.write("Suman is gay")
# file.close

                               # this works aot same as well
# with open("hridaya.txt","r")as f :
#     f.read()
# with open("hridaya.txt","w")as f :
#     f.write("hello")

# with open("hridaya.txt","a")as f :
#     f.write("new text")

                                # till here


# class Parrot:
#     name =""
#     age = 0
# parrot1 = Parrot()
# parrot1.name = "pyaro"    
# parrot1.age = 10 

# parrot2 = Parrot()
# parrot2.name = "pyari"    
# parrot2.age = 11

# print(f"{parrot1.name}is {parrot1.age}years old")
# print(f"{parrot2.name}is {parrot2.age}years old")

# class Animal():
#     def eat(self):
#         print("eating")

# class Lion(Animal):
#     def roar(self):
#         print("I'm the King of the jungle")
# lion1 = Lion()
# Lion1.eat()
# Lion1.sleep()
# Lion1.roar()


# class birds():
#      def flight(self):
#          print("flying")
# obj_birds= Birds()
# obj_spp= sparrpw()

 
     

# class Recipe:
#     def __init__(self,name,cuisine,ingredients,rating):
#         self.name=name
#         self.cuisine=cuisine
#         self.ingredients=ingredients
#         self.rating=rating
     
#     def get_name(self):
#         return self.name

#     def set_name(self, name):
#         self.name = name
     
#     def get_cuisine(self):
#         return self.cuisine                                                # Verry verry inportant

#     def set_cuisine(self, cuisine):
#         self.cuisine = cuisine
 
#     def get_ingredients(self):
#         return self.ingredients

#     def set_ingredients(self, ingredients):
#         self.ingredients = ingredients 
    
#     def get_rating(self):
#         return self.rating

#     def set_rating(self, rating):
#         self.rating = rating 

#     def __str__(self):
#         return f"{self.name} -Cusine:{self.cuisine},Ingredients : {self.ingredients}, Rating: {self.rating}"  


# class Song:
#     def __init__(self,title,artist,length):
#         self.title=title
#         self.artist=artist
#         self.length=length
        
     
#     def get_title(self):
#         return self.title

#     def set_title(self, title):
#         self.title = title
     
#     def get_artist(self):
#         return self.artist                                                # Verry verry inportant

#     def set_artist(self, artist):
#         self.artist = artist
 
#     def get_length(self):
#         return self.length

#     def set_length(self, length):
#         self.length = length 
    
#     def __str__(self):
#         return f"{self.title} by{self.artist}( {self.length}`)"  




class Subject:
    def __init__(self,name,code,credits):
        self.name=name
        self.code=code
        self.credits=credits

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
 
     
    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_credits(self): 
        return self.credits

    def set_credits(self, credits):
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.code}) with {self.credits}credits"   


# Subject1 = Subject("Discreet Mathamatics","BIT108",4)
# print(Subject1)       
# print(Subject1.get_name())
# Subject1.set_name("calculas")
# print(Subject1.get_name())

SubjectList = []

with open('subjectData.txt','r')as file:
    for line in file:
        data = line.strip().split(',')
        subject = Subject(data[0],data[1],int(data[2]))
        SubjectList.append(subject)

for subject in SubjectList:        
     print(subject)

new_subject = Subject('final year priject II','BIT305',5)
SubjectList.append(new_subject)
year_3_count = 0
for student in SubjectList:
    if subject.get_code()[3] == '3':
        year_3_count+=1
print("Number of year 3 subject:", year_3_count)
#calculate average 
average_credit = total_credit / num_subjects
# display average
print("Average credit of all subjects:", average_credit)
#open file for writing
with open('newSubject.txt','w') as file:
    # Interate t
    for subject in SubjectList:
        file.write(f"(subject.get_name())")