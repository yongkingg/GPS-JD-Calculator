import math

# math.trunc => 소수점 버림 함수 
def date2gwgs(year,month,day,hour,min,sec):
    ut = (hour)+ (min/60) + (sec/360)
    jd = math.trunc(365.25 * year) + math.trunc(30.6001 * (month + 1)) + day + (ut/24) + 1720981.5
    # gw
    print("jd : " + str(jd))
    print("gw : " + str(math.trunc((jd-2444244.5)/7))) 

    # gs
    n = math.trunc(math.trunc(jd+1.5)%7)
    print(n)
    print("gs : " + str( math.trunc((n * 86400) + hour*3600 + min*60 + sec )))

def date2doy(year, month, day):
    doy = 0
    days = 31 # 31일이 일수인 달이 많으므로, 31일을 기본 days 값으로 설정 
    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0): # 윤년 => 2월이 29일까지 
        print("윤년")
        for index in range(0,month): #반복문을 통해, 입력된 달의 이전 달까지의 모든 일들을 더함
            if index + 1 == month: 
                doy += day #만약 index 값이 입력된 달과 같아지면, 입력된 일수를 더함
            elif index + 1 < month: #index 값이 입력된 달과 같아질때까지, 기존의 일수를 더함 
                if (index+1) in [1,3,5,7,9,11]: 
                    days = 31
                elif (index+1) in [4,6,8,10,12]:
                    days = 30
                elif (index+1) == 2:
                    days = 29       
                doy += days
            else:
                pass
    elif year % 4 != 0: # 평년 => 2월이 28일까지 
        print("평년")
        for index in range(0,month):
            if index + 1 == month:
                doy += day
            elif index + 1 < month: 
                if (index+1) in [1,3,5,7,9,11]: 
                    days = 31
                elif (index+1) in [4,6,8,10,12]:
                    days = 30
                elif (index+1) == 2:
                    days = 28       
                doy += days
            else:
                pass
    if len(str(doy)) == 1: # 자리수에 따라, 1자리면 앞에 00 추가 
        print("00" + str(doy))
    elif len(str(doy)) == 2: # 자리수에 따라, 2자리면 앞에 0 추가 
        print("0" + str(doy))
    elif len(str(doy)) == 3: # 자리수에 따라, 3자리면 그대로 출력
        print(str(doy))

date2gwgs(2002,5,9,10,0,3)













