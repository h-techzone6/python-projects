def Agecalculator(y,m,d):
    import datetime
    today=datetime.datetime.now().date()
    dob=datetime.date(y,m,d)
    age=int((today-dob).days/365.25)
    print(age)

y=int(input("Enter year of birth:"))
m=int(input("Enter Month of Year:"))
d=int(input("Enter Date of Birth:"))

Agecalculator(y,m,d)