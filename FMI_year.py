'''
Python script for plotting yearly time-series data
from the Finnish Meteorological Institute
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.dates as md
import datetime
import FMI_xml as fmi


###################################
# 2013
data13 = fmi.getXMLroot('ENO_2013.xml')
tmp = fmi.getXMLtimes(data13)
lat, lon, days = zip(*tmp)
daysfmt13 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
datefmt13 = [x.date() for x in daysfmt13]


data = fmi.getXMLdata(data13)
rrday13, tday13, snow13, tmin13, tmax13 = zip(*data)

###################################
# 2012
data12 = fmi.getXMLroot('ENO_2012.xml')
tmp = fmi.getXMLtimes(data12)

lat, lon, days = zip(*tmp)
daysfmt12 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
datefmt12 = [x.date() for x in daysfmt12]

data = fmi.getXMLdata(data12)
data = np.delete(data, (59), axis=0) # Delete leap day
rrday12, tday12, snow12, tmin12, tmax12 = zip(*data)

###################################
# 2011
data11 = fmi.getXMLroot('ENO_2011.xml')
tmp = fmi.getXMLtimes(data11)

lat, lon, days = zip(*tmp)
daysfmt11 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
datefmt11 = [x.date() for x in daysfmt11]


data = fmi.getXMLdata(data11)
rrday11, tday11, snow11, tmin11, tmax11 = zip(*data)

###################################
# 2010
data10 = fmi.getXMLroot('ENO_2010.xml')
tmp = fmi.getXMLtimes(data10)

lat, lon, days = zip(*tmp)
daysfmt10 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
datefmt10 = [x.date() for x in daysfmt10]


data = fmi.getXMLdata(data10)
rrday10, tday10, snow10, tmin10, tmax10 = zip(*data)

###################################
# 2009
data09 = fmi.getXMLroot('ENO_2009.xml')
tmp = fmi.getXMLtimes(data09)

lat, lon, days = zip(*tmp)
daysfmt09 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
datefmt09 = [x.date() for x in daysfmt09]


data = fmi.getXMLdata(data09)
rrday09, tday09, snow09, tmin09, tmax09 = zip(*data)

###################################
# 2008
data08 = fmi.getXMLroot('ENO_2008.xml')
tmp = fmi.getXMLtimes(data08)

lat, lon, days = zip(*tmp)
daysfmt08 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
datefmt08 = [x.date() for x in daysfmt08]


data = fmi.getXMLdata(data08)
data = np.delete(data, (59), axis=0) # Delete leap day
rrday08, tday08, snow08, tmin08, tmax08 = zip(*data)

###################################
# 2007
data07 = fmi.getXMLroot('ENO_2007.xml')
tmp = fmi.getXMLtimes(data07)

lat, lon, days = zip(*tmp)
daysfmt07 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
datefmt07 = [x.date() for x in daysfmt07]


data = fmi.getXMLdata(data07)
rrday07, tday07, snow07, tmin07, tmax07 = zip(*data)

###################################
# 2006
data06 = fmi.getXMLroot('ENO_2006.xml')
tmp = fmi.getXMLtimes(data06)

lat, lon, days = zip(*tmp)
daysfmt06 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
datefmt06 = [x.date() for x in daysfmt06]


data = fmi.getXMLdata(data06)
rrday06, tday06, snow06, tmin06, tmax06 = zip(*data)

###################################
# 2005
data05 = fmi.getXMLroot('ENO_2005.xml')
tmp = fmi.getXMLtimes(data05)

lat, lon, days = zip(*tmp)
daysfmt05 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
datefmt05 = [x.date() for x in daysfmt05]


data = fmi.getXMLdata(data05)
rrday05, tday05, snow05, tmin05, tmax05 = zip(*data)

###################################
# 2004
data04 = fmi.getXMLroot('ENO_2004.xml')
tmp = fmi.getXMLtimes(data04)

lat, lon, days = zip(*tmp)
daysfmt04 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
datefmt04 = [x.date() for x in daysfmt04]


data = fmi.getXMLdata(data04)
data = np.delete(data, (59), axis=0) # Delete leap day
rrday04, tday04, snow04, tmin04, tmax04 = zip(*data)

###################################
# 2003
data03 = fmi.getXMLroot('ENO_2003.xml')
tmp = fmi.getXMLtimes(data03)

lat, lon, days = zip(*tmp)
daysfmt03 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
datefmt03 = [x.date() for x in daysfmt03]


data = fmi.getXMLdata(data03)
rrday03, tday03, snow03, tmin03, tmax03 = zip(*data)

###################################
# 2002
data02 = fmi.getXMLroot('ENO_2002.xml')
tmp = fmi.getXMLtimes(data02)

lat, lon, days = zip(*tmp)
daysfmt02 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
datefmt02 = [x.date() for x in daysfmt02]


data = fmi.getXMLdata(data02)
rrday02, tday02, snow02, tmin02, tmax02 = zip(*data)

###################################
# 2001
data01 = fmi.getXMLroot('ENO_2001.xml')
tmp = fmi.getXMLtimes(data01)

lat, lon, days = zip(*tmp)
daysfmt01 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
datefmt01 = [x.date() for x in daysfmt01]


data = fmi.getXMLdata(data01)
rrday01, tday01, snow01, tmin01, tmax01 = zip(*data)

###################################
# 2000
# data00 = fmi.getXMLroot('ENO_2000.xml')
# tmp = fmi.getXMLtimes(data00)
#
# lat, lon, days = zip(*tmp)
# daysfmt00 = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
# datefmt00 = [x.date() for x in daysfmt00]
#
#
# data = fmi.getXMLdata(data00)
# data = np.delete(data, (59), axis=0) # Delete leap day
# rrday00, tday00, snow00, tmin00, tmax00 = zip(*data)

tdayall = zip(tday13, tday12, tday11, tday10, tday09, tday08, tday06, tday05,
              tday04, tday03, tday02, tday01) #2007 data incomplete, ignored

snowall = zip(snow13, snow12, snow11, snow10, snow09, snow08, snow06, snow05,
              snow04, snow03, snow02, snow01)

tminall = zip(tmin13, tmin12, tmin11, tmin10, tmin09, tmin08, tmin06, tmin05,
              tmin04, tmin03, tmin02, tmin01)

tmaxall = zip(tmax13, tmax12, tmax11, tmax10, tmax09, tmax08, tmax06, tmax05,
              tmax04, tmax03, tmax02, tmax01)

tdayall = np.asarray(tdayall)
tdaymean = np.nanmean(tdayall,axis=1)
tdaystd = np.nanstd(tdayall,axis=1,dtype = 'float64')

tminall = np.asarray(tminall)
tminmean = np.nanmean(tminall,axis=1)
tminstd = np.nanstd(tminall,axis=1,dtype = 'float64')

tmaxall = np.asarray(tmaxall)
tmaxmean = np.nanmean(tmaxall,axis=1)
tmaxstd = np.nanstd(tmaxall,axis=1,dtype = 'float64')

snowall = np.asarray(snowall)
snowall = snowall.clip(min=0)
snowmean = np.nanmean(snowall,axis=1)
snowstd = np.nanstd(snowall,axis=1,dtype = 'float64')
###############

yearmintemps = np.nanmin(tminall, axis=0)
yearminloc = np.nanargmin(tminall,axis=0)
yearmaxtemps = np.nanmax(tmaxall, axis=0)
yearmaxloc = np.nanargmax(tmaxall,axis=0)

min_std = np.std(yearmintemps)
min_mean = np.mean(yearmintemps)
max_std = np.std(yearmaxtemps)
max_mean = np.mean(yearmaxtemps)

minloc_std = np.std(yearminloc)
minloc_mean = np.mean(yearminloc)
maxloc_std = np.std(yearmaxloc)
maxloc_mean = np.mean(yearmaxloc)

############
#ts = fmi.smooth(data[:,1])
#plt.plot(tday13,':')
#plt.plot(tday12,':')
# plt.plot(tday11)
# plt.plot(tday10)
# plt.plot(tday09)
# plt.plot(tday08)
# plt.plot(tday07)
# plt.plot(tday06)
# plt.plot(tday05)
# plt.plot(tday04)
# plt.plot(tday03)
# plt.plot(tday02)
# plt.plot(tday01)
# plt.plot(tday00)
fig, ax1 = plt.subplots()


ax1.plot(fmi.smooth(tdaymean), 'k', lw=2) #Weekly means of daily average temps
# plt.plot(fmi.smooth(tdayall[:,0])) #Weekly means of daily average temps 2013
# plt.plot(fmi.smooth(tdayall[:,12])) #Weekly means of daily average temps 2001
ax1.fill_between(xrange(0,len(fmi.smooth(tdaymean))),  # mean min and max
                 fmi.smooth(tminmean),
                 fmi.smooth(tmaxmean),
                 facecolor='blue', alpha=0.5)
ax1.fill_between(xrange(0,len(fmi.smooth(tdaymean))),  # 95% from mean
                 fmi.smooth(tminmean-1.959964*tminstd),
                 fmi.smooth(tmaxmean+1.959964*tmaxstd),
                 facecolor='blue', alpha=0.25)
ax1.fill_between(xrange(0,len(fmi.smooth(tdaymean))),  # 99% from mean
                 fmi.smooth(tminmean-2.575829*tminstd),
                 fmi.smooth(tmaxmean+2.575829*tmaxstd),
                 facecolor='blue', alpha=0.25)
ax1.plot(yearminloc, yearmintemps, 'bo') # Plot min values for each year
ax1.plot(yearmaxloc, yearmaxtemps, 'ro') # Plot max values for each year
ax1.plot(tdaymean, 'k')

# cov = np.cov(yearmaxloc, yearmaxtemps)
# lambda_, v = np.linalg.eig(cov)
# lambda_ = np.sqrt(lambda_)
# from matplotlib.patches import Ellipse
# j=2
# ell = Ellipse(xy=(np.mean(x), np.mean(y)), width=lambda_[0]*j*2, height=lambda_[1]*j*2, angle=np.rad2deg(np.arccos(v[0, 0])))
# ax1.add_artist(ell)


ax2 = ax1.twinx()
ax2.fill_between(xrange(0,len(snowmean)), 0, snowmean, facecolor='grey', alpha=0.5)
ax2.fill_between(xrange(0,len(snowmean)), 0, snowmean+2.575829*snowstd, facecolor='grey', alpha=0.25)
ax2.plot(snowmean-2.575829*snowstd,'k--')

# Plot set-up
ax1.axis([0, 360, -70, 35])
ax1.set_yticks((xrange(-50,40,10)))
ax2.axis([0, 360, 0, 500])
ax2.set_yticks((xrange(0,120,20)))

ax1.set_ylabel('Temperature ($^{\circ}$C)')
ax1.yaxis.set_label_coords(-0.05, 0.55)
ax2.set_ylabel('Snow Cover (cm)')
ax2.yaxis.set_label_coords(1.05, 0.1)
fig.savefig('test.eps', papertype = 'a4', orientation = 'portrait', format='eps', dpi=1000)
# ax1.grid(True)
# ax2.grid(True)
plt.show()