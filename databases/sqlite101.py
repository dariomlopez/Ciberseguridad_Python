import sqlite3

# conexión a base de datos
conn = sqlite3.connect("./test.db")

try:
  '''
  conn.execute("""
  DROP TABLE IF EXISTS articulos;
  """)
  
  conn.execute("""
  CREATE TABLE IF NOT EXISTS articulos (
    articulo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    precio REAL,
    descripcion TEXT
  );""")
  '''
  
  '''
  conn.execute(
    INSERT INTO articulos (nombre, precio, descripcion)
        VALUES ("Bananas", 20.99, "Son bananas");""")
  '''
  
  conn.execute(
    """INSERT INTO articulos (nombre, precio, descripcion) VALUES (?,?,?)""",("Kiwis", 45.99, "Son kiwis"))
  
except sqlite3.OperationalError as err:
  print("la tabla ya existe", err)
  
conn.commit()
conn.close()


