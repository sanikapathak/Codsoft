a= "Welcome To Simple Calculator"
print(a.center(50, "-"))


while True:

  # Operations included in the calculator
  print("\nPlease select an operation -\n" \
          "1. Addition(+)\n" \
          "2. Subtraction(-)\n" \
          "3. Multiplication(*)\n" \
          "4. Division(/)\n")
  
  # Take input from the user
  select = int(input("Select operations form 1, 2, 3, 4 :"))
  
  number1 = int(input("\nPlease enter first number: "))
  number2 = int(input("\nPlease enter second number: "))
  
  #Function to find sum of two numbers
  def addition(number1, number2):
    return number1 + number2
  
  #Function to find difference of two numbers
  def subtraction(number1, number2):
    if(number1 > number2):
      return number1 - number2
    else:
      return number2 - number1
  
  #Function to find product of two numbers
  def multiplication(number1, number2):
    return number1 * number2
  
  #Function to find quotient of two numbers
  def division(number1, number2):
    if(number1 > number2):
      return number1 / number2
    else:
      return number2 / number1
  
  if select == 1:
    print("\nResult of addition is:", number1, "+", number2, "=", addition(number1, number2))
  
  elif select == 2:
    if(number1 > number2):
      print("\nResult of subtraction is:", number1, "-", number2, "=", subtraction(number1, number2))
    else:
      print("\nResult of subtraction is:", number2, "-", number1, "=", subtraction(number1, number2))
  
  elif select == 3:
    print("\nResult of multiplication is:", number1, "*", number2, "=", multiplication(number1, number2))
  
  elif select == 4:
    if(number1 > number2):
      print("\nResult of division is:", number1, "/", number2, "=", division(number1, number2))
    else:
      print("\nResult of division is:", number2, "/", number1, "=", division(number1, number2))
  
  else:
    print("\nPlease check your input as it is invalid")
  
  
  # Ask the user if they want to continue
  
  continue_calculation = input("\nDo you want to continue? (yes/no): ")
  
  if continue_calculation.lower() != 'yes':
      break  # Exit the loop if the user does not want to continue