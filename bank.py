a = input("Enter money amount: ")
years = input("Enter number of years: ")

def bank(a, years):
    x = 0
    while x != int(years):
        b = (float(a) * 1.1)
        a = b
        x = x + 1
    print (float(a))

bank(a, years)