#Internship Task 1

import random

# range of the number
this_num = random.randint(1, 100)
tries = 1

yourname = input("wow,what is yourname??")
print("wow",yourname )

Ans = input("Do you want to drive a car?[ha/na]")

#your ans for ha statement of case
if Ans == "ha":
    print("the numner 1 and 100, username 3 tries")
    username = int(input("username"))

    if username>this_num:
        print("lower")

    if username<this_num:
        print("upper")

        if(this_num%2 == 0):
            print("even number is hear now")

        if (this_num % 2 != 0):
            print("odd bumber is hear now")

#your ans for na statement of case

if Ans == "na":
    print("nothing")

    while username != this_num:
        tries = 3
        username = int(input("please try again"))

        if(this_num%2 == 0):
            print("even number is hear now")
        if(this_num%2 != 0):
            print("odd number is hear now")


            if username > this_num:
                print("lower")
            if username < this_num:
                print("upper")

                if tries == 3:
                    print("correct",this_num)

                    break

                if username == this_num:
                    print("congrulations")
                if username != this_num:
                    print("sorry")




