class BookingError(Exception):
# """Raised when train ID is invalid or no seat is available"""
    pass
class PNRNotFoundError(Exception):
# """Raised when PNR is invalid"""
    pass