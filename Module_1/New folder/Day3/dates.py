import datetime

x=datetime.datetime.today()
print(x)
print(x.year)
print(x.date())
print(x.strftime("%A"))# showing day 
print(x.strftime("%B"))#showing months
print(x.strftime("%C"))# showin the centuray


# "'%A'=Wednesday(showing day) '&B'=october(Showing Month)"


# "Creating  date object"

y=datetime.datetime(2026,10,20,11,24,12)
print(y)