# Simple Bus Ticket Booking System for Beginners

journeys = []
bookings = []

def add_journey():
    print("\n--- Add Bus Journey ---")
    source = input("Enter source city: ")
    destination = input("Enter destination city: ")
    date = input("Enter date (DD-MM-YYYY): ")
    time = input("Enter time (HH:MM): ")
    price = int(input("Enter ticket price (INR): "))
    seats = int(input("Enter total seats: "))
    journey = [source, destination, date, time, price, seats]
    journeys.append(journey)
    print("Journey added successfully!")

def view_journeys():
    print("\n--- Available Bus Journeys ---")
    if len(journeys) == 0:
        print("No journeys available.")
    else:
        for j in journeys:
            print("From:", j[0], "To:", j[1], "| Date:", j[2], "| Time:", j[3], "| Price: ₹", j[4], "| Seats left:", j[5])

def book_ticket():
    print("\n--- Book Bus Ticket ---")
    source = input("Enter source city: ")
    destination = input("Enter destination city: ")
    date = input("Enter journey date (DD-MM-YYYY): ")
    match = False

    for j in journeys:
        if j[0] == source and j[1] == destination and j[2] == date:
            match = True
            if j[5] <= 0:
                print("No seats available.")
                return
            name = input("Enter your name: ")
            seats_required = int(input("How many seats do you want to book?: "))
            if seats_required > j[5]:
                print("Only", j[5], "seats available.")
                return
            total_price = seats_required * j[4]
            print("Total Price: ₹", total_price)

            print("Choose Payment Method:")
            print("1. Cash\n2. UPI\n3. Card")
            payment_choice = input("Enter choice (1/2/3): ")
            if payment_choice == '1':
                payment_method = "Cash"
            elif payment_choice == '2':
                payment_method = "UPI"
            elif payment_choice == '3':
                payment_method = "Card"
            else:
                print("Invalid payment method.")
                return

            booking = [name, source, destination, date, seats_required, total_price, payment_method]
            bookings.append(booking)
            j[5] -= seats_required
            print("Ticket booked successfully for", name)
            print("Amount Paid: ₹", total_price, "via", payment_method)
            return

    if not match:
        print("No matching journey found.")

def view_bookings():
    print("\n--- All Bookings ---")
    if len(bookings) == 0:
        print("No bookings made yet.")
    else:
        for b in bookings:
            print("Name:", b[0], "| From:", b[1], "To:", b[2], "| Date:", b[3], "| Seats:", b[4], "| Paid: ₹", b[5], "| Method:", b[6])

# Main Menu
while True:
    print("\n======== Bus Ticket Menu ========")
    print("1. Add Journey")
    print("2. View Journeys")
    print("3. Book Ticket")
    print("4. View Bookings")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_journey()
    elif choice == '2':
        view_journeys()
    elif choice == '3':
        book_ticket()
    elif choice == '4':
        view_bookings()
    elif choice == '5':
        print("Thanks for using Bus Ticket Booking System!")
        break
    else:
        print("Invalid choice. Enter number between 1 to 5.")
