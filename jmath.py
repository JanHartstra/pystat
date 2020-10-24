# Program : jmath.py
# Purpose : Module defining some additional) mathematical functions
# Author  : Jan Hartstra <jan.hartstra@gmail.com)

import math

def fac (n):
   """
   Function returning the faculty (n!) of a number.
   """
   f = 1
   for i in range(1, n + 1):
      f *= i
   return f

def perm (n,k):
   """
   Function returning the number of permuations of n over k
   """
   if k > n:
      s = float('nan')
   else:
      s = 1
      for i in range(n-k+1, n+1):
         s *= i
   return float(s)
   
def comb (n,k):
   """
   Function returning the number of combinations of n over k
   A combination is a selection of items from a collection, 
   such that the order of selection does not matter
   (unlike permutations).
   Binomial coefficient.
   """
   if k > n:
      s = float('nan')
   else:
      s = 1
      for i in range(1, n-k+1):
         s = s*(n-i+1)/i
   return float(s)

def erf (x):
   """
   Error function approximation
   Ambramowitz and Stegun, 7.1.28, p. 299
   """
   a=[1, 
   0.0705230784,
   0.0422820123,
   0.0092705272,
   0.0001520143,
   0.0002765672,
   0.0000430638
   ]
   s = 0
   for i in range(len(a)):
      #print('i=', i)
      #print('x^i= ', x**i)
      #print('a[i]=', a[i])
      t = a[i]*x**i
      #print('a[i]*x**i= ', t)
      s = s+t
      #print('s= ', s)
   return 1-1/s**16
      
def test():   
   print('Factorial of %d is %d' % (5, fac(5)))
   print('perm(%d, %d) = %d' % (10, 3, perm(10,3)))
   print('perm(%d, %d) = %f' % (7, 4, perm(7,4)))
   print('perm(%d, %d) = %f' % (3, 10, perm(3,10)))
   print('comb(%d, %d) = %f' % (4, 2, comb(4,2)))
   print('comb(%d, %d) = %f' % (4, 1, comb(4,1)))
   print('comb(%d, %d) = %f' % (10, 4, comb(10,4)))
   print('erf(%f) = %f' % (2, erf(2)))
   print('math.erf(%f) = %f' % (2, math.erf(2)))
   print('Note: erf(2) in this module provides a more crude approximation.')
