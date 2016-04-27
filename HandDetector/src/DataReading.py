#coding= UTF-8
'''
Created on 2014年10月29日

@author: Yang
'''
# -*- coding: utf-8 -*- 

import csv
import io 


with open('D:\label1.csv ','rb') as f:
       reader = csv.reader(f)
       arr = []
       for row in reader :
            #if row[1]!= "None":
                arr.append(row)
                
       print arr
                #[index] = row[2]
                #y = row[3]
                #w = row[4]
                #h = row[5]
                #angle = row[6]
                #print x,y,w,h,angle