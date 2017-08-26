import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("Create table if not exists book (id integer primary key AUTOINCREMENT,title text , author text , year integer,isbn integer)")
    conn.commit()
    conn.close()

connect()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO BOOK VALUES(Null,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM BOOK")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE  FROM book where id=?",(id,))
    conn.commit()
    conn.close()


def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? or author = ? or year = ? or isbn =?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE BOOK set title =?,author =?,year = ?,isbn = ? WHERE id = ?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()







    
