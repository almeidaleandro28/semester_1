import sqlite3

connect = sqlite3.connect( "library.db" )

# criar livros
connect.execute(' CREATE TABLE IF NOT EXISTS tb_book (\
                    book_id INTEGER PRIMARY KEY,\
                    book_title VARCHAR(200) NOT NULL,\
                    book_author VARCHAR(200) NOT NULL,\
                    book_year VARCHAR(200) NOT NULL,\
                    book_copies INTEGER NULL,)')