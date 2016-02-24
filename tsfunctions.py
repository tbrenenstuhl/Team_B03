# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:25:56 2016

@author: MSBA Team B-03
"""
# ACF & PACF Plots:
# from statsmodels.tsa.stattools import acf, pacf

print ()

def ts_run():
	import pandas as pd
	import timeseries_new as tsn	
	#metric variables from data file columns
	ts_gcr = tsn.data['gcr'] 
	ts_orders = tsn.data['orders'] 
	ts_months = tsn.data['product_months']
	ts_units = tsn.data['product_units']
	ts_gcrmonth = tsn.data['gcr'] / tsn.data['product_months']
	ts_gcrunits = tsn.data['gcr'] / tsn.data['product_units']
	ts_monthsunit = tsn.data['product_months'] / tsn.data['product_units']
	#subregion lists from respective regions
	apac = ['India', 'China', 'Australia', 'APAC-Tier2', 'APAC-Tier3']
	emea = ['Turkey', 'United Kingdom', 'EMEA-Tier2', 'EMEA-Tier3']
	latam = ['Mexico', 'Brazil', 'LATAM-Tier2', 'LATAM-Tier3']
	others = ['Others-Tier3']
	usa = ['United States']
	canada = ['Canada']	
	#list of metric variables
	metrics = [tsn.ts_gcr, tsn.ts_orders, tsn.ts_months, tsn.ts_units, tsn.ts_gcrmonth, tsn.ts_gcrunits, tsn.ts_monthsunit]
	#list of regions
	subregions = [apac, emea, latam, canada, usa, others]
	#list of product id's
	prod_id = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
	
	for m, r in zip(metrics, subregions):
		data_subset=tsn.data[(tsn.data.report_region_2==subregions) & (tsn.data.product_category_id==prod_id)]
		data_subset.sortlevel(['orderdate'],inplace=True)
		
#Plot metric
def ts_plot(metric):
	import matplotlib.pylab as plt
	plt.plot(metric)

#Plot rolling statistics:
def ts_rollingStats(metric, window=30):
	import pandas as pd
	import matplotlib.pylab as plt
	rolmean = pd.rolling_mean(metric, window=30)
	rolstd = pd.rolling_std(metric, window=30)
	orig = plt.plot(metric, color='blue',label='Original')
	mean = plt.plot(rolmean, color='red', label='Rolling Mean')
	std = plt.plot(rolstd, color='black', label = 'Rolling Std')
	plt.legend(loc='best')
	plt.title('Rolling Mean & Standard Deviation')
	plt.show(block=False)
    
#Perform Dickey-Fuller test:
def ts_df(metric):
	import pandas as pd
	from statsmodels.tsa.stattools import adfuller
	print ('Results of Dickey-Fuller Test:')
	dftest = adfuller(metric, autolag='AIC')
	dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
	for key,value in dftest[4].items():
	    dfoutput['Critical Value (%s)'%key] = value
	print (dfoutput)


#def ts_acf(x):
#	lag_acf = acf(ts_log_diff, nlags = 20)
#	plt.sublpot 
