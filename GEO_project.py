import pandas as pd
import sys
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s:\n %(message)s',level=logging.NOTSET)

log = logging.getLogger('normal_log')

# Take the first parameter after u call your script
ARCH = sys.argv[1]
log.debug('Will be used this arch %s',ARCH)

# Reading the data
df = pd.read_csv(ARCH)

#Logging on terminal a small set of your data
log.info(df.head())

# Data Cleaning (Data Munging)
df['dt_notific'] = pd.to_datetime(df['dt_notific'])
df['mes'] = df['dt_notific'].dt.month
df.fillna('No data')
df.drop_duplicates()

final_df = df[['num_not','racacor','evolucao']]
log.info(final_df.head())

#Exporting Data
final_df.to_csv('cleaned_df.csv',header=True,index=False)