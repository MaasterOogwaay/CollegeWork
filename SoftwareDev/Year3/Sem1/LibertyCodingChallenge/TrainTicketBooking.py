import math

seats = [0] * 10  # 10 seats available


def menu():
    running = True
    while running:
        print("Welcome to Train Ticket Booking System ")
        print("1. Book a ticket")
        print("2. View available seats")
        print("3. Exit")
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
        except:
            print("Invalid input, please enter a number.")
            continue

        if choice == 1:
            book_ticket()
        elif choice == 2:
            view_seats()
        elif choice == 3:
            running = False
            print("Thank you for using Train Ticket Booking System")
        else:
            print("Invalid choice, please try again")

def book_ticket_choice():
    running = True
    while running:
        print("Choose class type ")
        print("1. Book a standard ticket")
        print("2. Book a first class ticket")
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
        except:
            print("Invalid input, please enter a number.")
            continue

        if choice == 1:
            book_ticket()
        elif choice == 2:
            book_first_class_ticket()
            print("Thank you for using Train Ticket Booking System")
        else:
            print("Invalid choice, please try again")

def book_first_class_ticket():


def book_ticket():
    num_tickets = input("Enter number of tickets to book (max 4 per transaction): ")

    try:
        num_tickets = int(num_tickets)
    except:
        print("Invalid input, please enter a number.")
        return



    # if math.isnan(num_tickets):
    #     print("Please enter a integer value")
    #     return

    if num_tickets < 1 or num_tickets > 4:
        print("Invalid number of tickets, please try again")
        return

    total_tickets = 0
    # if num_tickets == total_tickets:
    #     print("No seats left")
    #     return
    # else:
    #     total_tickets += num_tickets
    for i in range(len(seats)):
        if seats[i] == 1:
            total_tickets += 1

    if total_tickets + num_tickets >= 10:
        print("No seats remaining")
        return


    total_cost = num_tickets * 100  # €100 per ticket
    print(f"Total cost is €{total_cost}")

    confirm = input("Enter 1 to confirm booking or any other key to cancel: ")

    try:
        confirm = int(confirm)
    except:
        print("Invalid input, booking cancelled")
        return

    if confirm == 1:
        seats_booked = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                seats[i] = 1
                seats_booked += 1

                print(f"Seat {i+1} booked successfully")

                if seats_booked == num_tickets:
                    break
        print("Tickets booked successfully!")
    else:
        print("Booking cancelled")


def view_seats():
    print("Available Seats:")
    for i in range(len(seats)):
        if seats[i] == 0:
            print(f"Seat {i+1} is available")


menu()
