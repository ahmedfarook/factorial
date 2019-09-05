#The below mentioned piece of code will fetch you factorial of a number

user_input=int(input("Enter a number:")) #Taking input from user

factorial = user_input  #Putting the user defined input in factorial

for i in range(user_input - 1):     # Starting of For Loop

    user_input -= 1     #Decrementing value of user_input by 1

    factorial *= user_input     #This is main line of code, where we're multiplying both the values.

print(factorial)    #Printing the value of Factorial  
