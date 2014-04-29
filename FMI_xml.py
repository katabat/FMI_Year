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

