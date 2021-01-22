import pymysql
from string import Template


def userExist(qqnumber):
    code = 0
    db = pymysql.connect(host='localhost', user='root',password='lyq990515',database='qqbot')
    cursor = db.cursor()
    query = "SELECT *" + " FROM user" + " WHERE qq_num=" + qqnumber
    cursor.execute(query)
    res = cursor.fetchone()
    if res:
        code = 1
    else:
        code = 0

    db.close()

    return code

def getUserAccount(qq_num):
    db = pymysql.connect(host='localhost', user='root',password='lyq990515',database='qqbot')
    cursor = db.cursor()
    query = "SELECT card_num, pwd" + " FROM user" + " WHERE qq_num=" + qq_num
    cursor.execute(query)
    res = cursor.fetchone()
    if res:
        db.close()
        return res[0], res[1]
    else:
        db.close()
        return 0

def insertUser(qq_num, card_num, password):
    db = pymysql.connect(host='localhost', user='root', password='lyq990515', database='qqbot')
    cursor = db.cursor()
    query = "INSERT INTO user(qq_num, card_num, pwd) VALUES('%s', '%s', '%s')" % (qq_num, card_num, password)

    cursor.execute(query)
    db.commit()
    db.close()

def updateUser(qq_num, card_num, password):
    db = pymysql.connect(host='localhost', user='root', password='lyq990515', database='qqbot')
    cursor = db.cursor()
    query = "UPDATE user SET card_num='%s',pwd='%s' WHERE qq_num='%S'" % (card_num, password, qq_num)

    cursor.execute(query)
    db.commit()
    db.close()



