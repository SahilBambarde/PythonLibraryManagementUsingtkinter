import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer,Issuer text)")
        self.conn.commit()

    def insert(self,title,author,year,isbn,Issuer):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?)",(title,author,year,isbn,Issuer))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn="",Issuer=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=? OR Issuer=?", (title,author,year,isbn,Issuer))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn,Issuer):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=?, Issuer=? WHERE id=?",(title,author,year,isbn,Issuer,id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()



#insert("The Sun","John Smith",1918,913123132,mrunmai)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))
