import pymysql
conn = pymysql.connect(db='testapp', user='root', passwd='admin', host='localhost',port=3306)
cur = conn.cursor()
cur.execute("select * from testapp.Teams")
allTeams=cur.fetchall()[0][0]
print(allTeams)
