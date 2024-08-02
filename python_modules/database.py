####################################
# @file		    - database.py
# @contributors - 
# @Usage	    - python3 database.py
# @Notes	    - 
####################################
import pymysql

class OurDB:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", user="root", password="aircanadaauto", db="aircanada", use_unicode=True, connect_timeout=1)
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        if not self.cursor:
            print ("Failed to establish Connection to Database")
            exit(1)
            
    def execute_select_query (self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if rows:
            return rows
        else:
            return None
        
    def execute_insertUpdate_query (self, query):
        data = self.cursor.execute(query)
        conn_commit = self.conn.commit()
        
    def GetAllCases(self):
        query = "select * from `case`"
        return self.execute_select_query(query)
        
    def viewcase(self, cta):
        query = f"select * from `case` where `CTA Case ID`='{cta}'"
        return self.execute_select_query(query)
        
if __name__ == "__main__":
    db = OurDB()
    #db.execute_insertUpdate_query("insert into `users` (username, secretKey, mailID) values ('user', 'password', 'test@gmail.com')")
    #print (db.execute_select_query("select * from `users`"))
    print (db.GetAllCases())