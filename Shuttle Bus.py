c_dep_wd,c_arr_wd,l_arr_wd=[650,715,740,805,830,855,920,1205,1230,1255,1320,1705,1730,1755,1820,1845,1910,1935,2000,2025],[705,730,755,820,845,910,935,1220,1245,1310,1335,1720,1745,1810,1835,1900,1925,1950,2015,2040],[700,718,736,754,812,830,848,906,1215,1245,1315,1345,1715,1745,1815,1840,1900,1920,1940,2000,2020,2040]#weekday
c_dep_sat,c_arr_sat,l_arr_sat=[905,940,1015,1050,1125,1200,1235,1310,1345],[920,955,1030,1105,1140,1215,1250,1325,1400],[915,945,1015,1045,1115,1145,1215,1245,1315,1345]#sat
c_dep_sun,c_arr_sun,l_arr_sun=[905,940,1015,1050,1125,1200,1705,1730,1755,1820],[920,955,1030,1105,1140,1215,1720,1745,1810,1835],[915,945,1015,1045,1115,1145,1715,1745,1815,1845]#sun

def map(d,loc,t,l1,l2,l3):
    if loc=='home':
        if t>max(l1):
            print('Sorry, no more shuttle service for today.')
        else:
            for char in l1:
                a=char-t
                if a <0:
                    continue
                else:
                    print('The next bus will depart at '+str(char)+' hrs.')
                    break
    elif loc=='mrt':
        if t>max(l2):
            print('Sorry, no more shuttle service for today.')
        else:
            for char in l2:
                a=char-t
                if a <0:
                    continue
                else:
                    print('The next C bus will arrive at '+str(char)+' hrs.')
                    break
            for char in l3:
                a=char-t
                if a <0:
                    continue
                else:
                    print('The next L bus will arrive at '+str(char)+' hrs.')
                    break 

def shuttle_time(d,loc,t):
    if d in [1,2,3,4,5]:
        map(day,location,time,c_dep_wd,c_arr_wd,l_arr_wd)
    elif d==6:
        map(day,location,time,c_dep_sat,c_arr_sat,l_arr_sat)
    elif d==7:
        map(day,location,time,c_dep_sun,c_arr_sun,l_arr_sun)


print('Please enter the day(1-7, 7 for public holidays):')
day=int(input())
print('Please enter the location(mrt or home):')
location=str(input())
print('Please enter the time(in 24h format):')
time=int(input())
shuttle_time(day,location,time)    


