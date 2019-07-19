# Vidisha Gupta 
# 7/19/19

import numpy as np
import matplotlib.pyplot as plt
import math

INCREASE = 0.0001 # do not change! 

theInput = []

try:
   f = open("input.txt", mode = 'r')
   theInput = [line.rstrip('\n') for line in f]
finally: 
   f.close() 

#theInput = [1, 1, 0, 0, 0, -5, 5, False, 10, 0, 0.5]

FUNCTION = int(theInput[0])

A = float(theInput[1]) 
B = float(theInput[2]) 
C = float(theInput[3]) 
D = float(theInput[4])

xMin = float(theInput[5]) 
xMax = float(theInput[6]) 

if theInput[7] == "True": # temporary solution!!!!
   WIDTH = True
else:
   WIDTH = False

NUM_RECT = int(theInput[8]) 
   
SUM_TYPE = int(theInput[9])

#for i in range(0, len(theInput)):
 #       print(theInput[i])

if WIDTH:
   DELTA_X = theInput[10] 
else:
   DELTA_X = (xMax - xMin) / NUM_RECT 

def main(): 
   xList= np.arange(xMin, xMax, INCREASE) 
   yList = createYArray(xList, FUNCTION, A, B, C, D) 
                 
   if SUM_TYPE == 3: 
      riemannTrap(yList, DELTA_X, xMin)
   else:
      riemann(yList, DELTA_X, xMin, SUM_TYPE) 
          
   plt.axhline(y = 0, color='k') # x axis
   plt.axvline(x = 0, color='k') # y axis 
   
   plt.plot(xList, yList, linewidth = 3)
   
   plt.grid(True)
   plt.show()
        
def createYArray(xList, type, A, B, C, D):
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
 
   for i in range(0, len(yList) / delta):      
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
         val = yList[delta * i + delta / 2]  
      
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
      
   if type == 0: # left
      print("\nThe left endpoint sum is: " + str(round(leftSum, 3)))
   elif type == 1: # right
      print("\nThe right endpoint sum is: " + str(round(rightSum, 3)))
   else: # Mid
        #midpoint is average of left and right sums
      print("\nThe midpoint sum is: " + str(round((rightSum + leftSum) / 2 , 3)))   
   
   plt.plot(riemannX, riemannY)
   

def riemannTrap(yList, deltaX, xMin):
   delta =  int(deltaX / INCREASE)  
   
   #print("deltaX: " + str(deltaX))
   sum = 0
      
   riemannX = []
   riemannY = []   

   for i in range(0, len(yList) / delta - 1):
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

   print("\nThe trapezoidal sum is: " + str(round(sum, 3)))
         
def test():
   print("\n1. Linear \n2. Quadratic \n3. Cubic \n4. Sine \n5. Cosine \n6. e^x \n7. Natural log")
   func = int(input("\nWhich function do you want to graph? "))
   while True:
      if isInstance(func, int) and func != 7: 
         break
      elif func == 7:
         function = "" # Natural log 
         xMin = float(input("\nEnter a value for the first x-coordinate: "))
         while xMin <= 0: 
            print("\nThe minimum x value must be greater than 0!")
            xMin = float(input("\nEnter a value for the first x-coordinate: "))
      else:
         print("\nMust enter an integer between 1 and 7!")
         print("\n1. Linear \n2. Quadratic \n3. Cubic \n4. Sine \n5. Cosine \n6. e^x \n7. Natural log")
         func = int(input("\nWhich function do you want to graph? "))
   
   if func != 7:             
      xMin= float(input("Enter a value for the first x-coordinate: "))
   xMax= float(input("Enter a value for the second x-coordinate: "))
   while xMax <= xMin: 
      print("\nError: maximum x value greater than or equal to minimum x value. Please enter a bigger value.")
      xMax= float(input("\nEnter a value for the second x-coordinate: "))
        
   xList= np.arange(xMin, xMax, INCREASE) 
   yList = createYArray(xList, (func - 1), A, B, C, D)  # graphs function
   
   userInput = input("\nWidth enter 0, Rectangles enter 1: ")
   while(True):
      if userInput == 0:
         width = True
         break
      elif userInput == 1:
         width = False
         break
      else:
         print("Error: Answer must be 0 or 1")
         userInput = input("Width enter 0, Rectangles enter 1: ")
   
   maxWidth = xMax - xMin
   if width == True:
      deltaX = float(input("Enter a value for the change in X: ")) 
      while deltaX > maxWidth: 
         print("\nChange in x is larger than the domain! Please enter a smaller value.")
         deltaX = float(input("\nEnter a value for the change in X: ")) 
   else:      
      numRect = int(input("Enter the number of rectangles: ")) 
      while numRect <= 1:
         print("Number of rectangles must be greater than 1")
         numRect = int(input("Enter the number of rectangles: "))      
      deltaX = (xMax - xMin) / numRect
      # print("\nDelta X: " + str(deltaX))
   
   type = int(input("\nWhich type of sum? \n1. Left \n2. Right \n3. Midpoint \n4. Trapezodial\n"))
   while True:
      if type == 1: 
         riemann(yList, deltaX, xMin, "Left")
         break
      elif type == 2: 
         riemann(yList, deltaX, xMin, "Right")
         break
      elif type == 3: 
         riemann(yList, deltaX, xMin, "Mid")
         break
      elif type == 4:
         riemannTrap(yList, deltaX, xMin)
         break
      else: 
         print("\nEnter an integer between 1 and 4!")
         type = int(input("\nWhich type of sum? \n1. Left \n2. Right \n3. Midpoint \n4. Trapezodial\n"))
        
   plt.axhline(y = 0, color='k') # x axis
   plt.axvline(x = 0, color='k') # y axis 
   
   plt.plot(xList, yList, linewidth = 3)
   
   plt.grid(True)
   plt.show()

# test()
# to run test, adjustments are needed 

main()