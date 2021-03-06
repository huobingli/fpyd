from mysql_comm.mysql_comm import *
from redis_comm.redis_comm import *

def insert_datas(datas):     
    with UsingMysql(log_time=True) as um:
        pass

def insert_data(database, data):
    with UsingMysql(log_time=True) as um:
        sql = "insert into " + database + "(fp_id, fp_title, fp_res_org, fp_report_time, fp_stock_name, fp_stock_code, fp_source_id, fp_is_stock)  \
        values(%s, %s, %s, %s, %s, %s, %s, %s)" 
        params = ('%s' % data[0], '%s' % data[1], "%s" % data[2], "%s" % data[3], "%s" % data[4], "%s" % data[5], "%s" % data[6], "%d" % data[7])
        # print(sql)
        um.cursor.execute(sql, params)

def test_insert_data():
    pass

def fecth_data(database, condition=""):
    with UsingMysql(log_time=True) as um:
        sql = 'select * from %s %s' % (database, condition)
        print(sql)
        um.cursor.execute(sql)
        data_list = um.cursor.fetchall()
        print('-- 总数: %d' % len(data_list))
        return data_list

def test_feach_data():
    pass

def update_data(database, setdata, condition=""):
    with UsingMysql(log_time=True) as um:
        sql = "update %s %s %s" % (database, setdata, condition)
        um.cursor.execute(sql)

def test_update_data():
    pass

def delete_data(database, condition=""):
    with UsingMysql(log_time=True) as um:
        sql = 'delete from %s %s' % (database, condition)
        um.cursor.execute(sql)

def redis_set(key, value):
    with UsingRedis(log_time=True) as ur:
        ur.set_key_value(key, value) 

def redis_get(key):
    with UsingRedis(log_time=True) as ur:
        return ur.get_key_value(key)

def redis_zset_set(set, key, value):
    with UsingRedis(log_time=True) as ur:
        ur.zset_set_key_value(set, key, value) 

def redis_zset_get(key):
    with UsingRedis(log_time=True) as ur:
        return ur.zset_get_key_value(key)

if __name__ == '__main__':
    pass