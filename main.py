loanAmount= int(input('What is the loan amount? '))
interestRate = int(input('What is the interest rate percent? '))
monthlyPayment = int(input('What is the monthly payment? '))
fileName = input('What is the name of the file to write to(csv format)? ')
print(loanAmount, interestRate, monthlyPayment, fileName)
f = open(fileName + ".csv", "a")
f.write(str(loanAmount))
f.write(',')
f.write(str(interestRate))
f.write(',')
f.write(str(monthlyPayment))
f.write(',')
f.write(str(fileName))
f.write('\n')
f.write("Month,Interest Incurred, Remaining Loan\n")
totalLoan = loanAmount
remainingLoan = loanAmount
months = 0
amountIncurred = 0
interestIncurred = 0
while remainingLoan > 0 and months <= 30:
   amountIncurred =  monthlyPayment * months
   remainingLoan = totalLoan - amountIncurred
   if remainingLoan < 0:
     amountIncurred = totalLoan
     remainingLoan = 0
     f.write(str(months) + "," + str(interestIncurred) +"," + str(remainingLoan) + "\n")
     break
   totalLoan = loanAmount * (1.0/12)*(interestRate/100.0) + totalLoan
   interestIncurred = totalLoan - loanAmount
   f.write(str(months) + "," + str(interestIncurred) +"," + str(remainingLoan) + "\n")
   months = months + 1
  
   print(months, remainingLoan)
print(loanAmount)
 
f.close()
 
 

