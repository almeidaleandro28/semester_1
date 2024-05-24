import sqlite3


def connect_database():
  return sqlite3.connect( "library.db" )

def insert_book( title, author, year, copies ):
  connect = connect_database()
  connect.execute('INSERT INTO tb_book\
                  ( book_title, book_author, book_year, book_copies )\
                   VALUES ( ?,?,?,? )' \
                  ,( title, author, year, copies ) )
  connect.commit()
  connect.close()
  
def insert_user( name, phone, address ):
  connect = connect_database()
  connect.execute('INSERT INTO tb_user\
                  ( user_name, user_phone, user_address )\
                  VALUES ( ?,?,? )'\
                  ,( name, phone, address ))
  connect.commit()
  connect.close()

def insert_loan( book_id, user_id, date_loan, date_return ):
  connect = connect_database()
  connect.execute('INSERT INTO tb_loan\
                ( loan_book_id, loan_user_id, loan_date_loan, loan_date_return)\
                VALUES ( ?,?,?,? )' \
                ,( book_id, user_id, date_loan, date_return ) )
  connect.commit()
  connect.close()
  
# relátorios
def show_books( ):
  connect = connect_database()
  books = connect.execute('SELECT * FROM tb_book').fetchall()
  connect.close()

  print("---- LISTA DE LIVROS -----")
  if books:
    for book in books:
      print(f"BOOK ID: { book[ 0 ] }") 
      print(f"BOOK TITLE: { book[ 1 ] }") 
      print("\n")
  else:
    print("NAO TEM NENHUM LIVRO CADASTRADO!")


def show_users():
  connect = connect_database()
  users = connect.execute('SELECT * FROM tb_user').fetchall()
  connect.close()

  print("LISTA DE USUÁRIOS CADATRADOS")
  if users:
    for user in users:
      print(f"NAME: { user[1]} ID: { user[0] }")
  else:
    print("NENHUM USUÁRIO CADASTRADO!")

def show_books_loan():
  connect = connect_database()
  query = connect.execute('SELECT tb_book.book_title,\
                              tb_user.user_name,\
                              tb_loan.loan_date_loan, tb_loan.loan_date_return\
                          FROM  \
                            tb_book\
                            INNER JOIN tb_loan ON tb_loan.loan_book_id = tb_book.book_id\
                            INNER JOIN tb_user ON tb_user.user_id = tb_loan.loan_user_id\
                            WHERE tb_loan.loan_date_return IS NULL\
                          ').fetchall()
  connect.close()
  return query

# insert_user("leandro","61 98174 9346","cnf 01")
# insert_user("tais","61 88174 9346","cnf 03")

# insert_book("titulo 1","autor 1",1970, 40)
# insert_book("titulo 2","autor 2",1971, 30)
# insert_book("titulo 3","autor 3",1972, 20)
# insert_book("titulo 4","autor 4",1999, 15)

# insert_loan(3, 1, "2024:05:01", "2024:05:30")
# insert_loan(3, 2, "2024:05:03",  None)
# insert_loan(1, 1, "2024-05-03", None)

# show_books()
print( show_books_loan() ) 
