from datetime import datetime

hotel = {
    "BASIC": {"total_rooms": 500, "available": 500, "rate": 79.99},
    "FAMILY": {"total_rooms": 400, "available": 400, "rate": 99.99},
    "SUITE": {"total_rooms": 200, "available": 200, "rate": 150},
    "PENTHOUSE": {"total_rooms": 40, "available": 40, "rate": 450}
}

room_bookings = {room_type: [] for room_type in hotel}

def welcome():
    today = datetime.date.today().strftime('%m-%d-%Y')
    print("*" * 20)
    print(f"Welcome to the Hotel Reservation System, today's date is {today}, we look forward to helping you!")
    print("*" * 20)
welcome()

def available_rooms():
    print("-" * 16)
    print("Available Rooms: ")
    for room_type, details in hotel.items():
        print(f"{room_type}: {details['available']} available, Rate: ${details['rate']}/night")

def room_available(room_type, check_in, check_out):
    for booking in room_bookings[room_type]:
        if not (check_out <= booking["check_in"] or check_in >= booking["check_out"]):
            return False
    return True

def booking_room():
    room_type = input("Which room do you want?: ").upper()
    nights = int(input("How many nights will you be staying?: "))

    check_in_year = int(input("Enter check-in year (YYYY): "))
    check_in_month = int(input("Enter check-in month (MM): "))
    check_in_day = int(input("Enter check-in day (DD): "))
    check_in_date = datetime.strftime(check_in_month+"/"+check_in_day+"/"+check_in_year)


    check_out_date = check_in_date + datetime.timedelta(days = nights)

    if room_type in hotel and hotel[room_type]['available'] > 0:
        if room_available(room_type, check_in_date, check_out_date):
            hotel[room_type]['available'] -= 1
            room_bookings[room_type].append({"check_in": check_in_date, "check_out": check_out_date})
            total_cost = hotel[room_type]['rate'] * nights
            print(f"\nBooking successful! The {room_type} room is booked from {check_in_date} to {check_out_date}.")
            print(f"Total cost: ${total_cost:.2f}")
        else:
            print(f"No availability for the selected dates.")
    else:
        print(f"Sorry, {room_type} rooms are not available.")

    if input("See updated availability (Y/N)?: ").upper() == 'Y':
        available_rooms()

available_rooms()
booking_room()
