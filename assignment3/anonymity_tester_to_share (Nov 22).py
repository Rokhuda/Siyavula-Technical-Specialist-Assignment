# Check identifying information (names, locations) has been removed from text
'''
misssing colon
is_anonymized - function mispelling
the arrangement of if statement would cause  the following string Sizwe must have made a mistake. return true nstead of false
It was returning true because after checking if Sizwe is in the name list annonymus becomes false and because that value is not returned, the function 
continues TO CHECK IF SIzwe is in the  city list. now annoymouse is given a new truthy value that get return
'''

def is_anonymised(text, names, cities):
    """
    Returns "True" if no names or cities appear in the text.
    Returns "False" if any names or cities appear in the text.
    """
    if any([name in text for name in names]) or any([city in text for city in cities]):
        anonymous = False
    else:
        anonymous = True

    return anonymous


# The names and cities that must not appear
names = ["Sizwe", "Sandra", "Tariq", "Nosipho"]
cities = ["Cape Town", "Bloemfontein", "Pretoria"]

text = input("Enter string to be tested:\n")
print(is_anonymised(text, names, cities))

# Cape Town must have made a mistake. 