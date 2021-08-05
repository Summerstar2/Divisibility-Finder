print ("This program will find whether the number you input is divisible by the other number you put in.")
def Continue():
    Again=str(input("Would you like to use this program again? (Yes/No) "))
    if Again=="No":
        return False
    return True
while True:
    Number=int(input("Enter any number - "))
    Divider=int(input("Enter the number of which you wish to test the divisibility of the previous number of - "))

    if Number%Divider==0:
        print (Number,"is divisible by ",Divider)
    else:
        print (Number,"is not divisible by ",Divider)
    if not Continue():
        break
