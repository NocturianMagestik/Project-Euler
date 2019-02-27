numbers = {
    1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
    8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
    14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
    18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',
    50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
    100:'hundred',1000:'thousand'}

total = 0
for number in range(1, 1001):
    string_of_number = str(number)
    if len(str(number)) == 1:
        # if the number only has one digit, then it is in the dictionary. No parsing or magical stuff required.
        length_of_number = len(numbers[number])
        

    elif len(str(number)) == 2:
        # if the number has 2 digits, split it up into the two digits
        first_digit = string_of_number[0]
        second_digit = string_of_number[1]
        if number < 20:
            # The numbers under 20 are in the dictionary, again, no magic required.
            length_of_number = len(numbers[number])
        else:
            if second_digit == '0':
                # This checks if the number is a multiple of ten, which are irregular and thus are referenced directly
                # in the dictionary, like the single digit numbers.
                length_of_number = len(numbers[number])
            else:
                # If the two digit number is not a multiple of ten, partition the number into tens and units by taking 
                # the first digit and adding 0 to it
                tens = str(first_digit + '0')
                length_of_number = len(numbers[int(tens)]) + len(numbers[int(second_digit)])
                


    elif len(str(number)) == 3:
        # if the number has 3 digits, split it up into 3 digits
        first_digit = string_of_number[0]
        second_digit = string_of_number[1]
        third_digit = string_of_number[2]
        # partition the number into tens, and then the last two digits separately for separate length calculation
        tens = str(second_digit + '0')
        last_two_digits = str(second_digit + third_digit)

        # we will check the length of the number in different ways depending on their format
        # check if the number is 100, and therefore in the dictionary, no magic required
        if first_digit == '1' and second_digit == '0' and third_digit == '0':
            
            length_of_number = len(numbers[1]) + len(numbers[100])

        # if not 100, then check if the number is another multiple of 100, and therefore easier to calculate
        elif second_digit == '0' and third_digit == '0':
            
            length_of_number = len(numbers[int(first_digit)]) + len(numbers[100])

        # check if the number fits the form of n - 0 - x, for example 2 - 0 - 3
        elif second_digit == '0' and third_digit != '0':

            length_of_number = 3 + len(numbers[int(first_digit)]) + len(numbers[100]) + len(numbers[int(third_digit)])

        # check if the number fits the form of n - x - 0, for example 2 - 3 - 0
        elif second_digit != '0' and third_digit == '0':

            length_of_number = 3 + len(numbers[int(first_digit)]) + len(numbers[100]) + len(numbers[int(tens)])

        # check if the number fits the form of n - 1 - 0
        elif second_digit == '1' and third_digit != '0':

            length_of_number = 3 + len(numbers[int(first_digit)]) + len(numbers[100]) + len(numbers[int(last_two_digits)])

        # all the other numbers
        else:
            length_of_number = 3 + len(numbers[int(first_digit)]) + len(numbers[100]) + len(numbers[int(tens)]) + len(numbers[int(third_digit)])

    else:
        # we work out the length of one thousand
        length_of_number = len(numbers[1]) + len(numbers[1000])

    total = total + length_of_number

print ("Final Tally = %s" % total)
