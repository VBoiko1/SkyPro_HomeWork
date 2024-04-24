def month_to_season(n):
        n=int(n)
        if n == 1 or n == 2 or n == 12:
          return ("Зима")
        if n == 3 or n == 4 or n == 5:
          return ("Весна")
        if n == 6 or n == 7 or n == 8:
          return ("Лето")
        if n == 9 or n == 10 or n == 11:
          return ("Осень")

         
q= month_to_season(input())
print (q)


