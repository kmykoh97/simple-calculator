while True:
  #ask for intention
  print('You can choose "add", "subtract", "multiply", or "division"')
  Intention = input('What do you wish to do? Please specify in full phrase:')
  #ask for numbers
  Number1 = float(input('insert your first number:'))
  Number2 = float(input('insert your second number:'))
  #start calculation
  if Intention == 'add':
    print('Your answer is ' + str(Number1 + Number2))
  elif Intention == 'subtract':
    print('Your answer is ' + str(Number1 - Number2))
  elif Intention == 'multiply':
    print('Your answer is ' + str(Number1 * Number2))
  elif Intention == 'division':
    print('Your answer is ' + str(Number1/Number2))
  elif int(Intention)/1 >= 0:
    print('please enter add, subtract, multiply or division only!')
    raise ValueError
  elif int(Intention)/1 <= 0:
    print('please enter add, subtract, multiply or division only!')
    raise ValueError
  else:
    print('please enter add, subtract, multiply or division only!')
    raise NameError("You are very stupid! Please follow instruction!!")
  #New loop if requested
  NewCalculation = input('Thank you for using me, do you want to start a new calculation?(y or n)')
  if NewCalculation == 'y':
    print('OK :)')
  elif NewCalculation == 'n':
    break
  else:
    #I can make one more loop here. Try again next time
    print("I don't understand you. I will assume you want to terminate program.")
    break

#termination lines
print('Thank you, see you again :)')
