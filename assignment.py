from num2words import num2words

def numToWords(num):
    return num2words(num)

def numToCheck(num):
    return f"{numToWords(num - (num % 1))} dollars and {(num % 1) * 100:02.0f}/100"

if __name__=="__main__":
    amount = input("enter the amount as a number: ")
    try:
        num = float(amount)
        print(numToCheck(num))
    except ValueError:
        print("Error: not a number")