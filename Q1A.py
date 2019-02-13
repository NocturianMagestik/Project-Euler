
isRunning = True

checkArr = []
checkBack = []
print('Daniyal Vemuri\n14\nReading School')
userNum = int(input())
checkNum = userNum
checkString = str(userNum)

def numToArr(number):
    numString = str(number)
    output = []
    for i in range(len(numString)):
        output.append(int(numString[i]))
    return output


def reverser(array):
    output = []
    length = len(array)
    for i in range(len(array)):
        output.append(array[length - 1])
        length -= 1
    return output


def reconstruct(array):
    output = ''
    for i in range(len(array)):
        output = output + str(array[i])
    return output


def increment(number):
    array = numToArr(number)
    dp = 0
    check = numToArr(number)
    reverse = reverser(check)
    if check != reverse:
        for i in range(len(array)):
            array = numToArr(number)
            if array[i] == array[-i - 1]:
                dp += 1

            else:
                if array[i] < array[-i - 1]:
                    numToAdd = array[i] + 10 - array[-i - 1]
                    strToAdd = str(numToAdd)
                    if dp == 0:
                        number += numToAdd

                        dp += 1
                    else:
                        for i in range(dp):
                            strToAdd = strToAdd + '0'
                        number += int(strToAdd)

                        dp += 1

                else:

                    numToAdd = array[i] - array[-i - 1]
                    strToAdd = str(numToAdd)
                    if dp == 0:
                        number += numToAdd

                        dp += 1
                    else:
                        for i in range(dp):
                            strToAdd = strToAdd + '0'

                        number += int(strToAdd)

                        dp += 1
            check = numToArr(number)
            reverse = reverser(check)
            if check == reverse:
                break
            else:
                continue
    else:
        number += 1
        array = numToArr(number)
        for i in range(len(array)):
            array = numToArr(number)
            if array[i] == array[-i - 1]:
                dp += 1

            else:
                if array[i] < array[-i - 1]:
                    numToAdd = array[i] + 10 - array[-i - 1]
                    strToAdd = str(numToAdd)
                    if dp == 0:
                        number += numToAdd

                        dp += 1
                    else:
                        for i in range(dp):
                            strToAdd = strToAdd + '0'
                        number += int(strToAdd)

                        dp += 1

                else:

                    numToAdd = array[i] - array[-i - 1]
                    strToAdd = str(numToAdd)
                    if dp == 0:
                        number += numToAdd

                        dp += 1
                    else:
                        for i in range(dp):
                            strToAdd = strToAdd + '0'

                        number += int(strToAdd)

                        dp += 1
            check = numToArr(number)
            reverse = reverser(check)
            if check == reverse:
                break
            else:
                continue
    output = number
    return output





checkArr = numToArr(userNum)

checkBack = reverser(checkArr)
print(str(increment(checkNum)))








