def unit_converter():
    print("Welcome to the Unit Converter!")
    print("Select the type of conversion:")
    print("1) Length")
    print("2) Temperature")
    choice = input("Enter your choice (1/2): ")
    if choice == '1':
        length_converter()
    elif choice == '2':
        temperature_converter()
    else:
        print("Invalid choice. Please try again.")
        unit_converter()

def length_converter():
    print("1) meter to kilometer")
    print("2) kilometer to meter")
    choice = input("Enter your choice (1/2): ")
    if choice == '1':
        meter_to_kilometer()
    elif choice == '2':
        kilometer_to_meter()
    else:
        print("Invalid choice. Please try again.")
        length_converter()

def temperature_converter():
    print("1) Celsius to Fahrenheit")
    print("2) Fahrenheit to Celsius")
    choice = input("Enter your choice (1/2): ")
    if choice == '1':
        celsius_to_fahrenheit()
    elif choice == '2':
        fahrenheit_to_celsius()
    else:
        print("Invalid choice. Please try again.")
        temperature_converter()

def meter_to_kilometer():
    m = float(input("Enter meters: "))
    km = m / 1000
    print("Answer:", km, "km")

def kilometer_to_meter():
    km = float(input("Enter kilometers: "))
    m = km * 1000
    print("Answer:", m, "m")

def celsius_to_fahrenheit():
    c = float(input("Enter Celsius: "))
    f = c * 9 / 5 + 32
    print("Answer:", f, "F")

def fahrenheit_to_celsius():
    f = float(input("Enter Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("Answer:", c, "C")

unit_converter()