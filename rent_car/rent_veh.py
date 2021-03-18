import datetime as date

class Vehicle_Rent:
    def __init__(self,stock):
        self.stock = stock

    def display_stock(self):
        print(f"stock is : {self.stock}")
        return self.stock
        
    def rent_hourly(self, n):
        if n <= 0:
            print("number should be positive ")
            return None
        
        elif n >= self.stock:
            print(f"Stock has not enough car. Avalibale car number : {self.stock} ")
            return None

        else:
            self.time = date.datetime.now()
            print(f"Rented {n} vehicle for hourly at {self.time.hour}")
            self.stock -= n 
            return self.time

    def rent_daily(self, n):
        if n <= 0:
            print("number should be positive ")
            return None
        
        elif n >= self.stock:
            print(f"Stock has not enough car. Avalibale car number : {self.stock} ")
            return None

        else:
            self.time = date.datetime.now()
            print(f"Rented {n} vehicle for daily at {self.time.hour}")
            self.stock -= n 
            return self.time

    def return_vehicle(self, request, brand): 
        # return a bill according to daily or hourly
        car_h_price = 10
        car_d_price = car_h_price * 8 / 10 * 24
        byc_h_price = 5
        byc_d_price = byc_h_price * 7 / 10 * 24
        
        rental_time, rental_basis, number_vehicle = request
        bill = 0

        if brand == "car":
            if rental_time and rental_basis and number_vehicle:
                self.stock += number_vehicle
                current_time = date.datetime.now()
                rental_period = current_time - rental_time

                if rental_basis == 1:  # hourly rent
                    bill = rental_period.seconds / 3600 * number_vehicle * car_h_price
                
                elif rental_basis == 2:  # daily rent
                    bill = rental_period.seconds / (3600 * 24) * number_vehicle * car_d_price

                if number_vehicle > 2:   # discount for more than two car
                    print("You have extra %20 discount")
                    bill *= 0.8
                
                print(f"Your price : $ {bill}")
                return bill 

        elif brand == "byc":
            if rental_time and rental_basis and number_vehicle:
                self.stock += number_vehicle
                current_time = date.datetime.now()
                rental_period = current_time - rental_time

                if rental_basis == 1:  # hourly rent
                    bill = rental_period.seconds / 3600 * number_vehicle * byc_h_price
                
                elif rental_basis == 2:  # daily rent
                    bill = rental_period.seconds / (3600 * 24) * number_vehicle * byc_d_price

                if number_vehicle > 4:   # discount for more than two car
                    print("You have extra %20 discount")
                    bill *= 0.8
                
                print(f"Your price : $ {bill}")
                return bill 
        else :
            print("You dont use any vehicle.")


# child classes
class Car(Vehicle_Rent):
    def __init__(self, stock):
        super().__init__(stock)

    def discount(self, b):
        bill -= (b * 15) / 100
        return bill 

class Byc(Vehicle_Rent):
    def __init__(self, stock):
        super().__init__(stock)
        
class Customer:
    def __init__(self):
        self.cars = 0
        self.rental_basis_c = 0
        self.rental_time_c = 0

        self.bycs = 0
        self.rental_basis_b = 0
        self.rental_time_b = 0
    
    def request_vehicle(self, brand):
        # take a request for a car or bycle 
        if brand == "car":
            car_n = input("How many car would you rent ?")

            try:
                car_n = int(car_n)

            except ValueError:
                print("Number of car should be a number !")
                return -1 

            if car_n < 1:
                print("Number of car should be greater than zero")
                return -1

            else:
                self.cars = car_n
                return self.cars

        elif brand == "byc":
            byc_n = input("How many byc would you rent ?")

            try:
                byc_n = int(byc_n)

            except ValueError:
                print("Number of byc should be a number !")
                return -1 

            if byc_n < 1:
                print("Number of byc should be greater than zero")
                return -1

            else:
                self.bycs = byc_n
                return self.bycs
        
        else:
            print("request vehicle error")

    def return_vehicle(self, brand):
        if brand == "car":
            if self.rental_time_c and self.rental_basis_c and self.cars:
                return self.rental_time_c, self.rental_basis_c, self.cars
            else: 
                return 0, 0, 0
        
        elif brand == "byc":
            if self.rental_time_b and self.rental_basis_b and self.bycs:
                return self.rental_time_b, self.rental_basis_b, self.bycs
            else: 
                return 0, 0, 0		
        else:
            print("Return vehicle error !")


