#Q11
dd= int(input('Please enter the day of the month: '))
mm= int(input('Please enter the month of the year: '))
year= int(input('Please enter the year: '))

if mm< 3:
    mm = mm+12
    year = year-1
y = year % 100    
c = year//100

w=(dd+((13*(mm+1))//5)+y+(y//4)+(c//4)-(2*c))%7
print('the day of the week is: ', w)

if w==0:
    weekday = "Saturday"
elif w==1:
    weekday = "Sunday"
elif w==2:
    weekday = "Monday"
elif w==3:
    weekday = "Tuesday"
elif w==4:
    weekday = "Wednesday"
elif w==5:
    weekday = "Thursday"
elif w==6:
    weekday = "Friday"
else:
    weekday="nil"
    print("Invalid date entered!")   

print("Weekday is ",weekday ," (which is ",w, " )")



    

#w= ((dd + (13*(mm+1)//5) + y + y//4 + (c//4) - 2*c)%7)
#print('The day of the week is', w)