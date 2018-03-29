import pymysql
import pymysql.cursors
import os


def dbhandle_online():
    host = '127.0.0.1'
    user = 'root'
    passwd = '12345'
    charset = 'utf8'
    conn = pymysql.connect(
        host=host,
        user=user,
        passwd=passwd,
        charset=charset,
        use_unicode=False
    )
    return conn