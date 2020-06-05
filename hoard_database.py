from sqlite3 import connect
from contextlib import contextmanager

class HoardDatabase:
    def __init__(self, books_database):
        self.books_database = books_database

    @contextmanager
    def books_table(self, cur):
        cur.execute("create table if not exists books(id integer PRIMARY KEY, Month text, Book text, Author text)")
        try:
            yield
        finally:
            pass

    def populate_table(self):
        with connect(self.books_database ) as conn:
            while True:
                month = input("Please enter a month: ")
                book = input("Please enter a book: ")
                author = input("Please enter author's name: ")

                parameters = (month, book, author)
                cur = conn.cursor()
                with self.books_table(cur):
                    cur.execute("INSERT into books (Month, Book, Author) values(?, ?, ?)", parameters)
                    continue_message = input("(if you want to continue, enter 'c' else enter anything else): ")
                    continue_message = continue_message.lower()
                    if continue_message != "c":
                        break
                    else:
                        continue
                    for row in cur.execute('select Month, Book, Author from books'):
                        print(row)
                    print(f"books table is created and populated")

    def access_data(self, data):
        with connect(self.books_database) as conn:
                cur = conn.cursor()
                for row in cur.execute('select Month, Book, Author from books'):
                    if row[0] == data:
                        yield row
                else:
                    print("Month not found")

if __name__ == '__main__':
    path = "./sqlite/db/hoard.db"
    # hdb = HoardDatabase(path)
    # data = "January"
    # hdb.access_data(data)
