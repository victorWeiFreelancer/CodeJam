import sys
sys.dont_write_bytecode = True

from TestCase import TestCase

def main():
    numTestCases = int(input())
    testCaseList = []
    for i in range(numTestCases):
        nEngine = int(input())
        engineDict = {}
        queryList = []
        for j in range(nEngine):
            engineDict[ input().rstrip('\n') ] = j
        nQuery = int(input())
        for _ in range(nQuery):
            queryList.append( engineDict[input().rstrip('\n')] )
        testCaseList.append( TestCase(i+1, nEngine, engineDict, nQuery, queryList) )
    print([x for x in testCaseList])

if __name__ == '__main__':
    main()