x = 23
epsilon = 0.01
step = 0.001
guess = 0.0
counter =0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
        print(str(guess))
        counter += 1
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess) + ' counter:' + str(counter)
