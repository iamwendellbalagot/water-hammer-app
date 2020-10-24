import serial
import numpy as np
import sqlite3
import pandas as pd
from tqdm import tqdm

process = True

def get_dataframe(table='test', path='database/whDB.db'):
        conn = sqlite3.connect(path)
        df = pd.read_sql('SELECT * FROM {}'.format(table), con=conn)
        conn.close()
        return df


def get_serial(req = True):
	n = 100
	path = 'database/whDB.db'
	arduino = serial.Serial('COM16', 9600)

	conn = sqlite3.connect(path)
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

def upload_generate(port='', baud=9600, n=200,
                    table = 'test',
                    path='database/whDB.db'):
        arduino = serial.Serial(port, baud)
        try:
            conn = sqlite3.connect(path)
            c = conn.cursor()
            readings = []
            
            while process:
                data = arduino.readline()[:-2].decode('utf-8')
                data = [float(i) for i in data.split('\t')]
                readings.append(data)
                
                c.execute('INSERT INTO '+ table +' VALUES(?,?);',tuple(data));
                conn.commit()
                if process == False:
                	break
            df = pd.DataFrame(readings, columns=['S1', 'S2'])
            return df
            conn.close()
        except:
            conn.close()
            query = '''CREATE TABLE IF NOT EXISTS {0} (
                                        S1 REAL,
                                        S2 REAL
                                    );'''.format(table)
            conn = sqlite3.connect(path)
            c = conn.cursor()
            c.execute(query)
            readings = []
            while process:
                data = arduino.readline()[:-2].decode('utf-8')
                data = [float(i) for i in data.split('\t')]
                readings.append(data)
                
                c.execute('INSERT INTO '+ table +' VALUES(?,?);',tuple(data));
                conn.commit()
                if process == False:
                	break
            df = pd.DataFrame(readings, columns=['S1', 'S2'])
            return df
            conn.close()

