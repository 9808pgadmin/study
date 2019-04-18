import json
import urllib
import time
import datetime
import re
import logging
import csv

csvfile = open('t_csv.csv','r',encoding='utf-8')
reader = csv.reader(csvfile)
data = list(reader)

# for index, line in enumerate(data):
#     if index > 0:
#         title = line[0]
#         id = line[1]
#         print(title)
#         print(id)
print(data[1:])
for line in data[1:]:
    xmlFilePath = line[0]
    eventId = line[1]
    print(xmlFilePath)
    print(eventId)



# jsonData = {
#     "data":{}
# }
# print(title)
# for value in data[1:]:
#     columns = dict()
#     for key,item in enumerate(title):
#         columns[item] = value[key]
#     result.append(columns)
# print(result)
    # print(value)