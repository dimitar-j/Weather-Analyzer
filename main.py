
import numpy as np
import FileIO
import Date
import TemperatureData
import Chart
import WeatherAnalyzer

def menu():
    print ("1- Get Minimum Temperature of 1990-2019")
    print ("2- Get Maximum Temperature of 1990-2019")
    print ("3- Get Minimum Temperature of 1990-2019 Annually")
    print ("4- Get Maximum Temperature of 1990-2019 Annually")
    print ("5- Get Average Snowfall between 1990-2019 Annually")
    print ("6- Get Average Temperature between 1990-2019 Annually")
    print ("7- LineChart Minimum Temperature of 1990-2019 Annually")
    print ("8- LineChart Maximum Temperature of 1990-2019 Annually")
    print ("9- BarChart Average Snowfall between 1990-2019")
    print ("10- Barchart Average Temperature between 1990-2019 Annually")

def getUserInput():
    i = 11
    while i > 10:
        i = int(input())
    print()
    return i

def callFunction(i,weatherAnalyzer,years,chart):
    if i == 1:
        print("Minimum Temperature of 1990 - 2019: ",weatherAnalyzer.getMinTemp())
    elif i == 2:
        print("Maximum Temperature of 1990 - 2019: ",weatherAnalyzer.getMaxTemp())
    elif i == 3:
        print("Annual Minimum Temperatures of 1990 - 2019: ",weatherAnalyzer.getMinTempAnnually())
    elif i == 4:
        print("Annual Maximum Temperatures of 1990 - 2019: ",weatherAnalyzer.getMaxTempAnnually())
    elif i == 5:
        print("Average Annual Snowfall between 1990 - 2019: ",weatherAnalyzer.getAvgSnowFallAnnually())
    elif i == 6:
        print("Average Temperature Annually between 1990 - 2019: ",weatherAnalyzer.getAvgTempAnnually())
    elif i == 7:
        print("Creating LineChart of minimum temperature of 1990-2019 annually")
        value = weatherAnalyzer.getMinTempAnnually()
        chart.drawLineChart(years,value,"Minimum temperature of 1990-2019 annually","Years","Temperature")
    elif i == 8:
        print("Creating LineChart of maximum temperature of 1990-2019 annually")
        value = weatherAnalyzer.getMaxTempAnnually()
        chart.drawLineChart(years,value,"Maximum temperature of 1990-2019 annually","Years","Temperature")
    elif i == 9:
        print("Creating BarChart of average snowfall between 1990-2019 Annually")
        value = weatherAnalyzer.getAvgSnowFallAnnually()
        chart.drawBarChart(years,value,"Average snowfall between 1990-2019 Annually","Years","Snowfall")
    elif i == 10:
        print("Creating BarChart of average temperature between 1990-2019 Annually")
        value = weatherAnalyzer.getAvgTempAnnually()
        chart.drawBarChart(years,value,"Average temperature between 1990-2019 Annually","Years","Temperature")
    else:
        print("Please enter correct input")
    print()

def main():

    #create FileIo object and store data from csv file
    fio = FileIO.FileIO("CalgaryWeather.csv")
    data = fio.dataTable

    #create list of TemperatureData objects from each row in csv file
    temperatureDataList = []
    for i in range(len(data)):
        tempTemperatureDataObj = TemperatureData.TemperatureData(data[i][1],data[i][0],data[i][3],data[i][2],data[i][4])
        temperatureDataList.append(tempTemperatureDataObj)
    
    #create list containing years
    listOfYears = list(range(1990,2020))

    #create WeatherAnalyzer object weatherAnalyzer and pass in list of temperatureData
    weatherAnalyzer = WeatherAnalyzer.WeatherAnalyzer(temperatureDataList)

    #create Chart object
    chartObj = Chart.Chart()

    #print menu of choices for user
    menu()

    #keep collecting user input until acceptable input is received and then store it in variable choice
    choice = getUserInput()

    #call the correct function based on user's input by passing in user's input
    callFunction(choice,weatherAnalyzer,listOfYears,chartObj)

if __name__ == "__main__":
    main()