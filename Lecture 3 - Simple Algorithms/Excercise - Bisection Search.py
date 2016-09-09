low = 0
high = 100
guess = 50
print("Please think of a number between 0 and 100! ")
print('Is your secret number '+str(guess)+'?')
ind = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")


while(ind != "c"):
    if ind not in "hlc": 
        print("Sorry, I did not understand your input.")
        print('Is your secret number '+str(guess)+'?')
        ind = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    elif ind == "h":
        high = guess
        guess = (high+low)/2
        print('Is your secret number '+str(guess)+'? ')
        ind = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")       
    elif ind == 'l':
        low = guess
        guess = (high+low)/2
        print('Is your secret number '+str(guess)+'? ')
        ind = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

print("Game over. Your secret number was: "+ str(guess))