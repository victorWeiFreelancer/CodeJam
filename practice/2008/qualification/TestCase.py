class TestCase(object):
    def __init__(self, number, nEngines, engines, nQuieries, queries, minSwitch=0):
        self.number = number
        self.nEngines = nEngines
        self.engines = engines
        self.nQuieries = nQuieries
        self.queries = queries
        self.minSwitch = minSwitch
    def findMinimalSwitch():
        print("todo")

    def __repr__(self):
        return "<Task %d:\n %d engines: %s\n %d queries:%s\n minimal switch:%d>" %(self.number, self.nEngines, self.engines, self.nQuieries, self.queries, self.minSwitch)
    def __str__(self):
        return "<Task %d:\n %d engines: %s\n %d queries:%s\n minimal switch:%d>" %(self.number, self.nEngines, self.engines, self.nQuieries, self.queries, self.minSwitch)
    
