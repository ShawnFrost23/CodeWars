def solution(number):
   return sum([int(x) for x in range(0, number, 1) if x % 3 == 0 or x % 5 == 0])
  