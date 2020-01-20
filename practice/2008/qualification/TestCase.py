class TestCase(object):
    def __init__(self, number, nEngines, engines, nQueries, queries, minSwitch=0):
        self.number = number
        self.nEngines = nEngines
        self.engines = engines
        self.nQueries = nQueries
        self.queries = queries
        self.minSwitch = minSwitch
    def findMinimalSwitch(self):
        switchCount = 0
        prevEngine = -1
        vacancyList = [0]* (self.nEngines)
        # print("Task %d engine vacant count %s" % (self.number, vacancyList))
        if self.nQueries:
            start = 0
            end = self.nQueries
            vacancyList = [0]*self.nEngines
            while start<end:
                vacancyList[self.queries[start]]+=1
                if not any(v==0 for v in vacancyList) :
                    # print("engine vacant count %s" % vacancyList)
                    prevEngine=start
                    switchCount+=1
                    vacancyList = [0]*self.nEngines
                    vacancyList[self.queries[start]]+=1
                start+=1
        self.minSwitch = switchCount
        print("Case #%d: %d" %(self.number, self.minSwitch))
        return switchCount



    def __repr__(self):
        return "<Task %d:\n %d engines: %s\n %d queries:%s\n minimal switch:%d>" %(self.number, self.nEngines, self.engines, self.nQueries, self.queries, self.minSwitch)
    def __str__(self):
        return "<Task %d:\n %d engines: %s\n %d queries:%s\n minimal switch:%d>" %(self.number, self.nEngines, self.engines, self.nQueries, self.queries, self.minSwitch)
    
