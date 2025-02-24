def numToWords(num):
    return "example"

def numToCheck(num):
    return f"{numToWords(num-(num%1))} dollars and {num%1}/100"

if __name__=="__main__":
    amount = input("enter the amount as a number: ")
    try:
        num = float(input)
        print(numToCheck(num))
    except ValueError:
        print("Error: not a number")