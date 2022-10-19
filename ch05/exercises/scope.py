# 1
def multiply(num1, num2):
  result = 0
  for i in range(num2):
    result = result + num1
  return result
  
def main():
  res = multiply(5, 4)
  print(res)

main()


# 2
def exponent(num, exponent):
  result = 1
  for i in range(exponent):
    result = result * num
  return result

def main2():
  res = exponent(2, 3)
  print(res)

main2()


# 3
def square(num):
  return exponent(num, 2)

# test = square(6)
# print(test)
