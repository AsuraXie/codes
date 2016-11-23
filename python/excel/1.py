#!/usr/bin/env python
# -*- coding:utf8 -*-

import xlwt
import xlrd
import os
import re

def open_excel(filename):
    workbook=xlrd.open_workbook(filename)
    return workbook

def save_excel(filename,result):
    workbook=xlwt.Workbook(encoding='utf-8')
    for key in result:
        ws=workbook.add_sheet(key)
        i=0
        for item in result[key]:
            j=0
            ws.write(i,j,item)
            print item
            for v in result[key][item]:
                j=j+1
                print "key:",key,"item:",item,"v:",v,"res:",v
                ws.write(i,j,v)
            i=i+1
    workbook.save(filename)
    return
        

def process(workbook):
    result={}
    worksheets=workbook.sheet_names()
    for sheet_names in worksheets:
        if 'eet' in sheet_names:
            continue

        if re.match("[a-zA-Z]",sheet_names):
            continue

        print "processing sheet:"+sheet_names
        ws=workbook.sheet_by_name(sheet_names)
        num_rows=ws.nrows
        row_65=0
        row_67=0
        for curr_row in range(num_rows):
            row_value=ws.row_values(curr_row)
            if "Total Consumption" in row_value[0]:
                row_65=row_value
            if "Non-Energy Use" in row_value[0]:
                row_67=row_value
                break
        row_74=[0.7143,0.9,0.2857,0.7143,0.9714,5.714,1.786,0.9702,1.4286,1.4714,1.4714,1.4571,1.4286,1.7143,1.5714,1.4268,13.3,1,1,1]
        count=len(row_74)
        res=[]
        for i in range(count):
            if row_65[i+1]=="":
                row_65[i+1]=0
            if row_67[i+1]=="":
                row_67[i+1]=0

            res.append((float(row_65[i+1])-float(row_67[i+1]))*row_74[i])
        result[sheet_names]=res

    return result


def get_sheet(filename):
    sheet_name=re.findall("\d+",filename)
    if len(sheet_name)>0:
        return sheet_name[0]
    else:
        return '00001'

if __name__=="__main__":
    files=os.popen('ls | grep xls')
    result={}
    for file_name in files:
        if 'result' in file_name:
            continue

        file_name=file_name.strip('\n')
        print "processing:"+file_name
        wb=open_excel(file_name)
        data=process(wb)
        res_sheet=get_sheet(file_name)
        result[res_sheet]=data
        print res_sheet

    save_excel("result.xlsx",result)

