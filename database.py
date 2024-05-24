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
connect.execute(' CREATE TABLE IF NOT EXISTS tb_loan (\
                    loan_id INTEGER PRIMARY KEY,\
                    loan_book_id INTEGER NOT NULL,\
                    loan_user_id INTEGER NOT NULL,\
                    loan_date_loan TEXT NOT NULL,\
                    loan_date_return TEXT NULL,\
                    FOREIGN KEY(loan_book_id) REFERENCES  tb_book(book_id),\
                    FOREIGN KEY(loan_user_id) REFERENCES tb_user(user_id) ) ')

connect.close()