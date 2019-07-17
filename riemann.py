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
   xMin= float(input("Enter a value for the first x-coordinate: "))
   xMax= float(input("Enter a value for the second x-coordinate: "))

   xArray= np.arange(xMin, xMax, INCREASE)
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
                break
        else:
                print("\nMust enter an integer between 1 and 6!")
                print("\n1. Linear \n2. Quadratic \n3. Sine \n4. Cosine \n5. e^x \n6. Natural log")
                func = int(input("\nWhich function do you want to graph? "))
                
   yArray = createYArray(xArray, function)  # graphs function
   
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
       
   if width == True:
      deltaX = float(input("Enter a value for the change in X: ")) 
   else:      
      numRect = float(input("Enter the number of rectangles: ")) 
      while True:
         if numRect >= 1:
            break
         else:
            print("Number of rectangles must be greater than or equal to 1")
            numRect = float(input("Enter the number of rectangles: "))      
      deltaX = (xMax - xMin) / numRect
      # print("\nDelta X: " + str(deltaX))
   
   type = int(input("Which type of sum? \n1. Left \n2. Right \n3. Midpoint \n4. Trapezodial\n"))
   while True:
      if type == 1: 
         riemann(yArray, deltaX, xMin, width, "Left")
         break
      elif type == 2: 
         riemann(yArray, deltaX, xMin, width, "Right")
         break
      elif type == 3: 
         riemann(yArray, deltaX, xMin, width, "Mid")
         break
      elif type == 4:
         riemannTrap(yArray, deltaX, xMin, width)
         break
      else: 
         print("Enter an integer between 1 and 4!")
         type = int(input("Which type of sum? \n1. Left \n2. Right \n3. Midpoint \n4.Trapezodial\n"))
        
   plt.axhline(y = 0, color='k') # x axis
   plt.axvline(x = 0, color='k') # y axis 
   
   plt.plot(xArray, yArray, linewidth = 3)
   
   plt.grid(True)
   plt.show()

def createYArray(xArray, type):
   if type == "LINEAR" or type == "QUAD":
      A = float(input("\nA? "))
      B = float(input("B? "))
      if type == "QUAD":
         C = float(input("C? "))  
         yArray = A * xArray * xArray + B * xArray + C
      else:
         yArray = A * xArray + B 
   elif type == "SINE":
      yArray = np.sin(xArray)
   elif type == "COSINE": 
      yArray = np.cos(xArray)
   elif type == "E":
      yArray = math.e ** xArray
   else: # natural log
      yArray = np.log(xArray)
   
   return yArray
   
def riemann(yArray, deltaX, xMin, width, type):
   delta =  int(deltaX / INCREASE)  
    
   sum = 0
   
   leftSum = 0 
   rightSum = 0 
   
   riemannX = []
   riemannY = [] 
 
   for i in range(0, len(yArray) / delta):      
      sum += yArray[i * delta] * deltaX # sum calculation
       
      # rectangle graphing
      riemannX.append(i * deltaX + xMin)
      riemannY.append(0)
      
      if type == "Left":
         val = yArray[delta * i]
      elif type == "Right":
         if i == len(yArray) / delta - 1:
            val = yArray[delta * (i + 1) - 1] # last rectangle
         else: 
            val = yArray[delta * (i + 1)]
      else: # Mid
         val = yArray[delta * i + delta / 2]  
      
      riemannX.append(i * deltaX + xMin)
      riemannY.append(val)
      riemannX.append((i + 1) * deltaX + xMin)
      riemannY.append(val)
   
   # adds last point
   riemannX.append((i + 1) * deltaX + xMin)
   riemannY.append(0) 
   
   leftSum = sum

   if type == "Right" or type == "Mid": 
        sum -= yArray[0] * deltaX
        sum += yArray[len(yArray) - 1] * deltaX
        rightSum = sum
   if type == "Left":
        print("The left endpoint sum is: " + str(round(leftSum, 2)))
   elif type == "Right": 
        print("The right endpoint sum is: " + str(round(rightSum, 2)))
   else: # Mid
        #midpoint is average of left and right sums
        print("The midpoint sum is: " + str(round((rightSum + leftSum) / 2 , 2)))   
   
   plt.plot(riemannX, riemannY)
   

def riemannTrap(yArray, deltaX, xMin, width):
   delta =  int(deltaX / INCREASE)  
   
   print("deltaX: " + str(deltaX))
   sum = 0
      
   riemannX = []
   riemannY = []   

   for i in range(0, len(yArray) / delta - 1):
      # area trapezoid = 0.5 * (base1 + base2) * height
      sum += 0.5 * (yArray[i * delta] + yArray[(i + 1) * delta]) * deltaX # sum calcs
      print("sum" + str(sum))   
      riemannX.append(i * deltaX + xMin) # rectangle graphing
      riemannY.append(0)
      riemannX.append(i * deltaX + xMin)
      riemannY.append(yArray[i * delta])
      val = yArray[(i + 1) * delta] 
      riemannX.append((i + 1) * deltaX + xMin)
      riemannY.append(val)
         
   # adds on values that are left out of main loop to sum 
   sum += 0.5 * (yArray[len(yArray) - delta] + yArray[len(yArray) - 1]) * deltaX 
                    
   # adds on values that are left out of main loop to riemann series
   i += 1
   riemannX.append(i * deltaX + xMin)
   riemannY.append(0) 
   riemannX.append(i * deltaX + xMin) 
   riemannY.append(yArray[i * delta]) 
   val = yArray[(i + 1) * delta - 1]
   riemannX.append((i + 1) * deltaX + xMin)
   riemannY.append(val)
   riemannX.append((i + 1) * deltaX + xMin)
   riemannY.append(0) 
   
   plt.plot(riemannX, riemannY)

   print("Trapezoidal sum: " + str(round(sum, 2)))
         
main()