celsius=float(input("Enter The Temprature in Celsius:"))
fah=(celsius*1.8)+32#This is the Formula of conversion,to convert celsius into fahrenheit
print(celsius,"is",fah,"in Fahrenheit")

print("%0.1f Degree celsius is equal to %0.1f Degree Fahrenheit"%(celsius,fah))

temp=fah

if(temp>=104):
    print("IT'S TOO HOT!!")
elif temp<=50:
    print("IT'S TOO COLD!!")
else:
    print("It is bareable :)")

