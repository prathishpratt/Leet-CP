# Question 1: Define a function called question1 that accepts a dictionary representing city names and 
# their respective populations. The function should filter and return a list of cities with 
# populations exceeding 1 million people. This function should use a lambda function 
# and the filter function to return a list of cities with populations exceeding 1 million people, 
# sorted in descending order based on their population.

# Ex: {"San Diego": 1.38, "Los Angeles": 3.849, "New York": 8.468} #values are in terms of million people
# Ans: ["New York", "Los Angeles", "San Diego"]

def question1(d):
    #Your code here
    #Use lambda function and filter here and print the output list
    li = filter(lambda x:d[x] > 1,d)
    sortli = sorted(li, key = lambda x:d[x], reverse=True)
    return sortli