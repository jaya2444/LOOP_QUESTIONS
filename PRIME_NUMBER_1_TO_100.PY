i=1
while i<=100:
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
        print(i,"prime number")
    elif i==2 or i==3 or i==5 or i==7:
        print(i,"prime number")
    i=i+1