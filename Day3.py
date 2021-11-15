# Today I want to adapt the mile_time function for use on a large dataset with import functions.
# Pandas appears to be the best option for interfacing with Excel documents, so we will try that.

import pandas as pd
import datetime

df = pd.read_excel(r'C:\Users\Chris\Documents\Day3_Test.xlsx')
print(df)  # Let's check that it worked... (it did!)

# Let's try to rewrite the mile_time function for use with Pandas.
# We need to convert TIME into a str not Series.


def convert_time(x):
    date_time_output = datetime.datetime.strptime(x, "%H:%M:%S")
    x_timedelta = date_time_output - datetime.datetime(1900, 1, 1)
    time_seconds = x_timedelta.total_seconds()
    return time_seconds


def mile_pace_pandas(a, b, c):
    """Returns the pace per mile based on time (in seconds), race distance, and type.
    a = TIME column
    b = DISTANCE column
    c = TYPE column 
    """

    if c == 0:  # If the user's race was ran in miles.
        seconds_pace = (a / b)
        pace = str(datetime.timedelta(seconds=round(seconds_pace)))
        return pace  # The function has to return a value, I guess.
    else:  # If the users race was ran in kilometers.
        seconds_pace = (a / (b * 0.621371))
        pace = str(datetime.timedelta(seconds=round(seconds_pace)))
        return pace


df.SECONDS = df.apply(lambda x: convert_time(x['TIME']), axis=1)
df.PACE = df.apply(lambda x: mile_pace_pandas(x['SECONDS'], x['DISTANCE'], x['TYPE']), axis=1)

print(df)
