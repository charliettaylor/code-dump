import os
import pprint as pp

coords = open("coords.txt", "r")
coordinates = []
connectors = []
cableID = []
#it usually goes connector id cable id (actual conn id) (actual cable ids)

def splitConnectors():
    '''gets txt file and splits it'''
    splitStuff = coords.read()
    '''
    while index < length:
	if newL[index].isnumeric():
		newL.pop(index)
		length -= 1
	else:
		index += 1
    '''
    splitStuff = splitStuff.split('\n')
    
    return splitStuff.split('\n')

def readData(data: list):
    '''parses through list to make conn list'''
    count = 0
    temp = []
    found = False
    for word in data:
        if word == "CABLE_ID":
            found = True
            if not temp.empty():
                cableID.append(temp)
                temp.clear()
        if found:
            connector.append(word)
            found = False
        if 'C' in word and word[1:len(word)].isnumeric():
            temp.append(word)

#USER INPUT FOR COORDINATES
def inputCoords():
    for i in range(0, len(connectors)):
        coordinates.append(input("Enter the coordinate for " + connectors[i] + ": "))
    
# 'main' function, just loops asking what you want to search for
def main():
    inputCoords()
    search = ''
    while(search != "done"):
        search = input("Enter the connector you'd like to label (Type done to end) : ")
        getCoords(connectors, cableID, coordinates, search)


#name is the connector we're dealing with
def getCoords(connectors, cableID, coordinates, name):
#looks through connectors and sets connectorNum = the index of the connector
    count = 0
    for names in connectors:
        if names == name:
            connectorNum = count
        count += 1

    if(name != 'done'):
        print(connectors[connectorNum])
        print(cableID[connectorNum])
        print(coordinates[connectorNum])
#so now that connectors has all of the names of the connectors and each index is matched to its cable IDs
#in the cableID array, we can associate a coordinate with each connector
#make data structure so that each cable id is associated with its connector

pp.pprint(splitConnectors())
