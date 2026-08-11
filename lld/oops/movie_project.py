"""
Create a class Movie with the following:

Attributes:
movie_name -> name of the movie
total_seats -> total seats available in the theatre
ticket_price -> price per ticket
booked_seats -> starts at 0

Methods:
book_ticket(num_tickets) -> books the given number of tickets.
If enough seats are available, confirm the booking and show the
total amount to pay. If not, show:
"Sorry, not enough seats available"

show_status() -> displays the movie name, seats available,
and seats booked so far.
"""


class Movie:

    # Constructor / initializer
    def __init__(self, m_name: str, t_seats: int, tk_price: int):

        # Store the movie name
        self.movie_name = m_name

        # Store the total number of seats
        self.total_seats = t_seats

        # Store the price of one ticket
        self.ticket_price = tk_price

        # Initially, no seats have been booked
        self.booked_seats = 0

    # Method to book tickets
    def book_ticket(self, num_tickets: int):

        # Calculate the total amount for the requested tickets
        total_amount = num_tickets * self.ticket_price

        # Check whether enough seats are available
        if num_tickets > self.total_seats - self.booked_seats:
            print("Sorry, not enough seats available")

        else:
            # Increase the number of booked seats
            self.booked_seats += num_tickets

            # Decrease the number of available seats
            self.total_seats -= num_tickets

            # Confirm the booking and show the total amount
            print(f"Confirm the booking and pay {total_amount}")

    # Method to display the current movie status
    def show_status(self) -> None:

        # Display the movie name
        print(f"Movie Name : {self.movie_name}")

        # Display the number of available seats
        print(f"Seats Available : {self.total_seats}")

        # Display the number of booked seats
        print(f"Total Booked : {self.booked_seats}")


# Create a Movie object
movie = Movie("Spiderman - Brand New Day", 100, 1200)

# Display the initial status
movie.show_status()

# Book 8 tickets
movie.book_ticket(8)

# Display the updated status
movie.show_status()