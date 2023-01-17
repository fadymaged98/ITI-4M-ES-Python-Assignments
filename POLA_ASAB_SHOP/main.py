import os
import datetime

print("\t\t Welcome To ITI Asab Shop\n", "_" * 40, "\n")
our_menu = {"Small": 10, "Medium": 15, "Large": 20}
current_cart = {"Small": 0, "Medium": 0, "Large": 0}
while 1:
    print("1.To View Sizes of Cups:        Press 1.\n"
          "2.To Add To Your Cart:          Press 2.\n"
          "3.To View Your Cart:            Press 3.\n"
          "4.To Checkout and Print Bill:   Press 4.\n"
          "5.To Exit Our Shop:             Press 5.\n")
    user_selection = input("Your Choice : ")
    print("_" * 50, "\n")
    if user_selection == '1':
        print("Our Menu:")
        print("-" * 9)
        print("1.Small Asab Cup.     10 LE.\n"
              "2.Medium Asab Cup.    15 LE.\n"
              "3.Large Asab Cup.     20 LE.")
        print("_" * 50, "\n")
    elif user_selection == '2':
        print("Choose The Required Operation(s):")
        while 1:
            print("-" * 33)
            print("1.To Add Small Cup:            Press 1.\n"
                  "2.To Add Medium Cup:           Press 2.\n"
                  "3.To Add Large Cup:            Press 3.\n"
                  "4.To Remove Small Cup:         Press 4.\n"
                  "5.To Remove Medium Cup:        Press 5.\n"
                  "6.To Remove Large Cup:         Press 6.\n"
                  "7.To Exit To Previous Menu:    Press 7.\n")
            cart_opt_select = input("Your Choice : ")
            if cart_opt_select == '1':
                cups_no = int(input("Number of Cups Required:"))
                current_cart["Small"] += cups_no
            elif cart_opt_select == '2':
                cups_no = int(input("Number of Cups Required:"))
                current_cart["Medium"] += cups_no
            elif cart_opt_select == '3':
                cups_no = int(input("Number of Cups Required:"))
                current_cart["Large"] += cups_no
            elif cart_opt_select == '4':
                cups_no = int(input("Number of Cups Required:"))
                current_cart["Small"] -= cups_no
            elif cart_opt_select == '5':
                cups_no = int(input("Number of Cups Required:"))
                current_cart["Medium"] -= cups_no
            elif cart_opt_select == '6':
                cups_no = int(input("Number of Cups Required:"))
                current_cart["Large"] -= cups_no
            elif cart_opt_select == '7':
                print("_" * 50, "\n")
                break
    elif user_selection == '3':
        print("Your Cart:")
        sums = 0
        for i in range(len(current_cart)):
            if list(current_cart.values())[i] != 0:
                print(f"{list(current_cart.keys())[i]} Cups", " " * (10 - len(list(current_cart.keys())[i]))
                      , list(current_cart.values())[i], " " * 10,
                      list(current_cart.values())[i] * list(our_menu.values())[i])
                sums += list(current_cart.values())[i] * list(our_menu.values())[i]
        if sums == 0:
            print("\t\t\t\t IS EMPTY!!")
        else:
            print("Total Price: ", sums)
        print("_" * 50, "\n")
    elif user_selection == '4':
        sums = 0
        current_bill = open("Current Bill.txt", "w")
        all_bills = open("All Bills.txt", "a")
        tmp = "Item" + " " * 10 + "Quantity" + " " * 10 + "Price\n"
        current_bill.write(tmp)
        all_bills.write(str(datetime.datetime.now()))
        current_bill.write(str(datetime.datetime.now()))
        all_bills.write("\n")
        all_bills.write(tmp)
        keys = list(current_cart.keys())
        vals = list(current_cart.values())
        for i in range(len(current_cart)):
            tmp = "{}".format(keys[i]) + " " * 9 + "{}".format(vals[i]) + " " * 21 + "{}".format(
                vals[i] * list(our_menu.values())[i]) + "\n"
            sums += vals[i] * list(our_menu.values())[i]
            current_bill.write(tmp)
            all_bills.write(tmp)
        tmp = " " * 30 + "Total Price : " + str(sums) + "\n"
        all_bills.write(tmp)
        tmp = "_" * 50
        all_bills.write(tmp)
        print("Your Bill Is Being Printed.....\n", " " * 25, "Done!!\n", " " * 15,
              "We Hope To See You Again Soon :)")
        print("_" * 50, "\n")
    elif user_selection == '5':
        print("\t\t\t\tByeeeeeeeeeeeee")
        print("_" * 50, "\n")
        break
