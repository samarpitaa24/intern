def cal(x):
  return 5 * x , x - 5 ,x + 5  #returns multiple values in tuple format
mult , sub , add = cal(10)
print(mult , sub , add)