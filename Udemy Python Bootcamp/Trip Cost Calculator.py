print("Welcome to the Trip Cost Calculator!")
days = int(input("How many days will you stay? "))
hotelCost = float(input("How much does hotel cost per night? £"))
flightCost = float(input("How much does flight cost? £"))
rentalCar = float(
    input("If you need rental car please enter the price otherwise enter zero. £"))
expenses = float(input("Enter other possible expenses £"))
cost = (hotelCost + flightCost + rentalCar + expenses) * days
print("Total Cost: £", round(cost, 2))
