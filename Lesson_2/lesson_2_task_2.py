def is_year_leap(x):
    x= int(x)
    if x % 4 != 0 :
     return (x, False)
    else:
      return (x, True)
y = is_year_leap(input()) 
print(y)   



