#Method 1 for concatenation

txt1 =  "Dhananjeyan"
txt2 =  "Thejasri"
print(txt1 + txt2)

# method 2 - % or C-style string formating

name = "Theja"
age = 21
score= 91.05
print("%s age is %d has scored %.2f in HSC."%(name,age,score))

#method 3 - .format method()
print("{} age is {}. She has scored {} in HSC.".format(name,age,score))

#method 4 - f'string
PersonName = "Thejasri"
Company = " Tesla "
print(f"{PersonName} works in {Company}")