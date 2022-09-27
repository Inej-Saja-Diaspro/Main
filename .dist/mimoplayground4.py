ingredient = "sugar"
quantity = 100
print(f"Add {quantity} grams of {ingredient}")

ingredient = "chocolate"
quantity = 150
print(f"Add {quantity} grams of {ingredient}")

ingredient = "flour"
quantity = 300
print(f"Add {quantity} grams of {ingredient}")

print("-----")
print("next test:")
print(" ")

hours = 14
minutes = 45
destination = "Paris"

print(f"Your flight to {destination} takes off in {hours}:{minutes}")

print("-----")
print("next test:")
print(" ")

name = "Kim"
greeting = f"Good morning, {name}"

print(greeting)

print("-----")
print("next test:")
print(" ")

ride_type = "Black"
credits = 4

ride_price = 0
final_price = 0

if ride_type == "DoorberX":
    ride_price = 20.5
elif ride_type == "Black":
    ride_price = 37.9
else:
    ride_price = 18.7

print("Ride price:")
print(ride_price)

if credits > 0:
    final_price = ride_price - credits

print("Final price:")
print(final_price)