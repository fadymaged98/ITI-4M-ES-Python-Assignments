print("*" * 10, "Welcome To ITI Calculator", "*" * 10, "\n", "*" * 45)

while (1):
    print("\nThe Available Modes Are:\n-------------------------")
    print("1.Scientific Mode.\n2.Programmer Mode.")
    while (1):
        print("\nYour Choice : ", end="")
        mode = int(input())
        if (mode == 1):
            print("-" * 35, "\n\t\tYou Chose Scientific Mode !")
            break
        elif (mode == 2):
            print("-" * 35, "\n\t\tYou Chose Programmer Mode !")
            break
        else:
            print(" Please Enter A Valid Choice :) ")

    if (mode == 1):
        first = int(input("Enter The First Number  : "))
        second = int(input("Enter The Second Number : "))
        operation = input("The Required Operation  : ")
        answer_1 = eval(f"{first}{operation}{second}")
        print(f"\n\t\tThe Answer : {answer_1}")
    else:
        inp_format = input("Enter Number System (e.g. B for binary)--> ")
        num = input("Enter The Number To Convert--------------> ")
        conv = input("Enter Required Conversion----------------> ")
        if (inp_format == 'B'):
            j = len(num)
            answer_2 = 0
            for i in num:
                if (i == '1'):
                    answer_2 += 2 ** (j - 1)
                j -= 1
        elif (inp_format == 'D'):
            answer_2 = int(num)
        # elif (inp_format == 'H'):
        #     answer_2 = hex(num)
        # elif (inp_format == 'O'):
        #     answer_2 = oct(num)
        else:
            print("Please Enter A Valid System.")

        if (conv == 'B'):
            answer_2 = bin(answer_2)
        elif (conv == 'D'):
            answer_2 = int(answer_2)
        elif (conv == 'H'):
            answer_2 = hex(answer_2)
        elif (conv == 'O'):
            answer_2 = oct(answer_2)
        print("The Answer Is : ", answer_2)

    print("To Exit Press 1. \nTo Repeat Press Enter.")
    if (input() == '1'):
        break
