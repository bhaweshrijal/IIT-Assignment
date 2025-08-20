income=int(input("enter the taxable income"))
if(income<=20000):
    set_tax=.025*income
elif (income<=50000):
    set_tax=400+.025*(income-20000)
else:
    set_tax=1150+.035*(income-50000)
print("your total tax is:",str(set_tax))    

