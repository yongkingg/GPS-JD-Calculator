import math

def date2gwgs(year,month,day,hour,min,sec):
    ut = (hour)+ (min/60) + (sec/360)
    jd = math.trunc(365.25 * year) + math.trunc(30.6001 * (month + 1) + day + ut/24 + 1720981.5)
    print("Julian Day : " + " = " + str(jd))

date2gwgs(2019,6,21,17,30,0)


















