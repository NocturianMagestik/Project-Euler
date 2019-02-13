
def primesto(to):
    to+=1
    li=[True]*to
    li[0]=False
    li[1]=False
    out=[]
    sum = 0
    for x in range(len(li)):
        if li[x]:
            out.append(x)
            sum += x
            up=x*2
            while up<to:
                li[up]=False
                up+=x

    return sum
print(str(primesto(20000000)))
























"""
sTotal = 0
total = 0
for i in range(1 , 101):
    square = i ** 2
    sTotal += square
    total += i
fTotal = total ** 2
ans = fTotal - sTotal
print(str(ans))


Factors = [11, 12, 13, 14, 15, 16, 17, 19, 20]


works = True
for i in range(2520, 9999999999, 2520):
    works = True
    for n in range(len(Factors)):
        if i % Factors[n] == 0:
            pass
        else:
            works = False
    if works == True:
        print(str(i))
        break


this is question 4
numbers = []
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

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if numToArr(product) == reverser(numToArr(product)):
            numbers.append(product)

print(str(max(numbers)))
"""