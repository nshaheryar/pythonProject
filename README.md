# pythonProject requirements

Requirements: Hotel Reservation System - Create a reservation system which books hotel rooms.
It charges various rates for particular types of the hotel.
Hotel rooms have penthouse suites which cost more.
Keep track of when rooms will be available and can be scheduled.

**THIS PROJECT DOES THE FOLLOWING**

Upon running the project1.py file for the first time, several things happen:
  - A database is created (hotel_bookings.db)
  - That database is populated with dummy data filling all but 10 rooms of each room-type
  - The user is shown the available rooms and their respective costs
  - The user will select their preferred room style
  - The user will input the number of nights they intend to stay at the hotel
  - The user will input the check-in date for their stay

Once these actions are completed, the user is informed their booking was successful and is asked if they would like a receipt
If they type 'y' to accept, their booking details are printed out [Roomtype, checkin/checkout, and cost]

4 types of rooms exist: Basic, Family, Suite, and Penthouse
Each room has a unique number available and an individual cost

A user can book the room for whatever dates they wish (as long as it's not in the past)
The system will inform the user prior to booking how many of each room-type is available
Once the user selects a room-type and a date, the system will inform them if it's available
If unavailable, the system presents the next date that style room is available for the specified duration
Once the user determines an acceptable date range per their requested room, they can book it
Upon booking, the user is prompted with the option to accept or decline a receipt
There are various levels of error handling in place to prevent the user from entering false dates or an incorrect room
After booking (and when checking availability before), the database is updated to include the user's booking. 
