import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()
file = open("BookInfo.txt","w")
file.close()
author = input("Please enter an authors name: ")
sqlCode = "Select * FROM Books WHERE author = '" + author + "';"
cursor.execute(sqlCode)
books = []
for x in cursor.fetchall():
    books.append(x)
for i in range(0, len(books)):
    bookInfo = ""
    for j in range(0,4):
        print(books[i][j])
        bookInfo += " - " + str(books[i][j])
    bookInfo = bookInfo.replace('-','', 1)
    file = open("BookInfo.txt", "a")
    file.write(bookInfo + "\n")
    file.close()


