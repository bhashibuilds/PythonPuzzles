# Factorial 

def factorial(n):
    # Base case: n = 0 or 1
    # The base case is 0 or 1 because those are the final most simplest cases that can be used for recursive steps 
    if n <= 1:
        return 1
    # Recursive case: n! = n * (n - 1)!
    return n * factorial(n - 1)

# Reverse Linked List 