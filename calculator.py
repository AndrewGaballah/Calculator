while True:
  try:
    first_number = float(input('Enter the first number: '))
  except ValueError:
    print('Invalid input. Please enter a number.')
    continue
  while True:
    try:
      operation = input('Enter operation type: ')
      if operation not in ('+', '-', '*', '/'):
       raise ValueError
      else:
          break
    except ValueError:
     print('Invalid input. Please enter +, -, *, /')
    continue
  while True:
    try:
        second_number = float(input('Enter the second number: '))
        break
    except ValueError:
        print('Invalid input. Please enter a number.')
        continue


  if operation == '+':
    print(first_number + second_number)
  elif operation == '-':
    print(first_number - second_number)
  elif operation == '/':
    print(first_number / second_number)
  elif operation == '*':
    print(first_number * second_number)
  else:
    print('ArithmeticError')
  repeat = input('Do you want to perform another operation (y/n): ')
  if repeat == 'n':
    break
print('program exited')