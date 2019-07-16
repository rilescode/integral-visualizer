import numpy as np
import matplotlib.pyplot as plt
import math

INCREASE = 0.001

xMin = 0
xMax = 0
A = 0 
B = 0
C = 0

def main():
   xMin= float(input("Enter a value for the first x-coordinate: "))
   xMax= float(input("Enter a value for the second x-coordinate: "))

   xArray= np.arange(xMin, xMax, INCREASE)
   yArray = createYArray(xArray, "QUAD")  # graphs function
   
   while(True):
      userInput = input("Width enter 0, Rectangles enter 1 \n")
      if userInput == 0:
         width = True
         break
      elif userInput == 1:
         width = False
         break
      else:
         print("Error: Answer must be 0 or 1")
    
   plt.plot(xArray, yArray)
   plt.grid(True)
   
   if width == True:
      deltaX = float(input("Enter a value for the change in X: ")) 
   else:
      numRect = float(input("Enter the number of rectangles: ")) 
      deltaX = (xMax - xMin) / numRect
      print(deltaX)
    
   riemann(yArray, deltaX, xMin, width)

   plt.axvline(x = 0, color='k')
   plt.axhline(y = 0, color='k')

   plt.show()


def createYArray(xArray, type):
   if type == "LINEAR" or type == "QUAD":
      A = float(input("A? "))
      B = float(input("B? "))
      if type == "QUAD":
         C = float(input("C? "))  
         yArray = A * xArray * xArray + B * xArray + C
      else:
         yArray = A * xArray + B 
   elif type == "SINE":
      yArray = np.sin(xArray)
   elif type == "COSINE": 
      yArray = np.cosine(xArray)
   elif type == "E":
      yArray = math.e ** xArray
   else: # natural log
      yArray = math.log(xArray)
   
   return yArray
   
def riemann(yArray, deltaX, xMin, width):
   delta =  int(deltaX / INCREASE)  
   
   print(delta)
   
   sum = 0
   leftSum = 0 
   rightSum = 0 
   
   riemannX = []
   riemannY = [] 
   
   i = 0 
   while (i < len(yArray) / delta):
      sum += yArray[i * delta] * deltaX # sum calculation
       
      # draws rectangles
      riemannX.append(i * deltaX + xMin)
      riemannY.append(0)
      val = yArray[delta * i]
      riemannX.append(i * deltaX + xMin)
      riemannY.append(val)
      riemannX.append((i + 1) * deltaX + xMin)
      riemannY.append(val)
        
      i += 1
   
   if width == True: # adds last point
      riemannX.append(i * deltaX + xMin)
      riemannY.append(0) 
   
   plt.plot(riemannX, riemannY)
   
   leftSum = round(sum + yArray[0] * deltaX, 3)
   print(leftSum)
        
main() 
       


