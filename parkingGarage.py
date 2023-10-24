
class ParkingGarage:
    def __init__(self, total_spaces = 50):
        self.tickets = list(range(1, total_spaces + 1))
        self.parkingSpaces = list(range(1, total_spaces + 1))
        self.currentTicket = {}

    def takeTicket(self):
        
        ticket = self.tickets.pop(0)
        parking_space = self.parkingSpaces.pop(0)
        self.currentTicket = {'ticket': ticket, 'parking_space': parking_space, 'paid': False}
        print(f"Ticket {ticket} issued. Parking space {parking_space} is available.")

    def payParking(self):

        payment = input("Please enter the amount for parking: $")
        if payment:
            print("Payment received. You have 15 minutes to leave the garage.")

    def leaving(self):
        payment = input("Please make a payment before leaving. Enter the payment amount: $")
        if payment:
                self.currentTicket['paid'] = True
                print("Payment received. Thank you for visiting! Have a nice day.")
                

customer = ParkingGarage()

while True:
    print("\nOptions:")
    print("1. Take a ticket")
    print("2. Pay for parking")
    print("3. Leave the garage")
    print("4. Exit")
    choice = input("Select an option (1/2/3/4): ")

    if choice == '1':
            customer.takeTicket()
    elif choice == '2':
            customer.payParking()
    elif choice == '3':
            customer.leaving()
    elif choice == '4':
        break
    else:
        print("Invalid option. Please choose a valid option.")
