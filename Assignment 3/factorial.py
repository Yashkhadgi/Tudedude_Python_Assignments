def factorial(n):
    if n < 0:
        return " Enter a positive number "
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        
        return result 


sample_no = 5

output = factorial(sample_no) 
print(f"The factorial of {sample_no} is: {output}")