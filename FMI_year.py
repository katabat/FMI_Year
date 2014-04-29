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

# 2013
data13 = fmi.getXMLroot('ENO_2013.xml')
tmp = fmi.getXMLtimes(data13)
lat, lon, days = zip(*tmp)
daysfmt = np.array([datetime.datetime.fromtimestamp(days[i]) for i in xrange(len(days))])

data = fmi.getXMLdata(data13)
rrday13, tday13, snow13, tmin13, tmax13 = zip(*data)
