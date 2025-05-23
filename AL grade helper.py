print("HI, i hope you have good day..")

print("")

marks_user = int(input("Enter your marks: "))

if marks_user >= 75:
    print("A")
else:
    if marks_user >= 65:
        print("B")
    else:
        if marks_user >= 55:
            print("C")
        else:
            if marks_user >= 35:
                print("S")
            else:
                if marks_user < 35:
                    print(f'"w" try again')

if marks_user >= 75:
    Greeting = "Good_Luck"
else:
    if marks_user >= 65:
        Greeting = "Wow"
    else:
        if marks_user >= 55:
            Greeting = "Not bad"
        else:
            if marks_user >= 35:
                Greeting = "Try harder..you can do it!"
            else:
                Greeting = "Forcus bn,,,u can do it"
    


print(f'you got {marks_user} marks..{Greeting}')
print("G'Day")

