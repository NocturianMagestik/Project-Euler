numbers = {
    1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
    8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
    14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
    18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',
    50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
    100:'hundred',1000:'thousand'}

tally = 0
for number in range(1, 1001):
    string_of_number = str(number)
    if len(str(number)) == 1:

        length_of_number = len(numbers[number])
        print ("n= %s k= %s" % (number, length_of_number))

    elif len(str(number)) == 2:
        x1 = string_of_number[0]
        x2 = string_of_number[1]
        if number < 20:
            # The numbers under 20 -- in the dictionary
            length_of_number = len(numbers[number])
            print ("n= %s k= %s" % (number, length_of_number))
        else:
            if x2 == '0':
                # The numbers under 100 and greater than 19 -- in the
                # dictionary ending in '0', (20, 30, 40 ....)
                length_of_number = len(numbers[number])
                print ("n= %s k= %s" % (number, length_of_number))
            else:
                # The other numbers under 100 greater than 19
                x1a = str(x1 + '0')
                length_of_number = len(numbers[int(x1a)]) + len(numbers[int(x2)])
                print ("n1= %s k1= %s" % (number, length_of_number))


    elif len(str(number)) == 3:
        # add 3 for 'and' i.e. -- two-hundred and ten
        x1 = string_of_number[0:1]
        x2 = string_of_number[1:2]
        x3 = string_of_number[2:3]
        x1a = str(x2 + '0')
        x1aa = str(x2 + x3)
        if x1 == '1' and x2 == '0' and x3 == '0':
            # 100 -- in the dictionary
            length_of_number = len(numbers[1]) + len(numbers[100])
            print ("n= %s k= %s" % (number, length_of_number))
        elif x2 == '0' and x3 == '0':
            # Consider 200, 300, 400, 500, 600, 700, 800, and 900
            length_of_number = len(numbers[int(x1)]) + len(numbers[100])
            print ("n= %s k= %s" % (number, length_of_number))
        elif x2 == '0' and x3 != '0':
            # Consider 101, 102 ... 109, 201, 202, ... 209 etc.
            length_of_number = 3 + len(numbers[int(x1)]) + len(numbers[100]) \
                               + len(numbers[int(x3)])
            print ("n= %s k= %s" % (number, length_of_number))
        elif x2 != '0' and x3 == '0':
            # Consider 110, 120, ... 190, 210, 220, ... 290 etc.
            length_of_number = 3 + len(numbers[int(x1)]) + len(numbers[100]) \
                               + len(numbers[int(x1a)])
            print ("n= %s k= %s" % (number, length_of_number))
        elif x2 == '1' and x3 != '0':
            # Consider the teens 111, 112, ... 119, 211, 212, ... 219 etc.
            length_of_number = 3 + len(numbers[int(x1)]) + len(numbers[100]) \
                               + len(numbers[int(x1aa)])
            print ("n= %s k= %s" % (number, length_of_number))
        else:
            # Consider all the other numbers
            length_of_number = 3 + len(numbers[int(x1)]) + len(numbers[100]) \
                               + len(numbers[int(x1a)]) + len(numbers[int(x3)])
            print ("n= %s k= %s" % (number, length_of_number))

    else:
        # 1000 -- two parts (one and thousand) -- in the dictionary
        length_of_number = len(numbers[1]) + len(numbers[1000])
        print ("n= %s k= %s" % (number, length_of_number))

    tally = tally + length_of_number
print ("Final Tally = %s" % tally)