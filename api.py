import pymysql as DBAdapter
import numpy as np
import pandas as pd
import sys, os, math
from threading import Thread
import joblib
import datetime
import hashlib
import base64

__PATH__ = os.path.realpath("")

__PRICE_PER_COIN_IN_DOLLARS__ = 0.5

def buildUp(args):
	end = ""
	for i in range(len(args)):
		if (args[i] == args[-1]):
			end += str(args[i])
		else:
			end += str(args[i]) + ","
	return end

def superBuildUp(args):
	end = ""
	for i in range(len(args)):
		if (args[i] == args[-1]):
			end += buildUp(args[i])
		else:
			end += buildUp(args[i]) + ";"
	return end

# def con(host='remotemysql.com', db='qMrNNwY7xi'):
# 	return DBAdapter.connect(host, "qMrNNwY7xi", "e64zdS2mbk", db)

def con(host='localhost', db='cyfar-gaming-coin'):
	return DBAdapter.connect(host, "root", "", db)
