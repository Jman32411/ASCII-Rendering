import os
import time
import math

# 113 x 53 character box
# 0, 0 at top left and 113, 53 bottom right


fullGraph = []
xCoordinates = [-6, -6, 6, 6, 0]
yCoordinates = [-6, 6, -6, 6, 0]
graphWidth = 31

def createEmptySquareGraph(graphWidth):
    height = (53/113)*graphWidth
    xAxis = " " * graphWidth
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
        graph[yCoordinate] = graph[yCoordinate][:xCoordinates[index]-1] + "@" + graph[yCoordinate][xCoordinates[index]:]

def drawGraph(graph):
    os.system('cls||clear')
    for yAxis in graph:
        print(yAxis)

createEmptySquareGraph(graphWidth)
print(f"Original X Coordinates: {xCoordinates}\nOriginal Y Coordinates: {yCoordinates}")
convertCoordinates(xCoordinates, yCoordinates, graphWidth)
print(f"New X Coordinates: {xCoordinates}\nNew Y Coordinates: {yCoordinates}")
placeCoordinates(xCoordinates, yCoordinates, fullGraph)
for counter in range(0, 1000):
    drawGraph(fullGraph)
    print(counter)
    time.sleep(0.05)
