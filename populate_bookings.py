import sqlite3
import datetime
import random

def populate_bookings(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    #matches the columns with the rooms table & determines how far in advance you want to populate the table from today
    room_types = ["BASIC", "FAMILY", "SUITE", "PENTHOUSE"]
    days_to_book = 30


    for i in range(days_to_book):
        check_in_date = (datetime.datetime.now() + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        for room_type in room_types:
            
            #populates the current available rooms for a specific room type
            cursor.execute("SELECT available FROM rooms WHERE room_type = ?", (room_type,))
            available_rooms = cursor.fetchone()[0]

            #always leaves at least 10 rooms open for each room type ('max' does this dynamically independent of room totals)
            max_bookings = max(0, available_rooms - 10)
            
            #randomly determine the number of bookings for this day and room type
            num_bookings = random.randint(0, max_bookings)

            for _ in range(num_bookings):
                #generate a random duration for user's stay
                nights = random.randint(1, 5)
                check_out_date = (datetime.datetime.strptime(check_in_date, "%Y-%m-%d") + datetime.timedelta(days=nights)).strftime("%Y-%m-%d")

                #insert booking into the database
                cursor.execute("INSERT INTO bookings (room_type, check_in, check_out) VALUES (?, ?, ?)",
                            (room_type, check_in_date, check_out_date))
                
                #updates available rooms for the room type
                cursor.execute("UPDATE rooms SET available = available - 1 WHERE room_type = ?", (room_type,))

    #commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Database populated with bookings.")

if __name__ == "__main__":
    populate_bookings('hotel_bookings.db')
