list1 = [1,2,3,4,5,6,7,8,-1,-2,-3]
counter = 0
while counter < len(list1):
    if list1[counter] > 0:
        print(list1[counter])

    else:
        print("this is a negative number")
    counter += 1
#when using if , you need an else and another command.
