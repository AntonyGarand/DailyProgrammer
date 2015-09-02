words = '''billowy
biopsy
chinos
defaced
chintz
sponged
bijoux
abhors
fiddle
begins
chimps
wronged'''.split("\n")

for word in words:
    case = 0 #0 = ordered, 1 = reverse, 2 = random
    for i in range(len(word)-1):
        #If it not ordered
        if(case != 0):
            if(ord(word[i]) < ord(word[i+1])):
                print word + " NOT IN ORDER"
                case = 2
                break
        #if the next character is bigger than the current one (b > a), it is not ordered
        elif (ord(word[i]) > ord(word[i+1])):
            #Check if it is NOT the first character. If it isn't, it is not in order. If it is, check for reverse. 
            if(i != 0):
                print word + " NOT IN ORDER"
                case = 2
                break
            else:
                case = 1
    if case == 0:
        print word + " IN ORDER"
    elif case == 1:
        print word + " REVERSE ORDER"
