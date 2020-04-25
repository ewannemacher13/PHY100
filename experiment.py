# Elliot Wannemacher
# PHY 100 experiment

import time
import random
from datetime import datetime

NUM_TESTS = 500

def runTest(seq,seqType,cat,filename):
    times = [seqType + ': in']
    avgTime = 0
    for i in range(NUM_TESTS):
        totalTime = 0
        inStartTime = time.time()
        for i in range(1000000):
            'e' in seq
        inEndTime = time.time()
        totalTime += inEndTime-inStartTime
        times.append(totalTime)
        avgTime += totalTime

    print(seqType +" average 'in' time:",avgTime/NUM_TESTS)
    # with open("run"+str(datetime.strftime('%Y%d%j_%H%M%S')),'w') as f:
    with open(filename,'w') as f:
        for t in times:
            f.write(str(t) + ',')
        f.write(str(avgTime/NUM_TESTS) + '\n')


    times = [seqType + ': not in']
    avgTime = 0
    for i in range(NUM_TESTS):
        totalTime = 0
        inStartTime = time.time()
        for i in range(1000000):
            'e' not in seq
        inEndTime = time.time()
        totalTime += inEndTime-inStartTime
        times.append(totalTime)
        avgTime += totalTime

    print(seqType + " average 'not in' time:",avgTime/NUM_TESTS)
    # with open("run"+str(datetime.strftime('%Y%d%j_%H%M%S')),'w') as f:
    with open(filename,'a') as f:
        for t in times:
            f.write(str(t) + ',')
        f.write(str(avgTime/NUM_TESTS) + '\n')

    times = [seqType + ': concatenation']
    avgTime = 0
    for i in range(NUM_TESTS):
        totalTime = 0
        inStartTime = time.time()
        for i in range(1000000):
            seq + cat
        inEndTime = time.time()
        totalTime += inEndTime-inStartTime
        times.append(totalTime)
        avgTime += totalTime

    print(seqType + " average 'concatenation' time:",avgTime/NUM_TESTS)
    # with open("run"+str(datetime.strftime('%Y%d%j_%H%M%S')),'w') as f:
    with open(filename,'a') as f:
        for t in times:
            f.write(str(t) + ',')
        f.write(str(avgTime/NUM_TESTS) + '\n')

    times = [seqType + ': 3 copies']
    avgTime = 0
    for i in range(NUM_TESTS):
        totalTime = 0
        inStartTime = time.time()
        for i in range(1000000):
            seq * 3
        inEndTime = time.time()
        totalTime += inEndTime-inStartTime
        times.append(totalTime)
        avgTime += totalTime

    print(seqType + " average 'n copies' time:",avgTime/NUM_TESTS)
    # with open("run"+str(datetime.strftime('%Y%d%j_%H%M%S')),'w') as f:
    with open(filename,'a') as f:
        for t in times:
            f.write(str(t) + ',')
        f.write(str(avgTime/NUM_TESTS) + '\n')

    times = [seqType + ': item access']
    avgTime = 0
    for i in range(NUM_TESTS):
        totalTime = 0
        inStartTime = time.time()
        for i in range(1000000):
            seq[3]
        inEndTime = time.time()
        totalTime += inEndTime-inStartTime
        times.append(totalTime)
        avgTime += totalTime

    print(seqType + " average 'item access' time:",avgTime/NUM_TESTS)
    # with open("run"+str(datetime.strftime('%Y%d%j_%H%M%S')),'w') as f:
    with open(filename,'a') as f:
        for t in times:
            f.write(str(t) + ',')
        f.write(str(avgTime/NUM_TESTS) + '\n')

    times = [seqType + ': slice']
    avgTime = 0
    for i in range(NUM_TESTS):
        totalTime = 0
        inStartTime = time.time()
        for i in range(1000000):
            seq[3:5]
        inEndTime = time.time()
        totalTime += inEndTime-inStartTime
        times.append(totalTime)
        avgTime += totalTime

    print(seqType + " average 'slice' time:",avgTime/NUM_TESTS)
    # with open("run"+str(datetime.strftime('%Y%d%j_%H%M%S')),'w') as f:
    with open(filename,'a') as f:
        for t in times:
            f.write(str(t) + ',')
        f.write(str(avgTime/NUM_TESTS) + '\n')

    times = [seqType + ': length']
    avgTime = 0
    for i in range(NUM_TESTS):
        totalTime = 0
        inStartTime = time.time()
        for i in range(1000000):
            len(seq)
        inEndTime = time.time()
        totalTime += inEndTime-inStartTime
        times.append(totalTime)
        avgTime += totalTime

    print(seqType + " average 'length' time:",avgTime/NUM_TESTS)
    # with open("run"+str(datetime.strftime('%Y%d%j_%H%M%S')),'w') as f:
    with open(filename,'a') as f:
        for t in times:
            f.write(str(t) + ',')
        f.write(str(avgTime/NUM_TESTS) + '\n')

    times = [seqType + ': min']
    avgTime = 0
    for i in range(NUM_TESTS):
        totalTime = 0
        inStartTime = time.time()
        for i in range(1000000):
            min(seq)
        inEndTime = time.time()
        totalTime += inEndTime-inStartTime
        times.append(totalTime)
        avgTime += totalTime

    print(seqType + " average 'min' time:",avgTime/NUM_TESTS)
    # with open("run"+str(datetime.strftime('%Y%d%j_%H%M%S')),'w') as f:
    with open(filename,'a') as f:
        for t in times:
            f.write(str(t) + ',')
        f.write(str(avgTime/NUM_TESTS) + '\n')

    times = [seqType + ': max']
    avgTime = 0
    for i in range(NUM_TESTS):
        totalTime = 0
        inStartTime = time.time()
        for i in range(1000000):
            max(seq)
        inEndTime = time.time()
        totalTime += inEndTime-inStartTime
        times.append(totalTime)
        avgTime += totalTime

    print(seqType + " average 'max' time:",avgTime/NUM_TESTS)
    # with open("run"+str(datetime.strftime('%Y%d%j_%H%M%S')),'w') as f:
    with open(filename,'a') as f:
        for t in times:
            f.write(str(t) + ',')
        f.write(str(avgTime/NUM_TESTS) + '\n')
    print()

def formatData(fileList):
    dataList = []
    types = ["in", "not in", "concatenation", "3 copies", "access", "slice", "length", "min", "max"]

    for index,value in enumerate(fileList):
        
        tempDataList = []
        with open(value,'r') as f:
            for line in f.read().split('\n')[:-1]:
                line = line.split(',')
                tempDataList.append(line[NUM_TESTS+1])
        dataList.append(tempDataList)

    with open("results.csv", 'w') as f:
        f.write(",String,List,Tuple\n")

    for index, value in enumerate(dataList[0]):
        writeList = [types[index]]
        for jndex,val in enumerate(fileList):
            writeList.append(dataList[jndex][index])
        with open("results.csv", 'a') as f:
            for item in writeList:
                f.write(item+',')
            f.write('\n')

            
    
            

seq = "Hello World"

runTest(str(seq),"String", "j","test1.csv")

runTest(list(seq), "List", ["j"], "test2.csv")

runTest(tuple(seq), "Tuple", ("j",), "test3.csv")

formatData(["test1.csv", "test2.csv", "test3.csv"])


