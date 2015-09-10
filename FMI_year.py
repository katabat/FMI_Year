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
import glob
import pandas as pd

xmlfiles = glob.glob('*.xml')

ENO = {}

for f in xmlfiles:
    d = fmi.getXMLroot(f)
    tmp = fmi.getXMLtimes(d)
    lat, lon, days = zip(*tmp)
    data = fmi.getXMLdata(d)
    rrday, tday, snow, tmin, tmax = zip(*data)
    
    daysfmt = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])
    ENO[f[4:8]] = pd.DataFrame({'rrday': rrday, 'tday':tday, 'snow':snow, 'tmin':tmin, 'tmax':tmax}, index= daysfmt)


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
#fig.savefig('test.eps', papertype = 'a4', orientation = 'portrait', format='eps', dpi=1000)
# ax1.grid(True)
# ax2.grid(True)
plt.show()