class Train:
    def __init__(self, train_id, name, seats):
        self.train_id = train_id
        self.name = name
        self.seats = seats
        self.booked_seats = 0
    def get_available_seats(self):
        if(self.booked_seats>0):
            print("seats are available")
        else:
            print("seats are not available")
    def book_seat(self):
        user=int(input("enter a no of seats u want to booked:"))
        self.booked_seats=self.booked_seats+user
    def cancel_seat(self):
        user2=int(input("enter a no of seats u want to cancle:"))
        self.booked_seats=self.booked_seats-user2
    def display_train_info(self):
        print(f"Train ID: {self.train_id}, Name: {self.name},Available Seats:{self.booked_seats}")
# 
class Person:
    def __init__(self, name, age, gender): 
        self.name = name
        self.age = age
        self.gender = gender
class Passenger(Person):
    def __init__(self, name, age, gender, pnr, train_id, timestamp):
        super().__init__(name, age, gender)
        self.pnr = pnr  
        self.train_id = train_id
        self.timestamp = timestamp
    def display_passenger_info(self):
        print((f"PNR: {self.pnr}, Name: {self.name}, Age: {self.age}, Gender:{self.gender},"
        f"Train ID: {self.train_id}, Booking Time: {self.timestamp}"))
obj1 = Train(123,"prachi",2)
obj1.book_seat()
obj1.cancel_seat()
obj1.get_available_seats()
obj1.display_train_info()
# 
obj = Passenger("prachi",19,"female",888,1111,'2pm')
obj.display_passenger_info()