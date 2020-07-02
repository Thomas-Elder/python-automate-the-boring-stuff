#! python3

# based on NA phone numbers
def isphonenumber(text):
    if len(text)!= 12: # it's not the right length
        return False
    
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    
    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    
    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    
    return True

number = '123-123-1234'
badnumber = '12x 12p,1234'

print(isphonenumber(number))
print(isphonenumber(badnumber))
#True
#False