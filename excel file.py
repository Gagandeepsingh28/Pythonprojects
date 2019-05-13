# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 23:28:26 2019

@author: Manmeet Kaur
"""
import xlwt
import xlrd
import xlutils.copy
import os
print(os.getcwd())
# Creating dynamic file name
file=os.getcwd()+"\\writing124.xls"
# Creating object for Workbook
wb=xlwt.Workbook()
# Adding sheet name
ws=wb.add_sheet("Test Sheet")
# Writing into sheet using rows and column index
ws.write(1,0,"Test Value")
# saving excel file
wb.save(file)
# opening excel file in read mode
rb=xlrd.open_workbook(file)
# get the number of active shees in workbook
print(rb.nsheets)
# get the sheet name and return list of active sheet name that has some content 
print(rb.sheet_names())
# Fetching the values rows from excel
first_raw=rb.sheet_by_index(0)
# Reading second as there is no value we added in first raw
print(first_raw.row_values(1))
# Creating object for xlutils module in order to append the existing sheet without overlapping values
wb=xlutils.copy.copy(rb)
w_sheet=wb.get_sheet(0)
w_sheet.write(1,1,"Modified")
w_sheet.write(3,1,"Modified")
w_sheet.write(2,1,"Modified")
w_sheet.write(2,0,"Test values")
wb.save(file)



