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

def createLine(startX, startY, endX, endY):
    startX = startX
    startY = startY
    endX = endX
    endY = endY
    if (endX-startX) != 0:
        slope = (endY-startY)/(endX-startX)
        distance = math.ceil(math.sqrt(((endX-startX)**2)+((endY-startY)**2)))
    else:
        distance = abs(endY-startY)
        if (endY-startY) < 0:
            slope = "Positive"
        else:
            slope = "Negative"
    if round(endX)-round(startX)>0:
        for xValue in range(0, round(endX)-round(startX)):
            for decimal in range(0, distance):
                x = startX + xValue + (decimal/distance)
                yIntercept = startY-(slope*startX)
                y = (slope * x) + yIntercept
                xCoordinates.append(round(x))
                yCoordinates.append(round(y))
    elif round(endX)-round(startX)<0:
        for xValue in range(round(endX)-round(startX), 0):
            for decimal in range(0, distance):
                x = startX + xValue + (decimal/distance)
                yIntercept = startY-(slope*startX)
                y = (slope * x) + yIntercept
                xCoordinates.append(round(x))
                yCoordinates.append(round(y))
    else:
        if slope == "Positive":
            for yValue in range(round(endY), round(startY)):
                xCoordinates.append(round(startX))
                yCoordinates.append(round(yValue))
        else:
            for yValue in range(round(startY), round(endY)):
                xCoordinates.append(round(startX))
                yCoordinates.append(round(yValue))


def createShape(shape, width, height, centerX, centerY):
    width = abs(round(width))
    height = abs(round(height))
    centerX = round(centerX)
    centerY = round(centerY)
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
        # graph[yCoordinate] = graph[yCoordinate][:xCoordinates[index]-1] + "@" + graph[yCoordinate][xCoordinates[index]:]
        graph[yCoordinate] = graph[yCoordinate][:xCoordinates[index]-1] + "·" + graph[yCoordinate][xCoordinates[index]:]

def render(graph, frameNum):
    os.system('cls||clear')
    print(frameNum)
    for yAxis in graph:
        print(yAxis)

def clock():
    createNewGraph(graphWidth, graphHeight)
    createShape("ellipse", 35, 35, 0, 0)
    createLine(0, 0, 20*math.cos(frameNum/10), 20*math.sin(frameNum/10))
    convertCoordinates(xCoordinates, yCoordinates, graphWidth, graphHeight)
    placeCoordinates(xCoordinates, yCoordinates, fullGraph)
    render(fullGraph,frameNum)

def flippingCircle():
    createNewGraph(graphWidth, graphHeight)
    createShape("ellipse", 35, 35*math.sin(frameNum/5), 0, 0)
    convertCoordinates(xCoordinates, yCoordinates, graphWidth, graphHeight)
    placeCoordinates(xCoordinates, yCoordinates, fullGraph)
    render(fullGraph,frameNum)

def goTo3D(x, y, z, fov, camX, camY, camZ):
    node = []
    node.append(fov*((x+camX)/(z+camZ)))
    node.append(fov*((y+camY)/(z+camZ)))
    return(node)

def drawCube(sideLen, fov, camX, camY, camZ):
    # SOURCE: https://scratch.mit.edu/projects/326624134/editor/
    vertecies = []
    vertecies.append(goTo3D(-sideLen, sideLen, 0*sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(sideLen, sideLen, 0*sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(sideLen, -sideLen, 0*sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(-sideLen, -sideLen, 0*sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(-sideLen, sideLen, 0*sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(-sideLen, sideLen, -sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(sideLen, sideLen, -sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(sideLen, sideLen, 0*sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(sideLen, sideLen, -sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(sideLen, -sideLen, -sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(sideLen, -sideLen, 0*sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(sideLen, -sideLen, -sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(-sideLen, -sideLen, -sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(-sideLen, -sideLen, 0*sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(-sideLen, -sideLen, -sideLen, fov, camX, camY, camZ))
    vertecies.append(goTo3D(-sideLen, sideLen, -sideLen, fov, camX, camY, camZ))
    createNewGraph(graphWidth, graphHeight)
    for index, coordPair in enumerate(vertecies):
        if index < len(vertecies)-1:
            createLine(coordPair[0], coordPair[1], list(vertecies[index+1])[0], list(vertecies[index+1])[1])
        else:
            createLine(coordPair[0], coordPair[1], list(vertecies[0])[0], list(vertecies[0])[1])
    convertCoordinates(xCoordinates, yCoordinates, graphWidth, graphHeight)
    placeCoordinates(xCoordinates, yCoordinates, fullGraph)
    render(fullGraph,frameNum)

fov = 30
camX = 0
camY = 0
camZ = 50
for frameNum in range(0, 50):
    start = time.time()
    fullGraph = []
    xCoordinates = []
    yCoordinates = []
    # flippingCircle()
    # clock()
    drawCube(20, fov, 10*math.sin(frameNum/10)+camX, 10*math.cos(frameNum/10)+camY, camZ)
    end = time.time()
    if (end-start) < 0.05:
        time.sleep((end-start))
for frameNum in range(0, 50):
    start = time.time()
    fullGraph = []
    xCoordinates = []
    yCoordinates = []
    # flippingCircle()
    # clock()
    drawCube(20, fov, frameNum+camX, camY, camZ)
    end = time.time()
    if (end-start) < 0.05:
        time.sleep((end-start))


# testList = [[1, 2], [3, 4], [5, 6], [7, 8]]
# for index, coordPair in enumerate(testList):
#     print(coordPair[1])
#     print(list(testList[index+1])[1])
# print("done")
