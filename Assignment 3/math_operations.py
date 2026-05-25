import math

def perform_calculations():
    try:
        user_input = float(input("Enter a positive number: "))
        
        if user_input <= 0:
            print("Enter a number greater than 0")
            return
            
       
        sqrt_val = math.sqrt(user_input)
        log_val = math.log(user_input)
        sine_val = math.sin(user_input)

        print(f"Square Root of {user_input}: {sqrt_val}")
        print(f"Natural Logarithm of {user_input}: {log_val}")
        print(f"Sine of {user_input}: {sine_val}")
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")


perform_calculations()