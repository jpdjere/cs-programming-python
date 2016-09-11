balance = 999999
annualInterestRate = 0.18
##########################################################
monthlyInterestRate = annualInterestRate/12.0
newbalance = balance
low = balance/12.0
high = (balance*(1+monthlyInterestRate)**12)/12.0
ans = (high+low)/2.0
epsilon = 0.01

while abs(newbalance) > epsilon:  
    
    newbalance = balance

    for j in range(1,13):
        newbalance = newbalance - ans
        #print('New Balance After Paid: '+str(newbalance))
        if newbalance > 0:
            newbalance = newbalance + monthlyInterestRate*newbalance  
        #print('New Balance + Int: '+str(newbalance))

    if newbalance < 0:
        high = ans
    else:
        low = ans
    ans = (high+low)/2.0

print('Lowest Payment: '+str(round(ans,2)))