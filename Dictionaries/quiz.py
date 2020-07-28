"""
100% first time through!!!
"""

# Question 1
# Which of the following corresponds to a dictionary with no elements

trial = dict()
print(trial)

# dict()
# {}

# Question 2 
# Given an existing dictionary favorites, 
# what Python statement adds the key 
# "fruit" to this dictionary with the corresponding value "blackberry"?
favorites = dict()
favorites["fruit"] = "blackberry"
print(favorites)

# Question 3
# Which of the expressions below returns True 
# when the dictionary my_dictionary contains 
# the key my_key and False otherwise?

# my_key in my my_dictionary

# Question 4
# Keys in a dictionary can have which of the following types?

# float
# tuple

# Question 5
# Values in a dictionary can have which of the following types?

# All 

# Question 6
# What happens when Python evaluates the expression instructor_ratings["John"]?
instructor_ratings = {"Joe" : "awesome", "Scott" : "hmmm..."}
#print(instructor_ratings["John"])

#     print(instructor_ratings["John"])
# KeyError: 'John'


# Question 7
"""
Write a function count_letters(word_list) that takes as input a list of words that are 
composed entirely of lower case letters . 
This function should return the lower case letter that appears most frequently (total number of occurrences) 
in the words in word_list. 
(In the case of ties, return the earliest letter in alphabetical order.)
"""
import operator
def count_letters(word_list):
    """ See question description """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0
 
    # enter code here
    for word in word_list:
        for letter in range(len(word)):
            #print(word[letter])
            letter_count[word[letter]] += 1
        
    print(max(letter_count.items(), key=operator.itemgetter(1))[0])
    
#count_letters(["hello", "world"])   
    


monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

monty_words = monty_quote.split(" ")

count_letters(monty_words)  
# e