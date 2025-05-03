age = int(input("Hi, Enter you age "))
if age <=2 or age > 16:
    print(" you are not eligible for admission in our school")
elif age >= 2:
    print("you are eligible for admission in playgroup")
elif age >= 3:
    print("you can get admission in class nursery")
elif age >= 4:
    print("you are eligible for admission in class KG")
elif age > 4 and age <= 9:
    print("you are eligible for admission in primary section")
elif age > 9 and age <= 14:
    print("you are eligible for admission in Middle Section")
else:
    print("you are eligible for admission in high school")