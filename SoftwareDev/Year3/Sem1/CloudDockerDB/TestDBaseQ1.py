import pymysql
conn = pymysql.connect(db='testapp', user='root', passwd='admin', host='localhost',port=3306)
cur = conn.cursor()
cur.execute("select * from testapp.Teams")
allTeams=cur.fetchall()
print()
print("Team          Score")
print("===================")
for team in allTeams:
    print(team[0] + '\t' + str(team[1]))
