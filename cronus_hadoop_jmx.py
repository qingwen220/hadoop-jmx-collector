#!/usr/bin/python

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from hadoop_jmx_kafka import *

def printCronus():
    cronusoutput = '[AGENT_MESSAGE]\n {\n"progress":100,\n"result": []\n}'
    print cronusoutput

main()
printCronus()