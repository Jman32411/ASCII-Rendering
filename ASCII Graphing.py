import os
import time
import math

# 113 x 53 character box
# 0, 0 at top left and 113, 53 bottom right

# Gradient Source: https://stackoverflow.com/a/74186686
shade = ["@", "&", "%", "Q", "W", "N", "M", "0", "g", "B", "$", "#", "D", "R", "8", "m", "H", "X", "K", "A", "U", "b", "G", "O", "p", "V", "4", "d", "9", "h", "6", "P", "k", "q", "w", "S", "E", "2", "]", "a", "y", "j", "x", "Y", "5", "Z", "o", "e", "n", "[", "u", "l", "t", "1", "3", "I", "f", "}", "C", "{", "i", "F", "|", "(", "7", "J", ")", "v", "T", "L", "s", "?", "z", "/", "*", "c", "r", "!", "+", "<", ">", ";", "=", "^", ",", "_", ":", "'", "-", ".", "`"]
fullGraph = []
# xCoordinates = [-6, -6, 6, 6, 0]
# yCoordinates = [-6, 6, -6, 6, 0]
xCoordinates = []
yCoordinates = []


graphWidth = 31
graphHeight = 31

def createShape(shape, width, height, centerX, centerY):
    precision = (width+height)
    # print(shape)
    if width > math.floor(graphWidth/2)-1 or height > math.floor(graphHeight/2)-1:
        print(f"SHAPE {shape} IS TOO LARGE!\nTHIS MEANS IT WILL SKIPPED WHEN GRAPHING")
        time.sleep(3)
        return()
    if shape == "circle":
        if width != height:
            print("THIS IS NOT A CIRCLE!\nTHIS MEANS IT WILL SKIPPED WHEN GRAPHING")
            time.sleep(3)
            return()
    # Equation: r^2 = (x-h)^2 + (y-k)^2
        h = centerX
        k = centerY
        r = width
        for xValue in range(int(-r), int(r)):
            for decimal in range(0, precision):
                # print(h+xValue+(decimal/precision))
                x = h+xValue+(decimal/precision)
                # print(math.sqrt((r**2)-((x-h)**2))+k)
                y = math.sqrt((r**2)-((x-h)**2))+k
                xCoordinates.append(round(x))
                xCoordinates.append(round(x))
                yCoordinates.append(round(y))
                yCoordinates.append(round(-y))

    elif shape == "ellipse":
    # Equation if h>k (wide): (((x−h)^2)/a^2) + (((y−k)^2)/b^2) = 1
    # Equation if h<k (tall): (((x−h)^2)/b^2) + (((y−k)^2)/a^2) = 1
        h = centerX
        k = centerY
        r = width
        for xValue in range(int(-r), int(r)):
            for decimal in range(0, precision):
                # print(h+xValue+(decimal/precision))
                x = h+xValue+(decimal/precision)
                # print(math.sqrt((r**2)-((x-h)**2))+k)
                y = math.sqrt((r**2)-((x-h)**2))+k
                xCoordinates.append(round(x))
                xCoordinates.append(round(x))
                yCoordinates.append(round(y))
                yCoordinates.append(round(-y))
                
    elif shape == "rectangle":
        h = centerX
        k = centerY
        width = width
        height = height
        for xValue in range(int(-width), int(width)+1):
            x = h+xValue
            if abs(xValue) == width:
                for yVal in range(int(-height),int(height)+1):
                    xCoordinates.append(round(x))
                    y = k+yVal
                    yCoordinates.append(round(yVal))
                continue
            xCoordinates.append(round(x))
            xCoordinates.append(round(x))
            y = k+height
            yCoordinates.append(round(y))
            y = k-height
            yCoordinates.append(round(y))

    else:
        print(f"THE SHAPE: {shape} DOES NOT CURRENTLY EXIST.")
        time.sleep(3)
        return()
    

def createNewGraph(graphWidth, graphHeight):
    height = (53/113)*graphHeight
    xAxis = " " * graphWidth
    # xAxis = "·" * graphWidth
    for _ in range(0, math.ceil(height)):
        fullGraph.append(xAxis)

def convertCoordinates(xCoordinates, yCoordinates, graphWidth, graphHeight):
    for coordinateNum, coordinate in enumerate(xCoordinates):
        xCoordinates[coordinateNum] = coordinate + math.floor(graphWidth/2)
    for coordinateNum, coordinate in enumerate(yCoordinates):
        yCoordinates[coordinateNum] = math.floor((coordinate + math.floor(graphHeight/2))*(53/113))

def placeCoordinates(xCoordinates, yCoordinates, graph):
    if len(xCoordinates) != len(yCoordinates):
        # Print color codes using ANSI: https://replit.com/talk/learn/ANSI-Escape-Codes-in-Python/22803#colours
        print("IT APPEARS THAT THERE IS AN ERROR!\nPLEASE CHECK AND MAKE SURE YOUR COORDINATES ARE IN MATCHING PAIRS!\nDUE TO THIS ERROR, NOTHING HAS BEEN ADDED TO THE GRAPH!")
        time.sleep(10)
        return()
    for index, yCoordinate in enumerate(yCoordinates):
        # graph[yCoordinate] = graph[yCoordinate][:xCoordinates[index]-1] + "@" + graph[yCoordinate][xCoordinates[index]:]
        graph[yCoordinate] = graph[yCoordinate][:xCoordinates[index]-1] + "·" + graph[yCoordinate][xCoordinates[index]:]

def drawGraph(graph):
    os.system('cls||clear')
    for yAxis in graph:
        print(yAxis)



createShape("rectangle", 14, 14, 0, 0)
createShape("circle", 14, 14, 0, 0)

createNewGraph(graphWidth, graphHeight)
print(f"Original X Coordinates: {xCoordinates}\nOriginal Y Coordinates: {yCoordinates}")
convertCoordinates(xCoordinates, yCoordinates, graphWidth, graphHeight)
print(f"New X Coordinates: {xCoordinates}\nNew Y Coordinates: {yCoordinates}")
placeCoordinates(xCoordinates, yCoordinates, fullGraph)
for counter in range(0, 1000):
    drawGraph(fullGraph)
    print(counter)
    time.sleep(0.05)
