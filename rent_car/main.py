from rent_veh import Car, Byc, Customer

car = Car(10)
byc = Byc(100)
customer = Customer()
main_menu = True

while True:

    if main_menu:
        print(  """
                ----------------- RENT A VEHİCLE -----------------   
                B - Bicycle Menu
                C - Car Menu
                Q - Quit
                """ )

        main_menu = False

        choise = input("Enter your choise : ")

    if choise == 'B' or choise == 'b':
        print(  """
                ----------------- BYCICLE MENU -----------------   
                1 - Display available bikes
                2 - Rent bike for hourly basis $5
                3 - Rent bike for daily basis $84
                4 - Return bike
                5 - Main menu
                6 - Exit    
                """ )
                
        choise = input("Enter your choise for bycicle : ")

        if choise == "1":
            byc.display_stock()
            choise = 'B'

        elif choise == "2":
            customer.rental_time_b = byc.rent_hourly(customer.request_vehicle("byc"))
            customer.rental_basis_b = 1
            main_menu = True
            print("-----------------------------")

        elif choise == "3":
            customer.rental_time_b = byc.rent_daily(customer.request_vehicle("byc"))
            customer.rental_basis_b = 2
            main_menu = True
            print("-----------------------------")

        elif choise == "4":
            customer.bill = byc.return_vehicle(customer.return_vehicle("byc"), "byc")
            customer.rental_basis_b, customer.rental_time_b, customer.bycs = 0, 0, 0
            main_menu = True

        elif choise == "5":
            main_menu = True

        elif choise == "6":
            break 

        else:
            print("Invalid Input !")
            main_menu = True

    elif choise == 'C' or choise == 'c':
        print(  """
                ----------------- CAR MENU -----------------   
                1 - Display available cars
                2 - Rent car for hourly basis $10
                3 - Rent car for daily basis $192
                4 - Return car
                5 - Main menu
                6 - Exit    
                """ )
                
        choise = input("Enter your choise for car: ")

        if choise == "1":
            car.display_stock()
            choise = 'C'

        elif choise == "2":
            customer.rental_time_c = car.rent_hourly(customer.request_vehicle("car"))
            customer.rental_basis_c = 1
            main_menu = True
            print("-----------------------------")

        elif choise == "3":
            customer.rental_time_c = car.rent_daily(customer.request_vehicle("car"))
            customer.rental_basis_c = 2
            choise = 'C'
            print("-----------------------------")

        elif choise == "4":
            customer.bill = car.return_vehicle(customer.return_vehicle("car"), "car")
            customer.rental_basis_c, customer.rental_time_c, customer.cars = 0, 0, 0
            main_menu = True

        elif choise == "5":
            main_menu = True

        elif choise == "6":
            break 

        else:
            print("Invalid Input !")
            main_menu = True

    elif choise == 'Q' or choise == 'q':
        print("Quitting")        
        break
 
    else:
        print("Input must be B - C - Q!")
        main_menu = True
    
print("THANK YOU..")