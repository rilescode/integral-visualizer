# Vidisha Gupta 
# 7/23/19

import numpy as np
import matplotlib.pyplot as plt
import math

INCREASE = 0.0001 # do not change! 

theInput = []

try: 
   f = open("input.txt", mode = 'r') # opens input file
   theInput = [line.rstrip('\n') for line in f] # cleans up line and puts into input list
finally: 
   f.close() 

FUNCTION = int(theInput[0])

A = float(theInput[1]) 
B = float(theInput[2]) 
C = float(theInput[3]) 
D = float(theInput[4])

xMin = float(theInput[5]) 
xMax = float(theInput[6]) 

NUM_RECT = int(theInput[8]) 

if theInput[7] == "0": 
   DELTA_X = float(theInput[10]) 
else: 
   DELTA_X = (xMax - xMin) / NUM_RECT 

SUM_TYPE = int(theInput[9])

def execute(): 
   xList= np.arange(xMin, xMax, INCREASE) 
   yList = createYList(xList, FUNCTION, A, B, C, D) 
                 
   if SUM_TYPE == 3: 
      sum = riemannTrap(yList, DELTA_X, xMin)
   else:
      sum = riemann(yList, DELTA_X, xMin, SUM_TYPE) 
          
   plt.axhline(y = 0, color='k') # x axis
   plt.axvline(x = 0, color='k') # y axis 
   
   plt.plot(xList, yList, linewidth = 3)
   
   # zooming out 
   plt.plot(xMin - INCREASE, 0)
   plt.plot(xMax + INCREASE, 0)
   plt.plot(0, max(yList) + INCREASE)
   plt.plot(0, min(yList) - INCREASE)
   
   plt.grid(True)
   plt.savefig("graph.jpg", bbox_inches = 'tight', pad_inches = 0)
   plt.show()
   
   try: 
        file = open("output.txt", mode = 'w') # opens output file
        file.write(str(sum))
   finally: 
        file.close()
        
   return sum 
        
def createYList(xList, type, A, B, C, D):
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
   else: # natural log
      yList = A * np.log(xList) + B
   
   return yList
   
def riemann(yList, deltaX, xMin, type):
   delta =  int(deltaX / INCREASE)  
    
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
   elif type == 1: # right
      return round(rightSum, 3)
   else: # Mid
      #midpoint is average of left and right sums
      return round(((rightSum + leftSum) / 2), 3)

def riemannTrap(yList, deltaX, xMin):
   delta =  int(deltaX / INCREASE)  
   
   #print("deltaX: " + str(deltaX))
   sum = 0
      
   riemannX = []
   riemannY = []   

   for i in range(0, len(yList) // delta - 1):
      # area trapezoid = 0.5 * (base1 + base2) * height
      sum += 0.5 * (yList[i * delta] + yList[(i + 1) * delta]) * deltaX # sum calcs
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
         

print(execute())
