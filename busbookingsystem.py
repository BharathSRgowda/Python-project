print("\n🪷__WELLCOME TO 🔴🟡__🇰 🇸 🇷 🇹 🇨__🔴🟡 BUS🚌 BOOKING SYSTEM__🪷")
Next_proceed=input("\n WOULD YOU LIKE TO CONTINUE(YES/NO) :")
if Next_proceed.lower()=="yes":
    print("")

else:
    
    
 while  True:
    
    if False:
        break 

print("\nCHECK YOUR TICKET PRICE BY ENTERING YOUR PERSONAL DETAILS")

Name=input("\nEnter your Name :").upper()
Gender=input("Enter the GENDER(M/F):" )
passenger=input("Enter (YES/NO) if you are a staff : ")
staff_id=(input("Enter staff id :"))
age =int(input("Enter the age :"))


if Gender== "F"or Gender=="f":
    print("\n Ticket is Free ( SHAKTHI YOJANE )".upper())
else:
    if age<=5:
        print("\nTicket is free ( LESS THAN 6 YEARS )".upper())
    elif age<=12:
        print(" \nYou'll get child discount (PAY HALF OF PRICE)".upper())
    elif age>=60:
        print("\nYou'll get senior citizen discount (PAY 75% OF PRICE)".upper())
    elif passenger=="yes"and (staff_id):
        print("\nTicket is free")    
    else:
        print("\nYou have to pay full price".upper())
        print("\n PLEASE SELECT BELOW OPTIONS TO BOOK YOUR SEATS..")
class Bus:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.seats = [False] * total_seats  # False means the seat is available

    def display_seats(self):
        print("Seat Status:")
        for i in range(self.total_seats):
            status = "Available" if not self.seats[i] else "Booked"
            print(f"Seat {i + 1}: {status}")

    def book_seat(self, seat_number):
        if 1 <= seat_number <= self.total_seats:
            if not self.seats[seat_number - 1]:
                self.seats[seat_number - 1] = True
                print(f"\n Dear, {Name} . Your Seat No.{seat_number}. has been booked successfully.✅")
                print(" \nTHANKS FOR BOOKING YOUR'S SEAT'S . HAVE A NICE DAY 😊")
            else:
                print(f" This Seat {seat_number} is already booked.Please select unoccupied seats")
        else:
            print("Invalid seat number.")
    

    def cancel_booking(self, seat_number):
        if 1 <= seat_number <= self.total_seats:
            if self.seats[seat_number - 1]:
                self.seats[seat_number - 1] = False
                print(f"Dear {Name}.Booking for seat {seat_number} has been canceled.")
            else:
                print(f"Seat {seat_number} is not booked.")
        else:
            print("Invalid seat number.")
            
def main():
    bus = Bus(total_seats=10)  # Create a bus with 10 seats
    while True:
        print("\n1. Display Seats")
        print("2. Book Seat")
        print("3. Cancel Booking")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            bus.display_seats()
        elif choice == '2':
            seat_number = int(input("Enter seat number to book: "))
            bus.book_seat(seat_number)
        elif choice == '3':
            seat_number = int(input("Enter seat number to cancel: "))
            bus.cancel_booking(seat_number)
        elif choice == '4':
            print("🪷__THANKS FOR VISITING 🔴🟡__🇰 🇸 🇷 🇹 🇨__🔴🟡 BUS🚌 BOOKING SYSTEM__🪷".upper())
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()