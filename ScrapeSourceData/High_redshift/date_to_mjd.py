import math
import pandas as pd
import os
import glob

def date_to_jd(year, month, day):
    """
    Convert a date to Julian Day.

    Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet',
        4th ed., Duffet-Smith and Zwart, 2011.

    Parameters
    ----------
    year : int
        Year as integer. Years preceding 1 A.D. should be 0 or negative.
        The year before 1 A.D. is 0, 10 B.C. is year -9.

    month : int
        Month as integer, Jan = 1, Feb. = 2, etc.

    day : float
        Day, may contain fractional part.

    Returns
    -------
    jd : float
        Julian Day

    Examples
    --------
    Convert 6 a.m., February 17, 1985 to Julian Day

    >>> date_to_jd(1985,2,17.25)
    2446113.75

    """
    if month == 1 or month == 2:
        yearp = year - 1
        monthp = month + 12
    else:
        yearp = year
        monthp = month

    # this checks where we are in relation to October 15, 1582, the beginning
    # of the Gregorian calendar.
    if ((year < 1582) or
            (year == 1582 and month < 10) or
            (year == 1582 and month == 10 and day < 15)):
        # before start of Gregorian calendar
        B = 0
    else:
        # after start of Gregorian calendar
        A = math.trunc(yearp / 100.)
        B = 2 - A + math.trunc(A / 4.)

    if yearp < 0:
        C = math.trunc((365.25 * yearp) - 0.75)
    else:
        C = math.trunc(365.25 * yearp)

    D = math.trunc(30.6001 * (monthp + 1))

    jd = B + C + D + day + 1720994.5

    return jd

def jd_to_mjd(year, month, day):
    """
    Convert Julian Day to Modified Julian Day

    Parameters
    ----------
    jd : float
        Julian Day

    Returns
    -------
    mjd : float
        Modified Julian Day

    """
    return date_to_jd(year, month, day) - 2400000.5

path = 'D:/PythonProjects/scraping/ScrapeSourceData/High_redshift'
dat_paths = []
for filename in glob.glob(path+"/*/*.dat"):
    dat_paths.append(filename)

for abs_path in dat_paths:
    data = pd.read_csv(abs_path, sep='|', header=None, skiprows=1,
                       low_memory = False, skipinitialspace=True,)
    del data[0]
    data.columns =["obsid","start_time","uvot_expo_uu","uvot_expo_bb","uvot_expo_vv","uvot_expo_w1","uvot_expo_w2","uvot_expo_m2","xrt_expo_wt","xrt_expo_pc","_Search_Offset"]
    splited_mjd= [data["start_time"][i].split(" ")[0].split("-") for i in range(len(data["start_time"]))]
    mjd_col = [jd_to_mjd(int(splited_mjd[k][0]),int(splited_mjd[k][1]), int(splited_mjd[k][2])) for k in range(len(splited_mjd))]
    data["MJD"] = mjd_col
    print(data)
    #data.to_csv(abs_path)


