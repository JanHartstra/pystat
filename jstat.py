# Program: jstat.py
# Purpuse: Python module for calculating simple descriptive statistics using a standard
#          python list data structure as a data vector. 
# Author:  Jan Hartstra <jan.hartstra@gmail.com>

import math #Used for the math.sqrt(), log(), exp() and fsum() functions.

def mean (y):
   """
   Returns the mean of a vector using the python sum() function.
   """
   #return sum(y)/len(y)
   return math.fsum(y)/len(y)  #Use math.fsum for a better precision?

def average (y):
   """
   Returns the mean of a vector using a for loop.
   """
   n,S = 0,0
   for yi in (y):
      n = n + 1
      S += yi
   return S/n

def gmean (y):
   """
   Returns the mean of a vector using a for loop.
   """
   n,S=0,0
   for yi in (y):
      n = n + 1
      S = S + math.log(yi)
   return math.exp(S/n)

def center (y,m):
   """
   Returns a vector centered around a specified number m.
   """
   x = []
   for i in range(len(y)):
      x.append(y[i]-m)
   return x

def sqr (y):
   """
   Return a vector with squared values of the elements of the input vector.
   """
   x = []
   for i in range(len(y)):
      x.append(pow(y[i],2))
   return x
   
def SS (y):
   """
   Returns the sum of squares of a specified vector.
   """
   return sum(sqr(center(y,mean(y))))

def var (y,d=1):
   """
   Returns the variance of a specified vector.
   """
   df = len(y)-d
   return SS(y)/df

def sd (y,d=1):
   """
   Return the standard deviation of a specified vector.
   
   y --- the data vector for which the standard deviation (SD) should calculated.
   d --- 1 for sample SD, 0 for population SD (mu known).
   """
   return math.sqrt(var(y,d))
   
def CV (y):
   """
   Return the Coefficient of Variance of a specified vector.
   Uses functions sd() and mean().
   """
   return sd(y)/mean(y)

def stats (y):
   """Prints an overview of descriptive statistics for a specified vector. """
   print('mean     = %f' % mean(y))   
   print('mean     = {:f}'.format(average(y)))
   print('geo. mean= {:f}'.format(gmean(y)))
   print('variance = {:f}'.format(var(y)))
   print('SD (n-1) = {:f}'.format(sd(y)))
   print('SD (n)   = {:f}'.format(sd(y,0)))
   print('CV       = {:f}'.format(CV(y)))
   print('CV (%)   = {:5.1f}'.format(100*CV(y)))
   
def normalCDF (x):
   """
   Standard normal cumulative distribution function.
   Uses math.erf() function.
   """
   return (1+math.erf(x/math.sqrt(2)))/2

def test():
   """
   Test the module.
   """
   #Define the data vector as a Python list of numbers.
   a = [1,2,3,4,5]
   stats(a)

   #print(len(a))
   #print(range(len(a)-1))
   #print(a[1])
   #print(a)
   #a2=center(a,3)
   #print(a2)

   print(normalCDF (1.96))
  
test()
