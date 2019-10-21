# 計算三天的天氣狀況
import pandas as pd

weatherList = ['Sunny', 'Cloudy', 'Rainy']
humidityList = ['VeryDry', 'Dry', 'Wet', 'VeryWet']

#初始條件
weatherProbabilities = {'Sunny'  : 0.63, 'Cloudy' : 0.17, 'Rainy'  : 0.20}
print('天氣初始條件:\n',weatherProbabilities)

humidities = {1 : 'VeryDry', 2 : 'Dry', 3 : 'Wet'}
print('濕度:\n',humidities)

#矩陣
weatherMatrix = [[0.500, 0.375, 0.125],[0.250, 0.125, 0.625],[0.250, 0.375, 0.375]]
print('天氣矩陣:\n',pd.DataFrame(data = weatherMatrix, index = weatherList, columns = weatherList))
print()

humidityMatrix = [[0.60, 0.20, 0.15, 0.05],[0.25, 0.25, 0.25, 0.25],[0.05, 0.10, 0.35, 0.50]]
print('濕度矩陣:\n',pd.DataFrame(data = humidityMatrix, index = weatherList, columns = humidityList))
print()

def A(day, weather, needPrint = True):
    weatherValue = 0.0
    if (day == 1):
        weatherValue = weatherProbabilities[weather]
        
        if needPrint: print('(%s' % weatherValue, end = '')
    else:
        if needPrint: print('(', end = '')
        
        for index in range(0, len(weatherList)):
            if needPrint and index != 0: print('+', end = '')
            if needPrint: print('a%s(%s)' % (day - 1, weatherList[index]), end = '')
            
            value = A(day - 1, weatherList[index], needPrint = False)
            weatherValue += value * weatherMatrix[index][weatherList.index(weather)]
        
        if needPrint: print(')', end = '')
    
    humidity = humidities[day]
    humidityValue = humidityMatrix[weatherList.index(weather)][humidityList.index(humidity)]
    
    if needPrint: 
        print('*%s)' % humidityValue, end = '')
    
    return weatherValue * humidityValue

def printA(day, weather):
    print('a%s(%s)=' % (day, weather), end = '')
    answer = A(day, weather)
    print('= %s' % answer)

#預測 a1三天的天氣狀況
printA(1, 'Sunny')
printA(1, 'Cloudy')
printA(1, 'Rainy')
print()

#預測 a2三天的天氣狀況
printA(2, 'Sunny')
printA(2, 'Cloudy')
printA(2, 'Rainy')
print()

#預測 a3三天的天氣狀況
printA(3, 'Sunny')
printA(3, 'Cloudy')
printA(3, 'Rainy')
print()