#Program: jcstat.py
#Purpose: Python module providing a class for doing simple
#         descriptive statistics.
#Author:  Jan Hartstra <jan.hartstra@gmail.com>

import math #Used for the math.sqrt(), log(), exp() and fsum() functions.

class Stat:
   """
   Define a class providing methods to calculate simple descriptive
   statistics using a Python list as data vector.
   """
   #Class variables:
   author='jan.hartstra@gmail.com'
   y = []                               #Use list as the data vector.
   
   def __init__(self, data):
      """
      Construtor of the Stat class.
      """
      self.y = data
      
   def n(self):
      """
      Class function returning the number elements of the data vector.
      """
      return len(self.y)

   def mean(self):
      """
      Class function returning the mean of the data vector using the python sum() function.
      """
      return math.fsum(self.y)/self.n()  #Use math.fsum for a better precision?

   def average(self):
      """
      Class function returning the mean of a vector using a for loop.
      """
      n,S = 0,0
      for yi in (self.y):
         n = n + 1
         S = S + yi
      return S/n
      
   def min(self):
      """
      Class function returning the minimum of the data vector.
      """
      return min(self.y)
      
   def max(self):
      """
      Class function returning the maximum of the data vector.
      """
      return max(self.y)
      
   def median(self):
      """
      Class function returning the median of the data vector.
      """
      s=sorted(self.y)
      n=self.n()
      if n % 2 == 0:
         return (s[math.floor(n/2)]+s[math.ceil(n/2)])/2
      else:
         return s[math.floor(n/2)]
      #return m
         
   def gmean(self):
      """
      Class function returing the geometric mean of the data vector using a for loop.
      """
      n,S = 0,0
      for yi in (self.y):
         n = n + 1
         S = S +math.log(yi)
      return math.exp(S/n)

   def center(self,yy,m):
      """
      Returns a vector centered around a specified number m.
      (Often used to produce a mean centered vector.)
      """
      x=[]
      for i in range(len(yy)):
         x.append(yy[i]-m)
      return x

   def pwr(self,yy,p=2):
      """
      Class function returning a vector with values raised to the power p (default 2)
      for the elements of the input vector yy.
      """
      x = []
      for i in range(len(yy)):
         x.append(pow(yy[i],p))
      return x
   
   def SS(self):
      """
      Class function returning the sum of squares of the data vector.
      This is squaring the mean centered data, using the
      sqr(), center() and mean() methods defined above.
      """
      return sum(self.pwr(self.center(self.y,self.mean())))

   def var(self,d=1):
      """
      Class function returing the variance of the data vector.
      """
      df = len(self.y)-d
      return self.SS()/df

   def sd(self,d=1):
      """
      Class function returning the standard deviation of the data vector.
      d --- 1 for sample SD, 0 for population SD (mu known).
      """
      return math.sqrt(self.var(d))
   
   def CV(self):
      """
      Class function returning the coefficient of variation
      """
      return self.sd()/self.mean()
      
   def skewness(self):
      """
      Class function returing the skewness.
      """
      g = sum(self.pwr(self.center(self.y,self.mean()),3))/self.n()/self.sd()**3
      c = math.sqrt(self.n()*(self.n())-1)/(self.n()-2)
      return c*g
      
   def stats(self):
      """((()))
      Prints an overview of descriptive statistics of the data vector.
      """
      print('mean     = %f' % self.mean())
      print('n        = {:d}'.format(self.n())) 
      print('mean     = {:f}'.format(self.average()))
      print('median   = {:f}'.format(self.median()))
      print('min      = {:f}'.format(self.min()))
      print('max      = {:f}'.format(self.max()))
      print('geo. mean= {:f}'.format(self.gmean()))
      print('variane  = {:f}'.format(self.var()))
      print('SD (n-1) = {:f}'.format(self.sd()))
      print('SD (n)   = {:f}'.format(self.sd(0)))
      print('CV       = {:f}'.format(self.CV()))
      print('CV (%)   = {:5.1f}'.format(100*self.CV()))
      print('skewness = {:f}'.format(self.skewness()))
   
   def normalCDF(self, x):
      """
      Returns the standard normal cummulative distibution of a value x.
      """
      return (1+math.erf(x/math.sqrt(2)))/2

def test():
   """
   Testing the class.
   """
   #Define the data vector as a Python list of numbers.
   a=[1,2,3,4,5]
   v=Stat(a)                  #Create an instance v of the Stat class.
   print(v.author)            #Print a class variable, not good OO practise?
   print(v.mean())            #Call a method of the Stat class and print the result.

   m=Stat([1,2,3,4,5]).mean() #Different way initialize an instance, call a method,
   print(m)                   #and print the result.
 
   print(v.center(v.y, v.mean()))
 
   v.stats()

test() 

