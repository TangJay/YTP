def getSum():
    Sum = int(input())
    return Sum
def division(Sum):
    divided = []
    for i in range(4):
        if Sum - (4 - i) >= 13:
            divided.append(13)
            Sum -= 13
        else:
            divided.append(Sum - (4 - i))
            Sum = 4 - i
    divided.append(Sum)
    return divided
if __name__ == "__main__":
    Sum = getSum()
    divided = division(Sum)
    for i in divided:
        print(i, end = " ") 