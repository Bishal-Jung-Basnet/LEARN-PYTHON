user_input = str(input("Enter date in a format(mm/dd/yyyy): "))
month, day, year = user_input.split('/')

def month_finder(value):
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    pos = (int(value)-1)*3
    monthAbbrav = months[pos:pos+3]
    return monthAbbrav
print("The conversion of this {0} is {1} {2}, {3}.".format(user_input, month_finder(month), day, year))