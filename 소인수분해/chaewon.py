n = 17
answer = []
for num in range(2, n+1):
  while n%num == 0:
    n = n/num
    answer.append(num)
print(list(set(answer)))
# n = 420
# num = 1
# while n%(num+1) == 0:
#   n = n/(num+1)
