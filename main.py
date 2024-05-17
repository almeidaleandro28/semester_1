import sqlite3


def connect_database():
  return sqlite3.connect( "library.db" )

def insert_book( title, author, year, copies ):
  connect = connect_database()
  connect.execute('INSERT INTO tb_book\
                  ( book_title, book_author, book_year, book_copies )\
                   VALUES ( ?,?,?,? )' \
                  ,( title, author, year, copies ) )
  
def insert_user( name, phone, address ):
  connect = connect_database()
  connect.execute('INSERT INTO tb_user\
                  ( user_name, user_phone, user_address )\
                  VALUES ( ?,?,? )'\
                  ,( name, phone, address ))

# insert_book("sem titulo","sem autor",1970, 40)
insert_user("sem nome","61 98174 9346","sem endereco")
