def findyearforage():
    try:
        user_enter_age=eval(input("please enter your present Age: "))
        age = int(user_enter_age)
    except:
        print("Please Enter Your age in Integer Number")

    x=(78-age)
    y=1941+x
    print("Your Birth Year as per You mention Age",age,"is",y)
findyearforage()

