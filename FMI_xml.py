'''
Python script for parsing XML times-series data
from the Finnish Meteorological Institute
'''
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.dates as md
import datetime

def split_seq(seq, numpieces):
    '''
    '''
    seqlen = len(seq)
    d, m = divmod(seqlen, numpieces)
    rlist = range(0, ((d + 1) * (m + 1)), (d + 1))
    if d != 0: rlist += range(rlist[-1] + d, seqlen, d) + [seqlen]

    newseq = []
    for i in range(len(rlist) - 1):
        newseq.append(seq[rlist[i]:rlist[i + 1]])

    newseq += [[]] * max(0, (numpieces - seqlen))
    return newseq

def getXMLroot(xml):
    '''
    '''
    xmldata = ET.parse(xml)
    root = xmldata.getroot()
    return root

def getXMLstart(root):
    '''
    '''
    start = root[0][0][0][0][0].text
    starttime = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ")
    return starttime

def getXMLend(root):
    '''
    '''
    end = root[0][0][0][0][1].text
    endtime = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ")
    return endtime

def getXMLtimes(root):
    '''
    '''
    cols = 3
    times = root[0][0][6][0][0][0][0].text
    times = [float(x) for x in times.split()]
    al=len(times)/cols
    data = np.asarray(split_seq(times,al))
    return data

def getXMLdata(root):
    '''
    '''
    cols = 5
    times = root[0][0][6][0][1][0][1].text
    times = [float(x) for x in times.split()]
    al=len(times)/cols
    data = np.asarray(split_seq(times,al))
    return data

def smooth(x,window_len=7,window='flat'):
    """smooth the data using a window with requested size.

    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.

    input:
        x: the input signal
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.

    output:
        the smoothed signal

    example:

    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)

    see also:

    np.hanning, np.hamming, np.bartlett, np.blackman, np.convolve
    scipy.signal.lfilter

    TODO: the window parameter could be the window itself if an array instead of a string
    NOTE: length(output) != length(input), to correct this: return y[(window_len/2-1):-(window_len/2)] instead of just y.
    """

    if x.ndim != 1:
        raise ValueError, "smooth only accepts 1 dimension arrays."

    if x.size < window_len:
        raise ValueError, "Input vector needs to be bigger than window size."


    if window_len<3:
        return x


    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError, "Window is one of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"


    s=np.r_[x[window_len-1:0:-1],x,x[-1:-window_len:-1]]
    #print(len(s))
    if window == 'flat': #moving average
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')

    y=np.convolve(w/w.sum(),s,mode='valid')
    #return y[(window_len/2):-(window_len/2)]
    return y