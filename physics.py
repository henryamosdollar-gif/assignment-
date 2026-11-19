# Physics Operations Using Functions
def speed():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    result = distance / time
    print("Speed =", result, "m/s")
def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    result = mass * acceleration
    print("Force =", result, "N")
def acceleration():
    velocity = float(input("Enter final velocity (m/s): "))
    initial = float(input("Enter initial velocity (m/s): "))
    time = float(input("Enter time (s): "))
    result = (velocity - initial) / time
    print("Acceleration =", result, "m/s²")
def work():
    force_value = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))
    result = force_value * distance
    print("Work done =", result, "J")
def power():
    work_done = float(input("Enter work done (J): "))
    time = float(input("Enter time (s): "))
    result = work_done / time
    print("Power =", result, "W")
# Infinite While Loop
while True:
    print("\n===== PHYSICS OPERATIONS =====")
    print("1. Calculate Speed")
    print("2. Calculate Force")
    print("3. Calculate Acceleration")
    print("4. Calculate Work Done")
    print("5. Calculate Power")
    choice = input("Select an operation (1-5): ")
    try:
        if choice == "1":
            speed()
        elif choice == "2":
            force()
        elif choice == "3":
            acceleration()
        elif choice == "4":
            work()
        elif choice == "5":
            power()
        else:
            print("Invalid selection!")
    except ValueError:
        print("Please enter valid numbers.")
    again = input(
        "\nDo you want to continue? (yes/no): "
    ).lower()
    if again != "yes":
        print("Thank you for using the Physics Calculator!")
        break