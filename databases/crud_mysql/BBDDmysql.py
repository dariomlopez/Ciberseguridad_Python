import mysql.connector


class Articulos:
  
  def conexion(self):
    conn = mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="",
                                   database="test")
    return conn

  def agregar(self, datos):
    conn = self.conexion()
    cursor = conn.cursor()
    cursor.execute("insert into articulos (descripcion, precio) "
                   "values (%s, %s)", datos)
    
    conn.commit()
    conn.close()
    
  def agregar_varios(self, datos):
    conn = self.conexion()
    cursor = conn.cursor()
    cursor.execute(
      "insert into articulos (descripcion, precio) "
      "values (%s, %s)", datos)
    
    conn.commit()
    conn.close()
    

  def consulta_articulo(self, datos):
    conn = self.conexion()
    try:
      cursor = conn.cursor()
      cursor.execute("select descripcion, precio from articulos where id = %s", datos)
      return cursor.fetchall()
    finally:
      conn.close()
    
  def consultar_todos(self):
    conn = self.conexion()
    try:
      cursor = conn.cursor()
      cursor.execute(
        "select id, descripcion, precio from articulos")
      return cursor.fetchall()
    finally:
      conn.close()
      
  def quitar_articulo(self, datos):
    conn = self.conexion()
    try:
      cursor = conn.cursor()
      cursor.execute(
        "delete from articulos where id = %s", datos)
      conn.commit()
      return cursor.rowcount
    finally:
      conn.close()
      
  def modificar_articulo(self, datos):
    conn = self.conexion()
    try:
      cursor = conn.cursor()
      cursor.execute(
        "update articulos set descripcion = %s, precio = %s where "
        "id = %s", datos)
      conn.commit()
      return cursor.rowcount
    finally:
      conn.close()