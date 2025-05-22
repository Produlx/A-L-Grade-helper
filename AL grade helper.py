print("HI, i hope you have good day..")

marks_user = int(input("Enter your marks: "))

if marks_user == 75:
    print("A")
else:
    if marks_user == 65:
        print("B")
    else:
        if marks_user == 55:
            print("C")
        else:
            if marks_user == 35:
                print("S")
            else:
                if marks_user < 35:
                    print(f'"w" try again')

print(f'you got {marks_user} marks..{Greeting}')

