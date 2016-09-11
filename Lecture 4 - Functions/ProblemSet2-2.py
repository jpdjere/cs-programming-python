balance = 4773
annualInterestRate = 0.2
##########################################################
monthlyInterestRate = annualInterestRate/12.0
newbalance = balance
for i in range(10,1000,10):
    
    #print('Fixed: '+str(i))
    newbalance = balance
    for j in range(1,13):
        newbalance = newbalance - i
        #print('New Balance After Paid: '+str(newbalance))
        if newbalance > 0:
            newbalance = newbalance + monthlyInterestRate*newbalance  
        #print('New Balance + Int: '+str(newbalance))
    if newbalance <= 0:
        lowest = i
        break

print('Lowest Payment: '+str(lowest))