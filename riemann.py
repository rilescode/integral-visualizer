import numpy as np
import matplotlib.pyplot as plt
import math

INCREASE = 0.0001

xMin = 0
xMax = 0
A = 0 
B = 0
C = 0

def main():
   print("\n1. Linear \n2. Quadratic \n3. Sine \n4. Cosine \n5. e^x \n6. Natural log")
   func = int(input("\nWhich function do you want to graph? "))
   while True:
      if func == 1: 
         function = "LINEAR"
         break
      elif func == 2: 
         function = "QUAD"
         break
      elif func == 3: 
         function = "SINE"
         break
      elif func == 4: 
         function = "COSINE"
         break
      elif func == 5: 
         function = "E"
         break
      elif func == 6:
         function = "" # Natural log 
         xMin = float(input("\nEnter a value for the first x-coordinate: "))
         while xMin <= 0: 
            print("\nThe minimum x value must be greater than 0!")
            xMin = float(input("\nEnter a value for the first x-coordinate: "))
      
         break
      else:
         print("\nMust enter an integer between 1 and 6!")
         print("\n1. Linear \n2. Quadratic \n3. Sine \n4. Cosine \n5. e^x \n6. Natural log")
         func = int(input("\nWhich function do you want to graph? "))
   if func != 6:             
      xMin= float(input("Enter a value for the first x-coordinate: "))
   
   xMax= float(input("Enter a value for the second x-coordinate: "))
   while xMax <= xMin: 
        print("\nError: maximum x value greater than or equal to minimum x value. Please enter a bigger value.")
        xMax= float(input("\nEnter a value for the second x-coordinate: "))
        
   xList= np.arange(xMin, xMax, INCREASE) 
   yList = createYArray(xList, function)  # graphs function
   
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
         riemann(yList, deltaX, xMin, width, "Left")
         break
      elif type == 2: 
         riemann(yList, deltaX, xMin, width, "Right")
         break
      elif type == 3: 
         riemann(yList, deltaX, xMin, width, "Mid")
         break
      elif type == 4:
         riemannTrap(yList, deltaX, xMin, width)
         break
      else: 
         print("\nEnter an integer between 1 and 4!")
         type = int(input("\nWhich type of sum? \n1. Left \n2. Right \n3. Midpoint \n4. Trapezodial\n"))
        
   plt.axhline(y = 0, color='k') # x axis
   plt.axvline(x = 0, color='k') # y axis 
   
   plt.plot(xList, yList, linewidth = 3)
   
   plt.grid(True)
   plt.show()

def createYArray(xList, type):
   if type == "LINEAR" or type == "QUAD":
      A = float(input("\nA? "))
      B = float(input("B? "))
      if type == "QUAD":
         C = float(input("C? "))  
         yList = A * xList * xList + B * xList + C
      else:
         yList = A * xList + B 
   elif type == "SINE":
      yList = np.sin(xList)
   elif type == "COSINE": 
      yList = np.cos(xList)
   elif type == "E":
      yList = math.e ** xList
   else: # natural log
      yList = np.log(xList)
   
   return yList
   
def riemann(yList, deltaX, xMin, width, type):
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
      
      if type == "Left":
         val = yList[delta * i]
      elif type == "Right":
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

   if type == "Right" or type == "Mid": 
      sum -= yList[0] * deltaX
      sum += yList[len(yList) - 1] * deltaX
      rightSum = sum
   if type == "Left":
      print("\nThe left endpoint sum is: " + str(round(leftSum, 2)))
   elif type == "Right": 
      print("\nThe right endpoint sum is: " + str(round(rightSum, 2)))
   else: # Mid
        #midpoint is average of left and right sums
      print("\nThe midpoint sum is: " + str(round((rightSum + leftSum) / 2 , 2)))   
   
   plt.plot(riemannX, riemannY)
   

def riemannTrap(yList, deltaX, xMin, width):
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

   print("\nThe trapezoidal sum is: " + str(round(sum, 2)))
         
main()