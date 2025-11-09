# #models.py
# class Train:
# def __init__(self, train_id, name, seats):
# self.train_id = train_id
# self.name = name
# self.seats = seats
# self.booked_seats = 0
# def get_available_seats(self):
# pass # To Do: return True if seats > 0
# def book_seat(self):
# pass # To Do: reduce seat by 1 if available
# def cancel_seat(self):
# pass # To Do: increase seat by 1
# def display_train_info(self):
# return f"Train ID: {self.train_id}, Name: {self.name}, Available Seats: 
# {self.get_available_seats()}"
# class Person:
# def __init__(self, name, age, gender):
# self.name = name
# self.age = age
# self.gender = gender
# class Passenger(Person):
# def __init__(self, name, age, gender, pnr, train_id, timestamp):
# super().__init__(name, age, gender)
# self.pnr = pnr
# self.train_id = train_id
# self.timestamp = timestamp
# def display_passenger_info(self):
# return (f"PNR: {self.pnr}, Name: {self.name}, Age: {self.age}, Gender: 
# {self.gender}, "
# f"Train ID: {self.train_id}, Booking Time: {self.timestamp}")
# #exceptions.py
# class BookingError(Exception):
# """Raised when train ID is invalid or no seat is available"""
# pass
# class PNRNotFoundError(Exception):
# """Raised when PNR is invalid"""
# pass
# #management.py
# import random
# from datetime import datetime
# class RailwayManagement:
# def __init__(self):
# self.trains = []
# self.passengers = {}
# def add_train(self, train):
# pass # Add new Train to self.trains
# def display_trains(self):
# pass # Loop through trains and print details
# def find_train(self, train_id):
# """ Find a train by its ID.
# Returns the train object if found, else None."""
# pass # Loop through self.trains and return the train with matching train_id
# def generate_pnr(self, train_id):
# pass # Return formatted PNR: train_id-DDMMYY-RANDOM
# def book_ticket(self, train_id, name, age, gender):
# """
# TODO:
# 1. Find train by train_id.
# 2. If seats are available, book and generate PNR.
# 3. If not available, then raise BookingError.
# 4. Store booking details file (dict with pnr, passenger, train_id, timestamp).
# """
# pass # Full booking flow: check seat, assign, create passenger
# def cancel_ticket(self, pnr):
# """
# TODO:
# 1. Find booking by PNR ,if PNR not found raise PNRNotFoundError.
# 2. Remove booking and increment train's seat count.
# """
# pass # Cancel booking by removing from dict and restoring seat
# def get_passengers_by_train(self, train_id):
# """
# Get a list of all passengers for a specific train using train_id.
# """
# pass
# def check_pnr_status(self, pnr):
# """
# TODO:
# 1. Find booking by PNR.
# 2. Display details if found, else raise PNRNotFoundError.
# """
# pass
# def save_booking_to_file(self, passenger):
# pass # To Do: write booking details to file