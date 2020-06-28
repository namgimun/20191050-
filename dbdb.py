import sqlite3

def dbcon():
    return sqlite3.connect('mydb.db')

def create_table():
    try:
            query = '''
            CREATE TABLE "users" (
                "id"    varchar(50),
                "pw"    varchar(50),
                "name"  varchar(50),
                PRIMARY KEY("id")
            )
         '''
        db = dbcon()
        c = db.cursor()
        c.execute("CREATE TABLE student (num varchar(50), name varchar(50))")
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_all():
    ret = list()
    try:
        db = dbcon()
        c = db.cursor()
        c.execute('SELECT * FROM student')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

def insert_user(id, pw, name):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id, pw, name)
        c.execute("INSERT INTO users VALUES (?, ?, ?)", setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

def select_user(id, pw):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id, pw)
        c.execute('SELCECT * FROM users WHERE id = ? pw = ?', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

def check_id(id, pw):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id)
        c.execute('SELCECT * FROM users WHERE id = ?', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

def select_data(num, name):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (num, name)
        c.execute("INSERT INTO student VALUES = (?, ?)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

def select_num(num):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (num,)
        c.execute('SELCECT * FROM student WHERE num = ?', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret 

#create_table()
#insert_user('abc', '1234', '에비시')
#insert_data('20201236', '디비')
#ret = select_all()
#print(ret)
ret = select_user('abc', '1234')
print(ret)