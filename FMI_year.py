'''
Script for comparing daily summary of times-series data
from Finnish Meteorological Institute
'''
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.dates as md
import datetime