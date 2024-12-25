# # # student={"Bishal": 90, "Sujan": 80, "Ramesh": 70}
# # # print(student["Bishal"])
# # # print(student)
# # # del student["Ramesh"]
# # # student["Hari"]=60
# # # print(student)
# # country={
# #     "Nepal":"Kathmandu",
# #     "India":"New Delhi"
# # }
# # print(country["Nepal"])
# # print(country["India"])
# # print(country)
# # type(country)
# # country["USA"]="Washington DC"
# # del country["India"]
# # print(country)
# # # country.clear() #clears all the elements in the dictionary
# # # print(country)
# # country["Nepal"]="Bagmati"
# # print(country)
# countryCapitals = {
#     "Nepal": "Kathmandu",
#     "India": "New Delhi",
#     "USA": "Washington DC"
# }
# for country in countryCapitals:
#     print(country)

# print()
# for counrty in countryCapitals:
#     capital =countryCapitals[country]
#     print(capital)

# countryCapitals = {"England": "London", "Italy": "Rome"}

car = {
    "Brand": "Ford",
    "Model": "Mutang",
    "year": 1990
}
# x = car.pop("Model")
# # print(car)
# print(x)
car.update({"Color":"Black"})
# print(car)
x = car.copy()
print(x)