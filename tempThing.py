# tempThing.py

def f2c(fTemp):
    return ((fTemp - 32) * 5 / 9)
    

def c2f(cTemp):
    return ((cTemp * 9 / 5) + 32)

def main():
    print("Temperature Converter")
    convChoice = input("Enter C for Celsius to Fahrenheit, F for Fahrenheit to Celsius, or E to exit: ")
    if convChoice == "C":
        print(c2f(float(input("Enter temperature in Celsius: "))), "F")
        main()
    elif convChoice == "F":
        print(f2c(float(input("Enter temperature in Fahrenheit: "))), "C")
        main()
    elif convChoice == "E":
        exit()
    else: main()

main()
