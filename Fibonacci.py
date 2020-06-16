#This code print fibonacci series.
#total is variable which contain total no. you want to print.
total = int(input("Enter no. you want to show in fibbonaci series :"))
i=2
sum1=0
sum2=1
print("\nFibbonaci series :\n")
print(sum1)
print(sum2)
while i<total: 
    sum=sum1+sum2
    print(sum)
    sum1=sum2
    sum2=sum
    i=i+1
