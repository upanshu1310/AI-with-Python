'''
1. Create the following get required input from the user until user does not want to add values
User give the details of car like
    Brand
    Model name
    Type
    Model year
    Registration number
    Color
    Value
2. Write the python code to accept following car details (note that user can add multiple car)
3. As soon as user added the cars show the cars who have price more than 500000 rs
4. Show car who have color white
5. Show all cars by mercedes brand
'''

cars = []

# Question 1 and 2
while True:

	car = {}

	brand = input("\n\nBrand: ")
	model = input("Model: ")
	type_of_car = input("Type: ")
	year = int(input("Year: "))
	registration_number = input("Registration Number: ")
	color = input("Color: ")
	value = int(input("Value: "))

	car["brand"] = brand
	car["model"] = model
	car["type"] = type_of_car
	car["year"] = year
	car["registration_number"] = registration_number
	car["color"] = color
	car["value"] = value

	cars.append(car)

	next = input("\nDo you want to add more data? (Y / N):  ")
	if next.upper() == "N":
		break

# Question 3
print("\nCars with price more than Rs. 5,00,000")
for car in cars:
	if car["value"] > 500000:
		print(car)

# Question 4
print("\nWhite colour cars")
for car in cars:
	if car["color"] == "white":
		print(car)

# Question 5
print("\nMercedes brand cars")
for car in cars:
	if car["brand"] == "mercedes":
		print(car)