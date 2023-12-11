import mysql.connector


class Articulos:
  
  # conexión a la base de datos
  def conexion(self):
    conn = mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="",
                                   database="test")
    return conn
  
  # agregar un articulo
  def agregar(self, datos):
    conn = self.conexion()
    cursor = conn.cursor()
    
    cursor.execute("insert into articulos (descripcion, precio) "
                   "values (%s, %s)", datos)
    conn.commit()
    # Recuperar última fila afectada
    # cursor.lastrowid
    cursor.execute("select last_insert_id()")
    last_id = cursor.fetchone()[0]
    
    conn.close()
    return last_id
    
  def agregar_varios(self, datos):
    conn = self.conexion()
    cursor = conn.cursor()
    
    # datos = [ ("Bici", 450), ("Chalecos", 50), ("Barbas", 670), ("Ojos", 810), ("Botellas", 45),  ]
    
    query = "insert into articulos (descripcion, precio) values (%s, %s)"
    cursor.executemany(query, datos)
    
    conn.commit()
    conn.close()
  
  # consultar un articulo por id
  def consulta_articulo(self, datos):
    conn = self.conexion()
    try:
      cursor = conn.cursor()
      cursor.execute("select descripcion, precio from articulos where id = %s", datos)
      return cursor.fetchall()
    finally:
      conn.close()
    
  # función que devuelve todos los articulos existentes
  def consultar_todos(self):
    conn = self.conexion()
    try:
      cursor = conn.cursor()
      cursor.execute(
        "select id, descripcion, precio from articulos")
      return cursor.fetchall()
    finally:
      conn.close()
  
  # función para quitar una articulo por id
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
      
  # función para modificar una articulo
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
  
  # función para crear una base de datos
  def crear_basedatos(self, nombre_db):
    conn = self.conexion()
    try:
      cursor = conn.cursor()
      cursor.execute(
        f"create database `{nombre_db}`")
    finally:
      conn.close()
  
  # función para borrar una base de datos
  def borrar_basedatos(self, nombre_db):
    conn = self.conexion()
    try:
      cursor = conn.cursor()
      cursor.execute(
        f"drop database {nombre_db}")
    finally:
      conn.close()
      
  # funcion para crear una tabla
  def crear_tabla(self, nombre_db, nombre_tabla, columnas):
    conn = self.conexion()
    try:
      cursor = conn.cursor()
      cursor.execute(f"use {nombre_db}")
      cursor.execute(f"create table {nombre_tabla} ({columnas})")
      conn.commit()
    finally:
      conn.close()
      
  # funcion para borrar una tabla y crear otra del mismo nombre
  def borrar_crear_tabla(self, nombre_tabla):
    conn = self.conexion()
    try:
      cursor = conn.cursor()
      cursor.execute(f"drop table if exists {nombre_tabla}")
      # cursor.execute(
      #   f"create table {nombre_tabla}")
      conn.commit()
    finally:
      conn.close()