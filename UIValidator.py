"""
Authors: Ryan Mulkey, Timothy Campbell, Robert Beery III

Description: This is a simple validator for input.

Date Modified: 7/26/21
"""
def uivalidator(question):
    condition = False
    invalid = True
    response = ''
    while invalid:
        response = input(question).lower()
        if response != 'y' and response != 'n':
            print("Invalid input. Please input either Y or N.")
        else:
            invalid = False

    if response == 'y':
        condition = True
    return condition
