import sqlite3

conn = sqlite3.connect("usuarios.db")

try:
  conn.execute(
    """
    create table if not exists usuarios (
      id_usuario integer primary key autoincrement,
      usuario text,
      password text
    );
    """)
  
  conn.execute(
    """
    insert into usuarios (usuario, password) values (?,?)""",
    ("admin", "admin"))


except sqlite3.OperationalError as err:
  print("la tabla ya existe", err)
  
conn.commit()
conn.close()