while(True):
    try:
        c = int(input("what is the temperature in Celsius?"))

        F = (c *9/5) + 32

        print("The temperature in C is %s" %F)
        break
    except ValueError:
        print("please insert a number.")