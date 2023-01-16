# Lists Declaration-------------------------------------------------------------------
fruits_list = {"Apples": 10,
               "Oranges": 12,
               "Bananas": 14,
               "Kiwiis": 20,
               "Mangos": 30,
               "Strawberries": 20}
shopping_list = {}
# ----------------------------------------------------------------------------------


while 1:

    # Main Menu-----------------------------------------------------------------------
    print("\t\t\t", "*" * 10, "Welcome To ITI Store", "*" * 10, "\n\t\t\t", "-" * 42)
    print("\n1.If You Are A Customer: Press 1."
          "\n2.If You Are The Owner:  Press 2."
          "\n3.To Exit The Shop:      Press 3.")
    # ---------------------------------------------------------------------------------

    mode = input("\n\nYour Choice : ")
    print("_" * 70)

    # Customer Menu----------------------------------------------------------------------------------
    if mode == '1':
        print("\t\t\t\t\t\tWelcome Customer!\n\n")
        while 1:
            print("1.To View A List of Our Products: Press 1.\n"
                  "2.To Buy From Our Products:       Press 2.\n"
                  "3.To Print Your Bill:             Press 3.\n"
                  "4.To Exit To The Previous Menu:   Press 4.\n")
            customer_choice = input("Your Choice : ")
            if customer_choice == '1':
                print("_" * 70, "\nOur Products Are : ")
                for i in range(len(fruits_list)):
                    item = list(fruits_list.keys())[i]
                    price = list(fruits_list.values())[i]
                    print((i + 1), ".", item, " " * (20 - len(item)), "Price: ", price, "LE")
                print("_" * 70)
            elif customer_choice == '2':
                print("_" * 70, "\nPlease Enter The Name of Product Followed By The"
                                "\nRequired Amount In Kg (When Finished, Type 'Stop'):\n")
                i = 1
                while i:
                    product = input(f"Product {i}: ")
                    if product == "Stop":
                        break
                    quantity = float(input("Quantity : "))
                    print()
                    shopping_list[product] = quantity
                    i += 1
                print("_" * 70)
            elif customer_choice == '3':
                print("_" * 70)
                if len(shopping_list) == 0:
                    print("You Have Bought Nothing Yet :)")
                    print("_" * 70)
                else:
                    sum = 0
                    print("You Have Bought : \n")
                    for i in range(len(shopping_list)):
                        item = list(shopping_list.keys())[i]
                        quantity = list(shopping_list.values())[i]
                        shopping_list[item] = fruits_list[item] * quantity
                        sum += fruits_list[item] * quantity
                        print(i + 1, ".", item, " " * (10 - len(item)), "Quantity : ", quantity,
                              "Kg", " " * 5
                              , " Total Price :", shopping_list[item])
                    print("\nThe Final Cost : ", sum)
                    print("_" * 70)
            elif customer_choice == '4':
                print("_" * 70)
                break
    # ----------------------------------------------------------------------------------------------------------

    # Owner Mode------------------------------------------------------------------------------------------------
    elif mode == "2":
        print("\t\t\t\t\t\tWelcome Owner!\n\n")
        i = 3
        while i:
            print("Enter Your Password To Continue: ", end='')
            password = 1111
            user_inp_pass = int(input())
            if user_inp_pass != password:
                print("_" * 70)
                i -= 1
                print(" " * 20, "Wrong Password!! Try Again!!\n", " " * 20, i, " Attempts Remaining.")
                print("_" * 70)
            else:
                print("_" * 70)
                while 1:
                    print("1.To View List Products:       Press 1.\n"
                          "2.To Add A New Product:        Press 2.\n"
                          "3.To Change Product's Price:   Press 3.\n"
                          "4.To Delete A Product:         Press 4.\n"
                          "5.To Exit To Previous Menu:    Press 5.\n")
                    owner_choice = input("Your Choice : ")
                    if owner_choice == '1':
                        print("_" * 70, "\nOur Products Are : ")
                        for i in range(len(fruits_list)):
                            item = list(fruits_list.keys())[i]
                            price = list(fruits_list.values())[i]
                            print((i + 1), ".", item, " " * (20 - len(item)), "Price: ", price, "LE")
                        print("_" * 70)
                    elif owner_choice == '2':
                        print("_" * 70)
                        new_prod = input("Enter New Product         : ")
                        new_prod_price = float(input("Enter The Product's Price : "))
                        fruits_list[new_prod] = new_prod_price
                        print(" " * 20, "Done!!")
                        print("_" * 70)
                    elif owner_choice == '3':
                        print("_" * 70)
                        prod = input("Enter Product Name            : ")
                        new_price = float(input("Enter The Product's New Price : "))
                        fruits_list[prod] = new_price
                        print(" " * 20, "Done!!")
                        print("_" * 70)
                    elif owner_choice == '4':
                        print("_" * 70)
                        prod = input("Enter Product Name     : ")
                        fruits_list.pop(prod)
                        print(" " * 20, "Done!!")
                        print("_" * 70)
                    elif owner_choice == '5':
                        print("_" * 70)
                        break
            if user_inp_pass == password:
                break
    # ----------------------------------------------------------------------------------------------------------

    elif mode == "3":
        print(" " * 30, "Bye Bye !!")
        print("_" * 70)
        break
