import sys
sys.dont_write_bytecode = True

def hitP(f, R, t, r, g):
    if f>=g/2 :
        return 0.0
    missArea = 0.0
    gridL = g+2*r
    nGrids = (R - t) // gridL
    missGridSideLength = g - 2*f
    print("gridL %.12f; nGrids %d" %(gridL, nGrids) )
    indentSquareLength = nGrids*gridL
    remain = (R - t) - indentSquareLength
    missArea += (nGrids * missGridSideLength)**2
    remainMissArea = 0
    if remain - 2*r > 2*f
        if remain > g+r:    
        


    totalArea = R**2 / 4.0
    print( "missed a %.12f, total area %.12f" %(missR**2, (R-t)**2) )

    return (totalArea -  missArea) / (R-t)**2

def main():
    numTestCases = int(input())
    for i in range(numTestCases):
        f, R, t, r, g = list(map(float, input().split()))
        p = hitP(f, R, t, r, g)
        print( "Case #%d: %.6f" %(i+1, p))

if __name__ == '__main__':
    main()