# Create function that return Fibonacci Sequence

def calculate_fibo(n):
  fibo=[0,1]
  for i in range (n):
    fibo.append(fibo[-1]+fibo[-2])
  return fibo

print (calculate_fibo(10))