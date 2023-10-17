# Question 5: Write a function generateModifiedFibonacci that generates a modified Fibonacci sequence using recursion of length n (provided as an argument).

# Fibonacci Sequence : The pattern begins after the first two numbers, 0 and 1, where each number in the sequence is always the sum of the two numbers before it.
# You need to identify a pattern from the samples given below and write a function to generate a sequence that follows this given pattern.
# Here are some examples of a ModifiedFibonacci sequence
# generateModifiedFibonacci(4) = [1, 2, 3, 7]
# generateModifiedFibonacci(6) = [1, 2, 3, 7, 22, 155]
# generateModifiedFibonacci(8) = [1, 2, 3, 7, 22, 155, 3411, 528706]


# Note: The base case for this problem is generateModifiedFibonacci(2) = [1,2]
# You need to solve the following problem using recursion, use of loops and other methods will result in point deduction.

def generateModifiedFibonacci(n):
    """
    input: integer n
    output: First n elements of the list based on the given pattern  
    """
    # The observed pattern in that 
    # To get n, we need to multiple n-1 and n-2 and add 1 to it
    # The base case is [1,2]
    
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        prev = generateModifiedFibonacci(n - 1) #Recursion
        curr = (prev[-1] * prev[-2]) + 1
        return prev + [curr]