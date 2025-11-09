import random
from datetime import datetime
class RailwayManagement:
    def __init__(self):
        self.trains = []
        self.passengers = {}
def add_train(self, train):
    self.trains.append(train)
def display_trains(self):
    pass # Loop through trains and print details
def find_train(self,train_id):
 """Find a train by its ID.
Returns the train object if found, else None."""
pass # Loop through self.trains and return the train with matching train_id
def generate_pnr(self, train_id):
    pass # Return formatted PNR: train_id-DDMMYY-RANDOM
def book_ticket(self, train_id, name, age, gender):
        """
    TODO:
1. Find train by train_id.
2. If seats are available, book and generate PNR.
3. If not available, then raise BookingError.
4. Store booking details file (dict with pnr, passenger, train_id, timestamp).
"""
    pass # Full booking flow: check seat, assign, create passenger
def cancel_ticket(self, pnr):
    """
TODO:
1. Find booking by PNR ,if PNR not found raise PNRNotFoundError.
2. Remove booking and increment train's seat count.
"""
    pass # Cancel booking by removing from dict and restoring seat
def get_passengers_by_train(self, train_id):
    """
Get a list of all passengers for a specific train using train_id.
"""
    pass
def check_pnr_status(self, pnr):
    """
TODO:
1. Find booking by PNR.
2. Display details if found, else raise PNRNotFoundError.
"""
    pass
def save_booking_to_file(self, passenger):
    pass # To Do: write booking details to file