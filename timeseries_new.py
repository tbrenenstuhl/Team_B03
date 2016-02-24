# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:38:23 2016

@author: Tyler
"""

#import modularized ts functions
import tsfunctions as tsf
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

#lamda function to define date format
dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y')
#requires input from stdin
#fileLocation = input ("Please list file location: ")
# tab delimited; specify the time column
data = pd.read_csv('C:\\Users\\Tyler\\Desktop\\GoDaddy_Data\\student_data_20160215\\student_data_20160215.csv', sep="\t",parse_dates='orderdate', index_col='orderdate',date_parser=dateparse)

#set parameters
#%matplotlib inline
plt.rcParams['figure.figsize'] = 15, 6

#metric variables from data file columns
ts_gcr = data['gcr'] 
ts_orders = data['orders'] 
ts_months = data['product_months']
ts_units = data['product_units']
ts_gcrmonth = data['gcr'] / data['product_months']
ts_gcrunits = data['gcr'] / data['product_units']
ts_monthsunit = data['product_months'] / data['product_units']
	
#run the ts code
tsf.ts_run()

#run module functions
tsf.ts_plot(ts_gcr)
tsf.ts_rollingStats(ts_gcr)
tsf.ts_df(ts_gcr)
