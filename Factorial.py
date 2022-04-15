print("""*******************
Factorial Calc

Press "q" quit 
*******************""")

while True:
    num =  input("Enter Number:")
    if (num == "q"):
        print("Closing Program")
        break
    num = int(num)

    fact = 1
    for i in range(2,num+1):
        fact *= i

    print("Factorial: ",fact)