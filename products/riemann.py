# Vidisha Gupta, main script
# Mark Gross, simpson's rule
# 7/26/19

import matplotlib

matplotlib.use("Agg")  # Use non-interactive backend for web applications

import numpy as np
import matplotlib.pyplot as plt
import math
import os
import shutil
import platform
import io
import uuid
from vercel_blob import put

INCREASE = 0.0001  # do not change!


def calculateSum(
    function_type, a, b, c, d, xmin, xmax, wdth_rect, rct_amnt, wdth_amnt, sum_type
):
    """
    Calculates the riemann sum, creates the function, plots function and rectangles, and saves the plot to Vercel Blob

    Args:
       function_type (int): the function; eg: 0 = linear,  1 = quadratic, etc
       a (float): the "A" constant
       b (float): the "B" constant
       c (float): the "C" constant
       d (float): the "D" constant
       xmin (float): the minimum x value
       xmax (float): the maximum x value
       wdth-rect (int): whether user picked rectangles or width. 0 = width, 1 = rectangles.
       rct_amnt (int): the number of rectangles; selected by user if wdth_rect = 0
       wdth_amnt (float): the width of the rectangles; selected by user if wdth_rect = 1
       sum_type (int): the type of sum; eg: 0 = left endpoint, 1 = right endpoint, etc

    Returns:
       tuple: (riemann_sum_calculation, graph_url)
    """

    plt.clf()  # Clears previous plot

    # CREATE THE FIGURE FIRST, BEFORE CALCULATIONS
    plt.figure(figsize=(10, 8))  # Set figure size
    plt.axhline(y=0, color="k")  # x axis
    plt.axvline(x=0, color="k")  # y axis

    FUNCTION = int(function_type)
    A = float(a)
    B = float(b)
    C = float(c)
    D = float(d)
    xMin = float(xmin)
    xMax = float(xmax)

    if wdth_rect == "0":
        DELTA_X = float(wdth_amnt)
        NUM_RECT = int((xMax - xMin) / DELTA_X)
    else:
        NUM_RECT = int(rct_amnt)
        DELTA_X = float((xMax - xMin) / NUM_RECT)

    SUM_TYPE = int(sum_type)

    # Creates the function
    if SUM_TYPE < 4:
        xList = np.arange(xMin, xMax, INCREASE)
        yList = createYList(xList, FUNCTION, A, B, C, D)
    else:
        xSimp = np.arange(xMin, xMax + 1, INCREASE)
        ySimp = createYList(xSimp, FUNCTION, A, B, C, D)
        xList = np.arange(xMin, xMax, INCREASE)
        yList = createYList(xList, FUNCTION, A, B, C, D)

    # Plot the function FIRST
    plt.plot(xList, yList, linewidth=3)

    # calculate sum (which will add rectangles to the existing plot)
    if SUM_TYPE == 3:
        sum_result = riemannTrap(yList, DELTA_X, xMin)
    elif SUM_TYPE < 3:
        sum_result = riemann(yList, NUM_RECT, xMin, xMax, SUM_TYPE)
    else:
        sum_result = simp(ySimp, NUM_RECT, xMin, xMax)

    # zooming out on graph
    plt.plot(xMin - INCREASE, 0)
    plt.plot(xMax + INCREASE, 0)
    plt.plot(0, max(yList) + INCREASE)
    plt.plot(0, min(yList) - INCREASE)

    plt.grid(True)

    # Save to buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")
    buffer.seek(0)

    # Generate unique filename using UUID
    filename = f"riemann_graph_{uuid.uuid4().hex}.png"

    try:
        blob = put(
            filename,
            buffer.getvalue(),
            {
                "access": "public",
                "contentType": "image/png",
                "addRandomSuffix": "False",  # prevents random suffixes
                "cacheControlMaxAge": "3600",  # Cache for 1 hour
            },
        )
        graph_url = blob.get("url")
        print(f"Graph uploaded successfully: {graph_url}")
    except Exception as e:
        print(f"Error uploading graph: {e}")
        graph_url = None
    finally:
        plt.clf()  # Clear the plot
        buffer.close()

    # bug adjustment ("don't worry about it")
    if sum_result == -0:
        sum_result = 0.0

    return sum_result, graph_url


def createYList(xList, type, A, B, C, D):
    """
    Generates y values for function.

    Args:
       variable (type): description
       xList (List): the x values
       type (int): function type; eg: 0 = linear, 1 = quadratic, etc
       A (float): the "A" constant
       B (float): the "B" constant
       D (float): the "D" constant
       D (float): the "D" constant
    Returns:
       List: the function
    """

    if type == 0:  # LINEAR
        yList = A * xList + B
    elif type == 1:  # QUAD
        yList = A * xList * xList + B * xList + C
    elif type == 2:  # CUBIC
        yList = A * xList * xList * xList + B * xList * xList + C * xList + D
    elif type == 3:  # SINE
        yList = A * np.sin(B * xList + C) + D
    elif type == 4:  # COSINE
        yList = A * np.cos(B * xList + C) + D
    elif type == 5:  # E
        yList = A * math.e**xList + B
    elif type == 6:  # natural log
        yList = A * np.log(xList) + B
    else:
        yList = A * ((xList - B) ** 2) + C  # vertex form for parabola

    return yList


def riemann(yList, rectNum, xMin, xMax, type):
    """
    Graphs the riemann rectangles for left, right, and midpoint sums

    Args:
       yList (list): the function
       rectNum (int): the number of rectangles
       xMin (float): the minimum x value
       xMax (float): the maximum x value
       type (int): sum type; eg: 0 = left, 1 = right, etc

    Returns:
       Float: the sum, rounded to 3 decimal places
    """

    deltaX = (xMax - xMin) / rectNum

    delta = int(deltaX / INCREASE)
    factor = 10000

    sum = 0

    leftSum = 0
    rightSum = 0

    riemannX = []
    riemannY = []

    for i in range(0, len(yList) // delta):
        sum += yList[i * delta] * deltaX  # sum calculation

        # rectangle graphing
        riemannX.append(i * deltaX + xMin)
        riemannY.append(0)

        if type == 0:  # Left
            val = yList[delta * i]
        elif type == 1:  # Right
            if i == len(yList) / delta - 1:
                val = yList[delta * (i + 1) - 1]  # last rectangle
            else:
                val = yList[delta * (i + 1)]
        else:  # Mid
            val = yList[delta * i + delta // 2]

        riemannX.append(i * deltaX + xMin)
        riemannY.append(val)
        riemannX.append((i + 1) * deltaX + xMin)
        riemannY.append(val)

    # adds last point
    riemannX.append((i + 1) * deltaX + xMin)
    riemannY.append(0)

    leftSum = sum

    if type == 1 or type == 2:  # right or midpoint
        sum -= yList[0] * deltaX
        sum += yList[len(yList) - 1] * deltaX
        rightSum = sum

    plt.plot(riemannX, riemannY, linewidth=1)

    if type == 0:  # left
        return round(leftSum, 3)
    elif type == 1:  # right
        return round(rightSum, 3)
    else:  # Mid
        midsum = 0
        for i in range(0, rectNum):
            midsum += yList[int(factor * (deltaX * i + deltaX / 2))] * deltaX
            sum = midsum
        return round(sum, 3)


def riemannTrap(yList, deltaX, xMin):
    """
    Graphs the trapezoids for trapezoidal rule

    Args:
       yList (List): the function
       deltaX (float): the width of each trapezoid
       xMin (float): the minimum x value

    Returns:
       Float: the sum, rounded to 3 decimal places
    """

    delta = int(deltaX / INCREASE)

    sum = 0

    riemannX = []
    riemannY = []

    for i in range(0, len(yList) // delta - 1):
        # area trapezoid = 0.5 * (base1 + base2) * height
        sum += 0.5 * (yList[i * delta] + yList[(i + 1) * delta]) * deltaX  # sum calcs
        # print("sum" + str(sum))
        riemannX.append(i * deltaX + xMin)  # rectangle graphing
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

    # print("/nThe trapezoidal sum is: " + str(round(sum, 3)))
    return round(sum, 3)


def interpolate(xList, a, b, c, d, e, f):
    """
    Creates a quadratic lagranage polynomial going through 3 points

    Args:
       xList (List): x value array
       a (float): x_1
       b (float): y_1
       c (float): x_2
       d (float): y_2
       e (float): x_3
       f (float): y_3

    Returns:
       List: the quadratic that goes through points (a, b),  (c, d) and (e, f)
    """

    # Lagrange interpolation for n=3 making a polynomial of degree n-1
    yList = (
        b * ((xList - c) * (xList - e)) / ((a - c) * (a - e))
        + d * ((xList - a) * (xList - e)) / ((c - a) * (c - e))
        + f * ((xList - a) * (xList - c)) / ((e - a) * (e - c))
    )

    return yList


def simp(yList, rectNum, xMin, xMax):
    """
    Simpsons rule approximation.

    Args:
       yList (List): y value array
       rectNum (int): the number of rectangles
       xMin (float): the minimum x value
       xMax (float): the maximum x value

    Returns:
       float: the sum, rounded to three decimal places
    """

    # f(0)=list(10000)
    sum = 0

    deltaX = float((xMax - xMin) / rectNum)

    deltaXL = float((xMax - xMin) / rectNum)

    delta = int(deltaXL / INCREASE)

    for i in range(1, rectNum + 1):
        simpX = np.arange(xMin + deltaX * (i - 1), xMin + deltaX * i, INCREASE)
        factor = 10000

        # left point
        a = float(xMin + deltaX * (i - 1))
        b = float(yList[int(factor * deltaX * (i - 1))])

        # mid point
        c = float(xMin + deltaX * (i - 1) + (deltaX) / 2)
        d = float(yList[int(factor * (deltaX * (i - 1) + (deltaX) / 2))])

        # right point
        e = float(xMin + deltaX * i)
        f = float(yList[int(factor * deltaX * i)])

        simpY = interpolate(simpX, a, b, c, d, e, f)

        plt.plot(simpX, simpY, color="red")

        # rule of 1/4/1
        sum += deltaXL / 3 * (b + 4 * d + f)

        for i in range(0, rectNum + 1):
            riemannX = []
            riemannY = []
            # rectangle graphing
            riemannX.append(i * deltaXL + xMin)
            riemannY.append(0)

            val = yList[delta * i]

            riemannX.append(i * deltaXL + xMin)
            riemannY.append(val)

            plt.plot(riemannX, riemannY, color="red")

    sum = round(sum, 3)

    return sum
