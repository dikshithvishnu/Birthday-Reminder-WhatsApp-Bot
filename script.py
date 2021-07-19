# Importing required packages
import pandas as pd
from datetime import date
from sqlalchemy import create_engine
import pywhatkit as kit

# Storing today's date
today = date.today()
# Changing today's date to 'dd-mm' format
today_format = today.strftime('%d-%m')

# Establishing a connection to AWS RDS MySQL instance
connection = create_engine('mysql+pymysql://username:password@database-1.cke6baraqvyb.ap-south-1.rds.amazonaws.com:3306/schema')
df = pd.read_sql('SELECT * FROM `employee_details` ORDER BY EXTRACT(MONTH FROM DOB), EXTRACT(DAY FROM DOB) ASC', connection)
# Storing the DOB column in 'dd-mm' format
df['DOB'] = pd.to_datetime(df['DOB']).dt.strftime('%d-%m')

def check_bday():
    for index, row in df.iterrows():
        try:
            if df['DOB'][index] == today_format:
                # kit.sendwhatmsg() takes Phone Number, message, hour in 24 Hour format, mins from 00-59 respectively as arguments  
                kit.sendwhatmsg("+91{9740979450}", "Today is " + df['Name'][index] + "'s birthday", 11, 24)
        except Exception as e:
            pass

check_bday()

