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


graphWidth = 113
graphHeight = 113

def createShape(shape, width, height, centerX, centerY):
    width = abs(round(width))
    height = abs(round(height))
    centerX = abs(round(centerX))
    centerY = abs(round(centerY))
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
                y = -k+math.sqrt((r**2)-(x**2)+(2*h*x)-(h**2))
                xCoordinates.append(round(x))
                xCoordinates.append(round(x))
                yCoordinates.append(round(y))
                y = -k-math.sqrt((r**2)-(x**2)+(2*h*x)-(h**2))
                yCoordinates.append(round(y))

    elif shape == "ellipse":
    # Equation if a>b (wide): (((x−h)^2)/a^2) + (((y−k)^2)/b^2) = 1
    # Equation if a<b (tall): (((x−h)^2)/b^2) + (((y−k)^2)/a^2) = 1
        h = centerX
        k = centerY
        a = width
        b = height
        for xValue in range(int(-a), int(a)):
            for decimal in range(0, precision):
                if a > b:
                    # print(h+xValue+(decimal/precision))
                    x = h+xValue+(decimal/precision)
                    # print(math.sqrt((r**2)-((x-h)**2))+k)
                    y = -k+((b*math.sqrt((a**2)-(h**2)+(2*h*x)-(x**2)))/a)
                    xCoordinates.append(round(x))
                    xCoordinates.append(round(x))
                    yCoordinates.append(round(y))
                    y = -k-((b*math.sqrt((a**2)-(h**2)+(2*h*x)-(x**2)))/a)
                    yCoordinates.append(round(y))
                elif a == b:
                    # print(h+xValue+(decimal/precision))
                    x = h+xValue+(decimal/precision)
                    # print(math.sqrt((r**2)-((x-h)**2))+k)
                    y = -k+math.sqrt((a**2)-(x**2)+(2*h*x)-(h**2))
                    xCoordinates.append(round(x))
                    xCoordinates.append(round(x))
                    yCoordinates.append(round(y))
                    y = -k-math.sqrt((a**2)-(x**2)+(2*h*x)-(h**2))
                    yCoordinates.append(round(y))
                else:
                    # print(h+xValue+(decimal/precision))
                    x = h+xValue+(decimal/precision)
                    # print(math.sqrt((r**2)-((x-h)**2))+k)
                    y = -k+((a*math.sqrt((b**2)-(h**2)+(2*h*x)-(x**2)))/b)
                    xCoordinates.append(round(x))
                    xCoordinates.append(round(x))
                    yCoordinates.append(round(y))
                    y = -k-((a*math.sqrt((b**2)-(h**2)+(2*h*x)-(x**2)))/b)
                    yCoordinates.append(round(y))

                
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
                    yCoordinates.append(round(y))
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
        graph[yCoordinate] = graph[yCoordinate][:xCoordinates[index]-1] + "@" + graph[yCoordinate][xCoordinates[index]:]
        # graph[yCoordinate] = graph[yCoordinate][:xCoordinates[index]-1] + "·" + graph[yCoordinate][xCoordinates[index]:]

def render(graph, frameNum):
    os.system('cls||clear')
    print(frameNum)
    for yAxis in graph:
        print(yAxis)
    


# createNewGraph(graphWidth, graphHeight)

# # createShape("rectangle", 14, 14, 10, 14)
# createShape("circle", 10, 10, 4, 4)
# # createShape("ellipse", 48, 25, 0, 0)

# # print(f"Original X Coordinates: {xCoordinates}\nOriginal Y Coordinates: {yCoordinates}")
# convertCoordinates(xCoordinates, yCoordinates, graphWidth, graphHeight)
# # print(f"New X Coordinates: {xCoordinates}\nNew Y Coordinates: {yCoordinates}")
# placeCoordinates(xCoordinates, yCoordinates, fullGraph)
# for counter in range(0, 1000):
#     drawGraph(fullGraph)
#     print(counter)
#     time.sleep(0.05)



for frameNum in range(0, 1000):
    start = time.time()
    fullGraph = []
    xCoordinates = []
    yCoordinates = []
    createNewGraph(graphWidth, graphHeight)
    createShape("ellipse", 35, 35*math.sin(frameNum/5), 0, 0)
    # createShape("rectangle", 40, 40*math.sin(frameNum/5), 0, 0)
    convertCoordinates(xCoordinates, yCoordinates, graphWidth, graphHeight)
    placeCoordinates(xCoordinates, yCoordinates, fullGraph)
    render(fullGraph,frameNum)
    end = time.time()
    if (end-start) < 0.05:
        time.sleep((end-start))