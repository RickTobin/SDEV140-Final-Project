# Compound interest calaculator. This program add the compound interest to the
# oringinal dollar amoount or the principle
# Author Rick Tobin
# Version 1.5
# Date: 6/19/2022


x = " "
while x != "quit":

    principle = float(input("please enter starting dollar  $"))
    interestRate = float(input("Enter interest rate  "))
    years = float(input("Enter number of years investing  "))
    numCompounded = int(input("enter number of times compounded a year, monthy = 12, quarterly - 4, semi-annually = 2, year = 1   "))

    futureValue = principle * (((1 + (interestRate/(100.0 * numCompounded))) ** (numCompounded*years)))




    #total amount of interest earned
    interestEarned = futureValue - principle
    formatedIE = "{:,.2f}".format(interestEarned)

    #Capital Gains tax rate 15%
    afterTax = futureValue - (interestEarned * .15)

    #Formated printed text with commas
    formatedNum = "{:,.2f}".format(futureValue)
    print(formatedNum)

    formatedNum2 =  "{:,.2f}".format(afterTax)
    print("Total after " ,years, "years", "$", formatedNum)
    print("After Taxes $", formatedNum2)
    print("Interest Earned $", formatedIE)


    print("")
    input("enter quit to end  ")
    if x == "quit":
        break





                    
