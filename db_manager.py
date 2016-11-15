import psycopg2

#23456789012345
class DbManager:
    def __init__(self):
        self.conn_str = "dbname=jnv user=postgres password=postgres"

#    def __init__(self, dbname, user, password):
#        self.dbname = dbname
#        self.user = user
#        self.password = password
         
    def fetch_all(self, sql):
        """Fetches all records."""
        con = psycopg2.connect(self.conn_str)
        cur = con.cursor()
        cur.execute(sql)
        records = cur.fetchall()
        con.commit
        cur.close
        con.close
        return records

    def fetch_one(self, sql):
        """Fetches 1 record."""
        con = psycopg2.connect(self.conn_str)
        cur = con.cursor()
        cur.execute(sql)
        record = cur.fetchone()
        con.commit
        cur.close
        con.close
        return record

    
## TODO: Unit test
if __name__ == "__main__":
    sql = """ SELECT * FROM users """
    dbm = DbManager()
    print(dbm.fetch_all(sql))

# 


