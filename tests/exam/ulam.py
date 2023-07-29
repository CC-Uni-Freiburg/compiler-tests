# Author: Alexander Pfefferle
#in=
#golden=1357930321844
def ulam(point: list[int]) -> int:
  x=point[0]
  y=point[1]
  xabs=(x if x>=0 else -x)
  yabs=(y if y>=0 else -y)
  if (x > yabs):
    return ((2*x-1)*(2*x-1)+y+x)
  if (y > xabs):
    return ((2*y)*(2*y)+1-y-x)
  if (x <= -yabs):
    return (((-2)*x)*((-2)*x)+1-y-x)
  return (((-2)*y+1)*((-2)*y+1)+x+y)

print(ulam([0,0]))
print(ulam([1,1]))
print(ulam([-1,1]))
print(ulam([-1,-1]))
print(ulam([1,-1]))
print(ulam([3,2]))
print(ulam([2,3]))
print(ulam([-2,1]))
print(ulam([-2,-3]))
