import sqlite3

connect = sqlite3.connect( "library.db" )

# criar tabela livros
connect.execute(' CREATE TABLE IF NOT EXISTS tb_book (\
                    book_id INTEGER PRIMARY KEY,\
                    book_title VARCHAR(200) NOT NULL,\
                    book_author VARCHAR(200) NOT NULL,\
                    book_year VARCHAR(200) NOT NULL,\
                    book_copies INTEGER NULL )')

# criar tabela usuários
connect.execute(' CREATE TABLE IF NOT EXISTS tb_user (\
                    user_id INTEGER PRIMARY KEY,\
                    user_name VARCHAR(200) NOT NULL,\
                    user_phone VARCHAR(200) NOT NULL,\
                    user_address VARCHAR(200) NOT NULL )')

#criar tabela emprestimo
connect.execute(' CREATE TABLE IF NOT EXISTS tb_loans (\
                    loas_id INTEGER PRIMARY KEY,\
                    loas_book_id INTEGER NOT NULL,\
                    loas_user_id INTEGER NOT NULL,\
                    loas_date_loan NOT NULL,\
                    loas_date_return NOT NULL,\
                    FOREIGN KEY(loas_book_id) REFERENCES  tb_book(book_id),\
                    FOREIGN KEY(loas_user_id) REFERENCES tb_user(user_id) ) ')
