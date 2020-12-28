weight = input("enter your weight : ")
choice = input("enter your choice (K)g or (L)bs : ")
if choice == 'K' or choice == 'k':
    pound = int(weight) / 0.45359237
    print("The weight of pounds : %f" % pound)
elif choice == 'L' or choice == 'l':
    kilogram = int(weight) * 0.45359237
    print("The weight of pounds : %f" % kilogram)
else:
    print("check your choice...")

