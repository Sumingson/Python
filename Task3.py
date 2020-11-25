a = int(input())
s = 0
while a != 0:
  a = a // 10
  s +=1
print(s)
if s %2 == 0:
  number = a
  n = s
  n1 = 1
  s1 = 0
  for j in range(0,int(s/2)):
    if (number//(10*(n-1)%(10*n1)) == (number % (10*n1))//10*(n-1)): #выдает ошибку здесь, как деление на ноль, хотя такового не производится
        s1+=1
    n1 +=1
    n -= 1
    if s1 = s/2:
      print("число",a,"палиндром")
else:
  #здесь для нечетных
