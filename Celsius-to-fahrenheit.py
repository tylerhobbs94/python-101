# while(true): makes it a loop so when they use a word number I.E : ten it restarts.
while(True):
#try allows except valueError so it catches the wrong answer.
    try:
        c = int(input("what is the temperature in Celsius?"))

        F = (c *9/5) + 32

        print("The temperature in C is %s" %F)
        break
    except ValueError:
        print("please insert a number.")
        # break stops the loop when given the correct answer.