#!/usr/bin/python
# coding:utf-8

import csv

row = list()
with open('test.csv', 'r', encoding='utf-8-sig')as file:
    result = csv.DictReader(file)
    data = {
        'title': list(),
        'rows': list()
    }
    for r in result:
        if None in list(r.keys()) or None in list(r.values()):
            print("error")
            continue
        if not data['title']:
            data['title'] = list(r.keys())
        data['rows'].append(dict(r))
        # if not row:
        #     row = list(r.values())
            # print(row)
    print(data)









# row =list()
# data= {
    # 'title':list(),
    # 'rows':list()
# }
# with open('test.csv','r',encoding='utf-8-sig') as q:
    # file = csv.DictReader(q)
    # for index,item in enumerate(file):
        # if index==0:
        #     title = list(item.keys())
        # if None in list(item.keys()) or None in list(item.values()):
        #     print("error")
        #     continue
        # data['title']=list(item.keys())

        # if not row:
            # row = list(item.values())
            # print(row)
        # data['rows'].append(dict(item))
    # print(data)
