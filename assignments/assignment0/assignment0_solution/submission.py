class theCalculator():
  def multiply(self, x, y):
    return(x * y)
  
  def add(self, x, y):
    return(x + y)
  
  def subtract(self, x, y):
    return(x - y)
  
  def divide(self, x, y):
    return(x/y)
  
  
  
if __name__ == '__main__':
  calc = theCalculator()
  print(calc.multiply(2,3))
  print(calc.add(2,3))
  print(calc.subtract(2,3))
  print(calc.divide(2,3))