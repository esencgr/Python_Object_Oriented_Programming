from city_and_weather import list_of_cities, get_weather_state
from datetime import datetime,timedelta
from random import randint

class Cities:
    def __init__(self, name):
        self.__name = name
        self.__weather = get_weather_state()

    def get_name(self):
        return self.__name
    
    def get_weather(self):
        return self.__weather

    def city_information(self):
        return f"{self.__name} weather: {self.__weather}"

class Flight:
    def __init__(self, from_city : Cities, to_city : Cities, date : datetime):
        self.from_city = from_city
        self.to_city = to_city
        self.date = date

    def delay(self, delay_time):
        self.date += timedelta(minutes = delay_time) 

class Passenger:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Ticket:
    def __init__(self, passenger : Passenger, flight : Flight, ticket_no : str):
        self.passenger = passenger
        self.flight = flight
        self.ticket_no = ticket_no
    
    def __str__(self):
        ticket_info = (f"""

        NAME:      {self.passenger.name}
        SURNAME:   {self.passenger.surname}
        FROM:      {self.flight.from_city}
        TO:        {self.flight.to_city} 
        DATE:      {self.flight.date}
        TICKET NO: {self.ticket_no} 
                
        """)
        return ticket_info
    
class Pegasus:
    def __init__(self):
        self.active_tickets = list()
        self.passive_tickets = list()
        self.active_flights = list()
        self.passive_flights = list()

    def create_flights(self, from_city : Cities, to_city : Cities, date : datetime):
        flight = Flight(from_city, to_city, date)
        self.active_flights.append(flight)
        return flight

    def get_ticket(self, passenger : Passenger, flight : Flight, ticket_no : str):
        if flight in self.active_flights:
            ticket = Ticket(passenger, flight, ticket_no)
            self.active_tickets.append(ticket)
            return ticket
    
    def del_ticket(self, ticket : Ticket):
        if ticket in self.active_tickets():
            self.passive_tickets.append(ticket)
            self.active_tickets.remove(ticket)
            return self.passive_tickets

    def done_flight(self, flight: Flight):
        print(f"{flight.from_city} -> {flight.to_city} flight is done!")
        for flight in self.active_flights:
            if ticket.flight == flight:
                self.passive_tickets.append(ticket)
                self.active_tickets.remove(ticket)
        self.active_flights.remove(flight)
        self.passive_flights.append(flight)
        

    def show_active_tickets(self):
        for i in range(0,len(self.active_tickets)):
            print("\nactive tickets : ", self.active_tickets[i])

    def show_passive_tickets(self):
        for i in range(0,len(self.passive_tickets)):
            print("\npassive tickets : ", self.passive_tickets[i])

    # def show_active_flights(self):
    #     for i in range(0,len(self.active_flights)):
    #         print("\nactive flights : ", self.active_flights[i])

    # def show_passive_flights(self):
    #     for i in range(0,len(self.passive_flights)):
    #         print("\npassive_flights : ", self.passive_flights[i])

if __name__ == "__main__":
    
    pegasus = Pegasus()

    flight_1 = pegasus.create_flights(Cities("İzmir").get_name(), Cities("İstanbul").get_name(), datetime(2021, 3, 11, 23, 40))
    # pegasus.show_active_flights()
    
    passenger_1 = Passenger("Cagri","Esen")
    ticket = pegasus.get_ticket(passenger_1, flight_1, "1")
    print(ticket)
    print("the weather that you want go : ", Cities("İstanbul").get_weather())

    pegasus.show_active_tickets()
    # pegasus.done_flight(flight_1)
    pegasus.show_passive_tickets()


    

