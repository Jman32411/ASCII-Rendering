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

def createShape(shape, size, centerX, centerY, angle):
    if shape == "circle":
        h = centerX
        k = centerY
        r = size
        for xValue in range(int(-r), int(r)+1):
            x = h+xValue
            y = math.sqrt((r**2)-((x-h)**2))+k
            xCoordinates.append(round(x))
            xCoordinates.append(round(x))
            yCoordinates.append(round(y))
            yCoordinates.append((-y))

def createEmptySquareGraph(graphWidth):
    height = (53/113)*graphWidth
    xAxis = " " * graphWidth
    # xAxis = "·" * graphWidth
    for _ in range(0, math.ceil(height)):
        fullGraph.append(xAxis)

def convertCoordinates(xCoordinates, yCoordinates, graphWidth):
    for coordinateNum, coordinate in enumerate(xCoordinates):
        xCoordinates[coordinateNum] = coordinate + math.floor(graphWidth/2)
    for coordinateNum, coordinate in enumerate(yCoordinates):
        yCoordinates[coordinateNum] = math.floor((coordinate + math.floor(graphWidth/2))*(53/113))

def placeCoordinates(xCoordinates, yCoordinates, graph):
    if len(xCoordinates) != len(yCoordinates):
        # Print color codes using ANSI: https://replit.com/talk/learn/ANSI-Escape-Codes-in-Python/22803#colours
        print("IT APPEARS THAT THERE IS AN ERROR!\nPLEASE CHECK AND MAKE SURE YOUR COORDINATES ARE IN MATCHING PAIRS!\nDUE TO THIS ERROR, NOTHING HAS BEEN ADDED TO THE GRAPH!")
        return()
    for index, yCoordinate in enumerate(yCoordinates):
        graph[yCoordinate] = graph[yCoordinate][:xCoordinates[index]-1] + "·" + graph[yCoordinate][xCoordinates[index]:]

def drawGraph(graph):
    os.system('cls||clear')
    for yAxis in graph:
        print(yAxis)

createShape("circle", 14, 0, 0, 0)
createShape("circle", 5, 0, 0, 0)
createEmptySquareGraph(graphWidth)
print(f"Original X Coordinates: {xCoordinates}\nOriginal Y Coordinates: {yCoordinates}")
convertCoordinates(xCoordinates, yCoordinates, graphWidth)
print(f"New X Coordinates: {xCoordinates}\nNew Y Coordinates: {yCoordinates}")
placeCoordinates(xCoordinates, yCoordinates, fullGraph)
for counter in range(0, 1000):
    drawGraph(fullGraph)
    print(counter)
    time.sleep(0.05)
