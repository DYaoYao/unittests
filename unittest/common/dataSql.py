
import cx_Oracle as oracle
import pymysql
import redis

from common.readConfig import ReadConfig

def conOracle():
    host = ReadConfig.get_sql("host")
    port = ReadConfig.get_sql("host")
    user = ReadConfig.get_sql("host")
    password = ReadConfig.get_sql("host")
    service = ReadConfig.get_sql("host")

    db = oracle.connect('TFT_TSM/tft_tsm@88.88.16.101:1521/tft_csm')
    cursor = db.cursor()
    sql = "select USERID from TFT_TSM.T_CLIENT_USER_INFO where MSISDN = '18328019517'"
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)
    cursor.close()
    db.close()


def conSql():

    conn = pymysql.connect(host="88.88.16.93",port=60001,user="bwt",password="bwt",database="msx_online")
    cursor = conn.cursor()
    sql = "select USER_ID from user_base where MOBILE_PHONE = '18328019517'"
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)
    cursor.close()
    conn.close()


def conRedis():
    pool = redis.ConnectionPool(host='88.88.16.66', port=6379)
    r = redis.Redis(connection_pool=pool)
    print(r.hget(name='CodeErrorRecord',key='9869485706684416'))

conRedis()