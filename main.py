from db_manager import DbManager
from sys import argv
import datetime

def usage():
    #TODO: 
    #Note: argv[0] is program name
    print(argv[0])

if len(argv) > 1:
    yyyymm = argv[1]
    year = int(yyyymm[0:4])
    month = int(yyyymm[4:6])
else:
    today = datetime.datetime.today()
    year = today.year
    month = today.month
    print(today.day)

print(year, month)
#yyyymmddhhmmss = 

print(argv)


cond_tokyo    = "pref_cd = 13"
cond_chiba    = "pref_cd = 12"
cond_kanagawa = "pref_cd = 14   "
cond_others   = "pref_cd not in (12, 13, 14)" 


sql = """ select 
 sum( case when {cond_tokyo}    then 1 else 0 end ) as cnt_tokyo
,sum( case when {cond_chiba}    then 1 else 0 end ) as cnt_chiba
,sum( case when {cond_kanagawa} then 1 else 0 end ) as cnt_kanagawa
,sum( case when {cond_others}   then 1 else 0 end ) as cnt_others
from users 
""".format(cond_tokyo=cond_tokyo, cond_kanagawa=cond_kanagawa, cond_chiba=cond_chiba, cond_others=cond_others)

print(sql)
dbm = DbManager()
result = dbm.fetch_one(sql)
print(result)
(cnt_tokyo, cnt_chiba, cnt_kanagawa, cnt_others) = result


text = """キャリア 現在の会員数レポート {year}年{month}月
東京: {cnt_tokyo}
千葉：{cnt_chiba}
神奈川：{cnt_kanagawa}
その他：{cnt_others}
""".format(year=year, month=month, cnt_tokyo=cnt_tokyo, cnt_chiba=cnt_chiba, cnt_kanagawa=cnt_kanagawa, cnt_others=cnt_others)


print(text)
