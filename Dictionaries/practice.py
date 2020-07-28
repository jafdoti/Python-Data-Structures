"""
Solution - Write a function is_empty(my_dict) that
returns True if a dictionary is empty and False otherwise
"""


def is_empty(my_dict):
    """
    Given a dictionary my_dict, return True if the 
    dictionary is empty and False otherwise
    """

    # Enter code here
    return len(my_dict) == 0

# Testing code
print(is_empty({}))
print(is_empty({0 : 1}))
print(is_empty({"Joe" : 1, "Scott" : 2}))


trial = {"Joe" : 1, "Scott" : 2}
vals = trial.values()
# Output
#True
#False
#False

"""
Template - Write a function value_sum(my_dict) that
returns the sum of the values in a dictionary
"""


def value_sum(my_dict):
    """
    Given a dictionary my_dict whose values are numbers, return 
    the sums of the values in my_dict
    """
    
    # Enter code here
    return sum(my_dict.values())

# Testing code
print(value_sum({}))
print(value_sum({0 : 1}))
print(value_sum({"Joe" : 1, "Scott" : 2, "John" : 4}))

# Output
#0
#1
#7