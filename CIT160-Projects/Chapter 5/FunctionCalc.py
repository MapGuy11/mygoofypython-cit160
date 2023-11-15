# Made by Connor Hackenberg
# Date Started: 10/23/23
# Program Importance: This program will create a calculator using functions
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11

def main():
    operand1 = float(input("Enter first operand: "))
    operator = input("Enter the operator: ")
    operand2 = float(input("Enter the second operand: "))

    result = 0
    # determine the operator
    if operator == "*":
        #multiply
      result = multiply(operand1,operand2)
    elif operator == "/":
        # divide
      result = divide(operand1, operand2)
    elif operator == "+":
        # add
      result = addition(operand1, operand2)
    elif operator == "-":
        # subtract
      result = substract(operand1, operand2)
    else:
        print("Bad operator..........")
    print(result)

def multiply(opp1, opp2):
    result (opp1 * opp2)
def divide(opp1, opp2):
    result (opp1 / opp2)
def substract(opp1, opp2):
    result (opp1 - opp2)
def addition(opp1, opp2):
    result (opp1 + opp2)


main()