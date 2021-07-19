import pandas as pd
from datetime import date
from sqlalchemy import create_engine
import pywhatkit as kit

today = date.today()
today_format = today.strftime('%d-%m')

connection = create_engine('mysql+pymysql://admin:shitindianssay@database-1.cke6baraqvyb.ap-south-1.rds.amazonaws.com:3306/memechat')
df = pd.read_sql('SELECT * FROM `employee_details` ORDER BY EXTRACT(MONTH FROM DOB), EXTRACT(DAY FROM DOB) ASC', connection)
df['DOB'] = pd.to_datetime(df['DOB']).dt.strftime('%d-%m')
# print(df)

def check_bday():
    for index, row in df.iterrows():
        try:
            if df['DOB'][index] == today_format:
                kit.sendwhatmsg("+91{9740979450}", "Today is " + df['Name'][index] + "'s birthday", 11, 24)
                #kit.sendwhatmsg_to_group("Chess", "Today is " + df['Name'][index] + "'s birthday", 1, 11)
                #kit.image_to_ascii_art("C:/Users/user/Downloads/wie05t4a9mb71.jpg", "C:/Users/user/Downloads/wie05t4a9mb71")
                # kit.playonyt("Yah Mean")
        except Exception as e:
            pass

check_bday()

