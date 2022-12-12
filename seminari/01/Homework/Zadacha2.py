def calculation(x, y, z):
   return ((not(x or y or z))== (not(x) and not(y) and not(z)))

for i in range(2):
   for y in range(2):
      for n in range(2):
         print(calculation(i, y, n))