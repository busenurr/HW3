age=float(input("please enter your age"))
if age>19:
    print("adult")
elif 10<age<=19:
    print("adolescent")
elif age<1:
    print("infant")
else:
    print("children")