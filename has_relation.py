class college:
    def __init__(self):
        self.college_name = "ahmednagar_college "
        self.department = "computer_science"
    def display(self):
        print(self.college_name)
        print(self.department)
class student:
    def __init__(self):
        self.student_name = "prachi"
        self.mobile_no = 92009980758
    def addmision(self,obj):
        self.a = obj

    def print(self):
        print(self.student_name)
        print(self.mobile_no)
        self.a.display()

obj1 = college()
obj2 = student()
obj2.addmision(obj1)
obj2.print()
# library has a book
class book:
    def __init__(self):
        self.book_name = "data communication"
        self.book_author = "reebeca ghorpade"
    def display(self):
        print("book name is :",self.book_name)
        print("book author name is :",self.book_author)
class library:
    def __init__(self):
        self.issue_date = "21-1-2025"
        self.rt_date = "25-1-2025"
    def iss_date(self,p):
        self.a = p 
    def show(self):
        print("book issue date is :",self.issue_date)
        print("book return date is :",self.rt_date)
        self.a.display()

obj2 = book()
obj1 = library()
obj1.iss_date(obj2)
obj1.show()
#class room each room has a room no and ,type ,price,booking status
#if booked or available 
# class guest:room check time,
# guest has a name and contact info,guese can be assign to a available  room
# class hotel:hotel name
# booking():book room
# isavailable():is avaible or not 
# show a lis of all available room
class room:
    def __init__(self):
        self.room_no = 21
        self.room_type="AC"
        self.room_price = 8000
        self.booking_status = "available"
    def display(self):
        print(self.room_no)
        print(self.room_type)
        print(self.room_price)
        print(self.booking_status)
class guest:
    def __init__(self):
        self.guest_name = "prachi"
        self.guest_contact = 78876748567
        self.check_in = "12:00 PM"
        self.check_out = "11:30 AM"
class hotel:
    def __init__(self):
        self.hotel_name = "singh rensidency"
    # def booking(self):
    #     user=int(input("enter a room no :"))

    def is_available(self):
        if(self.booking_status == "booked" or self.booking_status =="BOOKED"):
            print("this room is already booked by someone please check another room")
        else:
            print("the room is available")

obj2 = room()
obj2.display()
guestobj = guest()
ho = hotel()
ho.is_available()

