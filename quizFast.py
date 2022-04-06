#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json



# Complete the function below.
# Base query: https://jsonmock.hackerrank.com/api/stocks
#https://jsonmock.hackerrank.com/api/stocks/search?key=value&page=pageNumber

#given inputs of a date range of the format 1-January-2000, print the open and close
#stock prices for stocks of the given date range

def  openAndClosePrices(firstDate, lastDate):
    #print(firstDate)
    #print(lastDate)
    startDay = int(firstDate.split('-')[0])
    endDay = int(lastDate.split('-')[0])
    startYear = int(firstDate.split('-')[2])
    endYear = int(lastDate.split('-')[2])
    months = ['January', 'February', 'March', 'April', 'May', 'June','July','August','September', 'October', 'November', 'December']
    startMonth = firstDate.split('-')[1]
    endMonth = lastDate.split('-')[1]
    monthIndexStart = months.index(startMonth) #integer 0-11
    monthIndexEnd = months.index(endMonth) #integer 0-11
    #print(startMonth)
    #################################################
    queryList =[]

    datesList = [firstDate,lastDate] #expand these dates and search individually
    stockJSONStr = []
    requestedKeys = ['date','open','close']
    uriString = ""
    query = ""
    url = 'https://jsonmock.hackerrank.com/api/stocks/'
    uriString = query
    uri = url + uriString
    req = urlopen(uri).read()


    tp = json.loads(req)['total_pages'] #if total pages is more than 1, go through each, else just search results
    if tp > 1:
        if uri == url: #if it's the base URL with no further queries
                uri += "?page="# + str(i)          #https://jsonmock.hackerrank.com/api/stocks/
        else:
                uri += "&page="# + str(i)
        #print("querying " + str(tp) + " pages")
        for i in range(1,tp + 1):
            #print(uri + str(i))
            req = urlopen(uri + str(i)).read()
            stockJSONStr.append(req)
            #print(req)
            #os.system('pause')
    else:
        stockJSONStr.append(req)

    dateJSONObjects = []

    for jsonStr in stockJSONStr: #all stock objects
        jsonObj = json.loads(jsonStr)

        #print(type(jsonObj['data']))
        for dataObj in jsonObj['data']: #dict object of each stock

            dataString = ""
            dateStr = dataObj['date']
            stockDay = int(dateStr.split('-')[0])
            stockMonth = dateStr.split('-')[1]
            #endDay = int(lastDate.split('-')[0])
            stockYear = int(dateStr.split('-')[2])
            startMonthEndDay = 32
            endMonthStartDay = 0
            firstMonthStart = 0  #
            lastMonthEnd = 12
            #endYear = int(lastDate.split('-')[2])
            if stockYear not in range(startYear,endYear + 1): #ignore stocks in wrong year
                continue

            if stockYear in range(startYear +1,endYear): #take all stocks in middle years
                #print(dateStr)
                dateJSONObjects.append(dataObj)
                continue

            if startYear == endYear:
                firstMonthStart = monthIndexStart #index(startMonth) #0-11
                lastMonthEnd = monthIndexEnd #index(endMonth) #0-11

            if startYear == stockYear: #here all the start year months beteween first and last should be added
                #print(stockMonth +','+str(months.index(stockMonth)))
                #print(str(monthIndexStart) +','+str(lastMonthEnd))
                if months.index(stockMonth) in range(monthIndexStart + 1,lastMonthEnd):
                    #print("adding " + stockMonth)
                    dateJSONObjects.append(dataObj)
                    continue
            if endYear == stockYear and endYear != startYear: #here all the ending year months between first and last should be, if the years aren't the same
                if months.index(stockMonth) in range(firstMonthStart,monthIndexEnd):
                    #print("adding " + stockMonth)
                    dateJSONObjects.append(dataObj)
                    continue

            if startMonth == endMonth and startYear == endYear:
                startMonthEndDay = endDay
                endMonthStartDay = startDay

            if stockMonth == startMonth:
                if stockDay in range(startDay,startMonthEndDay+1):
                             #print("adding "  + str(stockDay) + stockMonth + str(stockYear))
                             dateJSONObjects.append(dataObj)
                             continue
            if stockMonth == endMonth:
                if stockDay in range(endMonthStartDay,endDay+1):
                             #print("adding "  + str(stockDay) + stockMonth + str(stockYear))
                             dateJSONObjects.append(dataObj)
                             continue

    #format requested keys and print them
    for dateJSONObject in dateJSONObjects:
            dataString = ""
            for stockDataKey in requestedKeys:
                if dataString == "":
                    dataString = str(dateJSONObject[stockDataKey])
                else:
                    dataString += " " + str(dateJSONObject[stockDataKey])
            print(dataString)



_firstDate = '1-January-2000'
_lastDate = '28-December-2013'
openAndClosePrices(_firstDate, _lastDate)
