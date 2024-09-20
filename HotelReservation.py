import datetime


hotel = {
    "BASIC":{"total_rooms":500,"available":500,"rate":79.99},
    "FAMILY":{"total_rooms":400,"available":400,"rate":99.99},
    "SUITE":{"total_rooms":200,"available":200,"rate":150},
    "PENTHOUSE":{"total_rooms":40,"available":40,"rate":450}
    }

def available_rooms():
    print("-" * 16)
    print("Available Rooms: ")
    print("=" * 47)
    for room_type, details in hotel.items():
        print(f"{room_type} Rooms: {details['available']} available, Rate: ${details['rate']}/night")
        print("=" * 47)

def booking_room():
    room_type = input("Which room do you want?: ")
    nights = int(input("How many nights will you be staying?: "))
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = (datetime.datetime.strptime(check_in, "%Y-%m-%d") + datetime.timedelta(days=nights)).strftime("%Y-%m-%d")
    if room_type.upper() in hotel:
        room_info = hotel[room_type.upper()]
        if room_available(room_type, check_in, check_out):
            room_info = hotel[room_type]
            if room_info['available'] > 0:
                total_cost = room_info['rate'] * nights
                room_info['available'] -= 1  # Deduct one room from availability
                room_bookings[room_type].append({"check_in": check_in, "check_out": check_out})  # Track booking dates
                print(f"\nBooking successful! The {room_type} room has been booked from {check_in} to {check_out}.")
                print(f"Your total cost will be: ${total_cost:.2f}\n")
            availability = input("Would you like to see updated availability, Y/N?: ")
            if availability.lower() == 'y':
                available_rooms()

available_rooms()
booking_room()
