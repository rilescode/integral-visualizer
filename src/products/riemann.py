# Vidisha Gupta
# 7/19/19

import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib as mpl
from os import path

#from matplotlib.pyplot import figure
#import mpld3

INCREASE = 0.0001 # do not change!

def calculateSum(function_type, a, b, c, d, xmin, xmax, width_rect, rct_amnt, wdth_amnt, sum_type):
   plt.clf()
   FUNCTION = int(function_type)

   A = float(a)
   B = float(b)
   C = float(c)
   D = float(d)


   xMin = float(xmin)
   xMax = float(xmax)

   NUM_RECT = int(rct_amnt)

   if width_rect == "0":
      DELTA_X = float(wdth_amnt)
   else:
      DELTA_X = (xMax - xMin) / NUM_RECT

   SUM_TYPE = int(sum_type)

   if SUM_TYPE < 4:
      xList= np.arange(xMin, xMax, INCREASE)
      yList = createYList(xList, FUNCTION, A, B, C, D)
   else:
      xSimp= np.arange(xMin, xMax+1, INCREASE)
      ySimp = createYList(xSimp, FUNCTION, A, B, C, D)

      xList= np.arange(xMin, xMax, INCREASE)
      yList = createYList(xList, FUNCTION, A, B, C, D)

   if SUM_TYPE == 3:
      sum = riemannTrap(yList, DELTA_X, xMin)
   elif SUM_TYPE < 3:
      sum = riemann(yList, NUM_RECT, xMin, xMax, SUM_TYPE)
   else:
      sum = simp(ySimp, NUM_RECT, xMin, xMax)



   plt.axhline(y = 0, color='k') # x axis
   plt.axvline(x = 0, color='k') # y axis

   plt.plot(xList, yList, linewidth = 3)

   # zooming out
   plt.plot(xMin - INCREASE, 0)
   plt.plot(xMax + INCREASE, 0)
   plt.plot(0, max(yList) + INCREASE)
   plt.plot(0, min(yList) - INCREASE)

   plt.grid(True)


   fileDir = path.dirname(path.realpath(__file__))
   print(fileDir)

   epic_path = fileDir + "\static\img\graphTest3.png"
   print("epic path: %s" % epic_path)

   plt.savefig(epic_path)
   


   try:
        file = open("output.txt", mode = 'w') # opens output file
        file.write(str(sum))
   finally:
        file.close()

   if(sum == -0):
      sum = 0.0
   return sum

def createYList(xList, type, A, B, C, D):
   # A = float(input("\nA? "))
   # B = float(input("B? "))
   #if type != "LINEAR" and type != "E" and type != "":
      #C = float(input("C? "))
      #if type == "CUBIC" or type == "SINE" or type == "COSINE":
         #D = float(input("D? "))

   if type == 0: # LINEAR
      yList = A * xList + B
   elif type == 1: # QUAD
      yList = A * xList * xList + B * xList + C
   elif type == 2: # CUBIC
      yList = A * xList * xList * xList + B * xList * xList + C * xList + D
   elif type == 3: # SINE
      yList = A * np.sin(B * xList + C) + D
   elif type == 4: # COSINE
      yList = A * np.cos(B * xList + C) + D
   elif type == 5: # E
      yList = A * math.e ** xList + B
   elif type == 6: # natural log
      yList = A * np.log(xList) + B
   else:
      yList = A*((xList-B)**2) + C # vertex form for parabola

   return yList

def riemann(yList, rectNum, xMin, xMax, type):
   deltaX = (xMax-xMin)/rectNum

   delta =  int(deltaX / INCREASE)
   factor = 10000
   
   sum = 0

   leftSum = 0
   rightSum = 0

   riemannX = []
   riemannY = []

   for i in range(0, len(yList) // delta):
      sum += yList[i * delta] * deltaX # sum calculation

      # rectangle graphing
      riemannX.append(i * deltaX + xMin)
      riemannY.append(0)

      if type == 0: # Left
         val = yList[delta * i]
      elif type == 1: # Right
         if i == len(yList) / delta - 1:
            val = yList[delta * (i + 1) - 1] # last rectangle
         else:
            val = yList[delta * (i + 1)]
      else: # Mid
         val = yList[delta * i + delta // 2]

      riemannX.append(i * deltaX + xMin)
      riemannY.append(val)
      riemannX.append((i + 1) * deltaX + xMin)
      riemannY.append(val)

   # adds last point
   riemannX.append((i + 1) * deltaX + xMin)
   riemannY.append(0)

   leftSum = sum

   if type == 1 or type == 2: # right or midpoint
      sum -= yList[0] * deltaX
      sum += yList[len(yList) - 1] * deltaX
      rightSum = sum
   

   plt.plot(riemannX, riemannY)

   if type == 0: # left
      return round(leftSum, 3)
      # print("\nThe left endpoint sum is: " + str(round(leftSum, 3)))
   elif type == 1: # right
      return round(rightSum, 3)
      # print("\nThe right endpoint sum is: " + str(round(rightSum, 3)))
   else: # Mid
      #midpoint is average of left and right sums
      midsum = 0
      for i in range(0, rectNum):
         midsum += yList[int(factor*(deltaX*i+deltaX/2))] * deltaX
         sum = midsum
      return round(sum, 3)
      # print("\nThe midpoint sum is: " + str(round((rightSum + leftSum) / 2 , 3)))

def riemannTrap(yList, deltaX, xMin):
   delta =  int(deltaX / INCREASE)

   #print("deltaX: " + str(deltaX))
   sum = 0

   riemannX = []
   riemannY = []

   for i in range(0, len(yList) // delta - 1):
      # area trapezoid = 0.5 * (base1 + base2) * height
      sum += 0.5 * (yList[i * delta] + yList[(i + 1) * delta]) * deltaX # sum calcs
      #print("sum" + str(sum))
      riemannX.append(i * deltaX + xMin) # rectangle graphing
      riemannY.append(0)
      riemannX.append(i * deltaX + xMin)
      riemannY.append(yList[i * delta])
      val = yList[(i + 1) * delta]
      riemannX.append((i + 1) * deltaX + xMin)
      riemannY.append(val)

   # adds on values that are left out of main loop to sum
   sum += 0.5 * (yList[len(yList) - delta] + yList[len(yList) - 1]) * deltaX

   # adds on values that are left out of main loop to riemann series
   i += 1
   riemannX.append(i * deltaX + xMin)
   riemannY.append(0)
   riemannX.append(i * deltaX + xMin)
   riemannY.append(yList[i * delta])
   val = yList[(i + 1) * delta - 1]
   riemannX.append((i + 1) * deltaX + xMin)
   riemannY.append(val)
   riemannX.append((i + 1) * deltaX + xMin)
   riemannY.append(0)

   plt.plot(riemannX, riemannY)

   # print("\nThe trapezoidal sum is: " + str(round(sum, 3)))
   return round(sum, 3)



   # adds last point

def interpolate(xList, a, b, c, d, e, f):
    #lagrange interpolation for n=3 making a polynomial of degree n-1
    yList = b * ((xList-c)*(xList-e))/((a-c)*(a-e)) + d * ((xList-a)*(xList-e))/((c-a)*(c-e)) + f * ((xList-a)*(xList-c))/((e-a)*(e-c))
    return yList

def simp(yList, rectNum, xMin, xMax):
    
   #f(0)=list(10000)
   sum = 0

   halvedRect = rectNum//2

   deltaX = float((xMax - xMin) / halvedRect)
    
   deltaXL = float((xMax - xMin) / rectNum)

   delta =  int(deltaXL / INCREASE)

   for i in range(1, halvedRect+1):
      simpX = np.arange(xMin+deltaX*(i-1), xMin+deltaX*i, INCREASE)
      factor = 10000

        #left point
      a=float(xMin+deltaX*(i-1))
      b=float(yList[int(factor*deltaX*(i-1))])
        
        #mid point
      c=float(xMin+deltaX*(i-1)+(deltaX)/2)
      d=float(yList[int(factor*(deltaX*(i-1)+(deltaX)/2))])

        #right point
      e=float(xMin+deltaX*i)
      f=float(yList[int(factor*deltaX*i)])
    
      simpY = interpolate(simpX, a, b, c, d, e, f)

      plt.plot(simpX, simpY, color='red')
        
        #rule of 1/4/1
      sum += deltaXL/3 * (b + 4*d + f)

      for i in range(0, rectNum+1):
         riemannX = []
         riemannY = []
      # rectangle graphing
         riemannX.append(i * deltaXL + xMin)
         riemannY.append(0)

         val = yList[delta * i]

         riemannX.append(i * deltaXL + xMin)
         riemannY.append(val)

         plt.plot(riemannX, riemannY, color='red')

   sum = round(sum, 3)
   return sum
   