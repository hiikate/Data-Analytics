#!/usr/bin/env python3
from math import sqrt
import sys
from getopt import getopt, GetoptError
import numpy

verboseMode = False

class Row(object):
    def __init__(self, myList):
        self.data = []
        for c in myList:
            self.data.append(c)

    def __str__(self):
        return str(self.data)

    def rotateLeft(self, amount):
        amount = amount % len(self.data)
        temp = [None]*len(self.data)
        for index in range(len(self.data)):
            temp[index] = self.data[(index + amount) % len(self.data)]
        return temp

    def reverse(self):
        temp = [None]*len(self.data)
        for index in range(len(self.data)):
            temp[index] = self.data[len(self.data)-index-1]
        return temp

class Block(object):
    rowLength = None
    rows = None
    size = None
    def __init__(self, size):
        self.rowLength = int(sqrt(size))
        if size != self.rowLength*self.rowLength:
            print (size, " is NOT a perfect square")
            sys.exit(1)
        self.rows = [None]*self.rowLength
        self.size = size

    def __str__(self):

        retValue = ''
        for r in self.rows:
            if verboseMode:
                print(r)
        return retValue

    def phaseTwoHash(self):
        """
        Converts the lists of rows into an array of indices.
        """
        m = numpy.arange(self.size).reshape(self.rowLength, self.rowLength)
        index = 0
        rowIndex = 0
        for row in self.rows:
            if index < self.rowLength-1:
                index += 1
                row = row.rotateLeft(index)
            else:
                row = row.reverse()

            numericalList = [int]*self.rowLength

            i = 0
            for el in row:
                value = ord(el) - ord('A')
                numericalList[i] = value
                i += 1

            m[rowIndex] = numericalList
            rowIndex += 1
        if verboseMode:
            print ('Phase two compressor matrix: ')
            print (m)

        retVal = [None]*self.rowLength
        columnIndex = 0
        for row in m.T:
            r = row
            total = 0
            for el in r:
                total += el
            total = total % 26
            retVal[columnIndex] = total
            columnIndex += 1
        return retVal

    def phaseOneHash(self):
        m = numpy.arange(self.size).reshape(self.rowLength, self.rowLength)
        rowIndex = 0
        for row in self.rows:
            numericalList = [int]*self.rowLength

            i = 0

            for el in row.data:
                value = ord(el) - ord('A')
                numericalList[i] = value
                i += 1

            m[rowIndex] = numericalList
            rowIndex += 1

        if verboseMode:
            print ('Phase one compressor matrix: ')
            print (m)

        retVal = [None]*self.rowLength
        columnIndex = 0
        for row in m.T:
            x = row
            total = 0
            for el in x:
                total += el
            total = total % 26
            #retVal[columnIndex] = chr(total+ord('A'))
            retVal[columnIndex] = total
            columnIndex += 1
        return retVal


    def addData(self, messageBuffer):

        tempMessage = messageBuffer.upper()
        if len(messageBuffer) == 0:
            print ("Empty Message")
            sys.exit(1)

        tempRow = ['']*self.rowLength
        rowIndex = 0
        rowCounter = 0
        characterCounter = 0
        examinedCounter = 0
        #If there are fewer usable characters
        #in a message than a blocksize, pad
        #with 'A's.

        for c in tempMessage:
            examinedCounter += 1

            if c.isalpha():
                characterCounter += 1
                #print 'counter = ', characterCounter
                tempRow[rowIndex] = c
                rowIndex += 1
                if rowIndex == self.rowLength:
                    #print "filled temporary row: ", tempRow
                    self.rows[rowCounter] = Row(tempRow)
                    rowIndex = 0
                    rowCounter += 1
                    tempRow = ['']*self.rowLength

            if characterCounter == self.size:
                break

        if characterCounter == 0:
            return ''

        retVal = messageBuffer[examinedCounter:]
        while characterCounter < self.size:
            characterCounter += 1
            tempRow[rowIndex] = 'A'
            rowIndex += 1
            if rowIndex == self.rowLength:
	    #print "filled temporary row: ", tempRow
                self.rows[rowCounter] = Row(tempRow)
                rowIndex = 0
                rowCounter += 1
                tempRow = ['']*self.rowLength

        return retVal

def addHashes(h1, h2):
    retValue = [int]*len(h1)
    for index in range(len(h1)):
        retValue[index] = (h1[index] + h2[index]) % 26
    return retValue

def Hash(myMessage):
    """Computes the hash of a given message
    """
    block = Block(16)
    hashValue = [0, 0, 0, 0]
    blockCounter = 1

    while myMessage != '':
        myMessage = block.addData(myMessage)
        if verboseMode:
            print ('block number: ' +str(blockCounter))
        blockCounter += 1
        if verboseMode:
            print (block)
        h = block.phaseOneHash()
        hashValue = addHashes(h, hashValue)
        if verboseMode:
            print ('round 1 hash')
            print (h)
        h = block.phaseTwoHash()
        if verboseMode:
            print ('round 2 hash')
            print (h)
        hashValue = addHashes(h, hashValue)
        if message == '':
            break

    thisHash = ['']*block.rowLength
    index = 0
    for h in hashValue:
        element = chr(h + ord('A'))
        thisHash[index] = element
        index += 1
    return thisHash

if __name__ == "__main__":

    def usage(name):
        print (name + " -h | -i inputFileName [-o outputFileName]")

    programName = sys.argv[0]

    try:
        opts, args = getopt(sys.argv[1:], "vhi:o:", ["help", "output="])
    except GetoptError as err:
        # print help information and exit:
        print (str(err))  # will print something like "option -a not recognized"
        usage(programName)
        sys.exit(2)
    outFile = None
    inFile = None
    for opt, a in opts:
        if opt in ("-o", "--output"):
            outFile = a
        elif opt in ("-h", "--help"):
            usage(programName)
            sys.exit()
        elif opt in ("-v",):
            print ("using verbose mode")
            verboseMode = True
        elif opt in ("-i", "--input"):
            inFile = a
        else:
            assert False, "unhandled option"

    if inFile == None:
        print ("No input file specified")
        usage(programName)
        sys.exit(1)
    #Acquire the message from the given file
    myFile = open(inFile, 'r')
    message = ''
    for line in myFile:
        if line.startswith('#'):
            continue
        message += line.strip()
    myFile.close()

    # Compute the hash of this message
    result = Hash(message)
    hashValue=str("")
    for letter in result:
        hashValue += letter

    if outFile != None:
        outputFile = open(outFile, 'w')
        outputFile.write(hashValue)
        outputFile.write("\n")
    else:
        print (hashValue)
