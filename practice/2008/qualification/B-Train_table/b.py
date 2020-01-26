import sys
sys.dont_write_bytecode = True

def timeStrConvertN(a):
    h, m = list(map(int, a.split(':')))
    return h*60+m

def depart(deltaT, x):
    # let the first train from x to depart
    t = x[0][0][1]
    iter = 1
    x[0].pop(0)
    while( len(x[iter])>0 and (t + deltaT <= x[iter][-1][0]) ):
        for i in range( len(x[iter]) ):
            if t+deltaT <= x[iter][i][0]:
                # if find the first schedule that departs after arrival + turnaround
                t = x[iter][i][1]
                x[iter].pop(i)
                iter = (iter + 1)%2
                break

def schedule(deltaT, a, b):
    aCounter, bCounter, aPoint, bPoint = [0]*4
    while(len(a) and len(b)):
        if (a[0][0] < b[0][0]) or (a[0][0]==b[0][0] and a[0][1] <= b[0][1]):
            aCounter+=1
            depart(deltaT, [a, b])
        elif (a[0][0] > b[0][0]) or ( a[0][0]==b[0][0] and a[0][1] > b[0][1] ):
            bCounter+=1
            depart(deltaT, [b, a])
    if len(a):
        aCounter += len(a)
    elif len(b):
        bCounter += len(b)
    return [aCounter, bCounter]

def main():
    numTestCases = int(input())
    for i in range(numTestCases):
        turnAround = int(input())
        na, nb = list(map(int, input().split()))
        aTrips = []
        bTrips = []
        for _ in range(na):
            startT, endT = input().split()
            aTrips.append([timeStrConvertN(startT), timeStrConvertN(endT)])
            aTrips = sorted(aTrips, key=lambda aTrips: aTrips[0])
        for _ in range(nb):
            startT, endT = input().split()
            bTrips.append([timeStrConvertN(startT), timeStrConvertN(endT)])
            bTrips = sorted(bTrips, key=lambda bTrips: bTrips[0])
        aTrains, bTrains = schedule(turnAround, aTrips, bTrips)
        print( "Case #%d: %d %d" %(i+1, aTrains, bTrains))

if __name__ == '__main__':
    main()