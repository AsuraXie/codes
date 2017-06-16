#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys
import random

def convert(file_name):
    my_file = open(file_name,"r")
    out_file = open("output"+str(random.randint(10000,99999))+".txt","a+")
    out_file.write("FN Thomson Reuters Web of Science™\n")
    out_file.write("VR 1.0\n")
    signal = 0
    single_article = []
    for line in my_file.readlines():
        if len(line) <= 1:
            continue
        item = line[0]+line[1]
        if item == "PT":
            signal = 1
            cond1 = 0
            cond2 = 0
            cond3 = 0
            single_article = []

        if signal == 1:
            single_article.append(line)
            if item == "TI" or item == "DE" or item == "AB":
                if line.find("land use") or line.find("land-use") or line.find("land use allocat*") or line.find("land-use allocat*") > 0:
                    cond1 = 1
                if line.find("climate change") or line.find("climate change") or line.find("climate changes") or line.find("climatic change") or line.find("climatic changes") or line.find("climate variability") or line.find("low carbon") or line.find("carbon emissions") or line.find("carbon dioxide") or line.find("carbon emission") or line.find("carbon cycle") or line.find("CO2") or line.find("GHG") or line.find("greenhouse gas") or line.find("climate resilience") or line.find("climate vulnerability") or line.find("climate impact") or line.find("climate mitigation") or line.find("climate adaptation") > 0:
                    cond2 = 1
                if line.find("model") > 0:
                    cond3 = 1
        if item == "ER":
            if cond1 and cond2 and cond3:
                single_article.append("\n")
                for item in single_article:
                    out_file.write(item)
            signal = 0
            cond1 = 0
            cond2 = 0
            cond3 = 0

    out_file.write("EF")
    out_file.close()
    my_file.close()

if __name__=="__main__":
    if len(sys.argv)<=1:
        print "输入文件名"
        exit()

    file_name = sys.argv[1]
    if file_name == "":
        print "输入文件名"
        exit()
    convert(file_name)
