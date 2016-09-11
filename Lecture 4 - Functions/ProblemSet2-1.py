balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
##########################################################
monthlyInterestRate = annualInterestRate/12
totalPaid = 0
for i in range(0,12):
    print('Month: '+str(i+1))
    minMonthlyPayment = monthlyPaymentRate*balance
    print('Minimum monthly payment: '+str(round(minMonthlyPayment,2)))
    monthlyUnpaidBalance = balance - minMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
    print('Remaining balance: '+str(round(balance,2)))
    totalPaid += minMonthlyPayment
    
print str(round(totalPaid,2))
print('Remaining balance: '+str(round(balance,2)))
