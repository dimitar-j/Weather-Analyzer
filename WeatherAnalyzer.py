import numpy as np

class WeatherAnalyzer:
    def __init__(self,tempData):
        self.temperatureDataList = np.array(tempData)

    def getMinTemp(self):
        tempList = []
        for i in range(len(self.temperatureDataList)):
            tempList.append(self.temperatureDataList[i].minTemperature)
        
        minTemps = np.array(tempList)
        return np.min(minTemps)
        
    def getMinTempAnnually(self):
        tempList = []
        yearlyMins = []
        currentYear = self.temperatureDataList[0].date.year

        for i in range(len(self.temperatureDataList)):
            if self.temperatureDataList[i].date.year == currentYear:
                yearlyMins.append(self.temperatureDataList[i].minTemperature)
                if i == len(self.temperatureDataList) - 1:
                    tempList.append(np.min(np.array(yearlyMins)))
            else:
                currentYear = self.temperatureDataList[i].date.year
                tempList.append(np.min(np.array(yearlyMins)))
                yearlyMins.clear()
                yearlyMins.append(self.temperatureDataList[i].minTemperature)
        return tempList

    def getMaxTemp(self):
        tempList = []
        for i in range(len(self.temperatureDataList)):
            tempList.append(self.temperatureDataList[i].maxTemperature)

        maxTemps = np.array(tempList)
        return np.max(maxTemps)

    def getMaxTempAnnually(self):
        tempList = []
        yearlyMaxs = []
        currentYear = self.temperatureDataList[0].date.year

        for i in range(len(self.temperatureDataList)):
            if self.temperatureDataList[i].date.year == currentYear:
                yearlyMaxs.append(self.temperatureDataList[i].maxTemperature)
                if i == len(self.temperatureDataList) - 1:
                    tempList.append(np.max(np.array(yearlyMaxs)))
            else:
                currentYear = self.temperatureDataList[i].date.year
                tempList.append(np.max(np.array(yearlyMaxs)))
                yearlyMaxs.clear()
                yearlyMaxs.append(self.temperatureDataList[i].maxTemperature)

        return tempList

    def getAvgSnowFallAnnually(self):
        tempList = []
        yearlySnowfalls = []
        currentYear = self.temperatureDataList[0].date.year

        for i in range(len(self.temperatureDataList)):
            if self.temperatureDataList[i].date.year == currentYear:
                yearlySnowfalls.append(self.temperatureDataList[i].snowFall)
                if i == len(self.temperatureDataList) - 1:
                    tempList.append(np.average(np.array(yearlySnowfalls)))
            else:
                currentYear = self.temperatureDataList[i].date.year
                tempList.append(np.average(np.array(yearlySnowfalls)))
                yearlySnowfalls.clear()
                yearlySnowfalls.append(self.temperatureDataList[i].snowFall)

        return tempList

    def getAvgTempAnnually(self):
        monthlyAverage = []
        yearlyAverage = []
        currentYear = self.temperatureDataList[0].date.year

        for i in range(len(self.temperatureDataList)):
            if self.temperatureDataList[i].date.year == currentYear:
                monthAverage = (self.temperatureDataList[i].minTemperature + self.temperatureDataList[i].maxTemperature)/2
                monthlyAverage.append(monthAverage)
                if i == len(self.temperatureDataList) - 1:
                    yearAverage = np.average(np.array(monthlyAverage))
                    yearlyAverage.append(yearAverage)
            else:
                currentYear = self.temperatureDataList[i].date.year
                yearAverage = np.average(np.array(monthlyAverage))
                yearlyAverage.append(yearAverage)
                monthlyAverage.clear()
                monthAverage = (self.temperatureDataList[i].minTemperature + self.temperatureDataList[i].maxTemperature)/2
                monthlyAverage.append(monthAverage)

        return yearlyAverage