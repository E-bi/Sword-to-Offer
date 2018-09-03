import re
from datetime import date,time
today = date.today().day
today_time = time.time().hour
print(today_time)
def chi2engTime(s):
    nowdate = str(today.year)+str(today.month)+str(today.day)+str(toda.year)+str(today.year)+str(today.year)
    dat = ['大前天','前天','昨天','今天','明天','后天','大后天']
    day_time = {'早上','中午','下午','晚上','凌晨'}
    chi_time = {'一':1,'二':2,'两':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10,'十一':11,'十二':12,'十三':13,'十四':14,'十五':15,'十六':16,'十七':17,'十八':18,'十九':19,'二十':20,'二十一':21,'二十二':22,'二十三':23,'二十四':24}
    pat_dat = re.compile('.{1,2}天')
    pat_day = re.compile('.{1,2}天')
    pat_time = re.compile('.{1}点')

    if re.search(pat,s).group()[0] in chi_time:
        print(True)

#chi2engTime('今天明天下午两点')
