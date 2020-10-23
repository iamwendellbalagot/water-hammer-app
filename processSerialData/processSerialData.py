import serial
import numpy as np
import sqlite3
import pandas as pd
from tqdm import tqdm


def get_serial():
	n = 100
	path = 'database/whDB.db'
	arduino = serial.Serial('COM16', 9600)

	conn = sqlite3.connect(path)
	c = conn.cursor()
	readings = []

	for i in tqdm(range(n)):
		data = arduino.readline()[:-2].decode('utf-8')
		data = [float(i) for i in data.split('\t')]
		readings.append(data)
	arduino.close()
	df = pd.DataFrame(readings)
	df.columns = ['S1', 'S2']
	df.to_sql(name='Test', con = conn)
	return df

