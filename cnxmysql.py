
# Por Jose Fernando Galindo
# Ingrese a la pagina: https://colab.research.google.com/
# Descargue la base de datos Neptuno.sqlite en:
# http://fegasusoft.com/innca/sql/movil/tool.htm
#pip install pandas


#https://www.w3schools.com/python/python_mysql_getstarted.asp
#python -m pip install mysql-connector
import pymysql
import  sqlite3
import pandas as pd
import numpy as np
import pyodbc
from os import getcwd

class Cnx:
	con=0
	Datos=0
	def __init__(self,TIPO="Mysql",HOST="localhost",USUA="root",CLA="", DB=""):
		self.Base=DB
		self.Usua=USUA
		self.Cla=CLA
		self.Host=HOST
		self.Tipo=TIPO
	def Conecta(self):
		if self.Tipo=="mysql":
			self.con = pymysql.connect(self.Host,self.Usua,self.Cla,self.Base)
		elif self.Tipo=="sqlite":
			self.con = sqlite3.connect(self.Base) 
		elif self.Tipo=="access":
			self.con = pyodbc.connect("DSN="+self.Base)
		self.cursorObj = self.con.cursor()
	def Consulta(self, query):
		self.df = pd.read_sql_query(query, self.con)
		self.df=list(self.df)
		self.cursorObj.execute(query)
		self.rows = self.cursorObj.fetchall()
	def ConsultaDML(self, query):
		try:
			self.cursorObj.execute(query)
			self.con.commit()
		except Exception as e:
			print(e)
	def ConsultaDDL(self, query):
		try:
			self.df = pd.read_sql_query(query, self.con)
			self.df=list(self.df)
			self.cursorObj.execute(query)
			self.rows = self.cursorObj.fetchall()
		except IOError as e:
			print(e)
	def TotalColumnas(self):
		return len(self.df)
	def TotalLineas(self):
		return(len(self.rows))
	def CargaFilas(self):
		self.Datos= pd.DataFrame(self.rows)
		for i in range(len(self.df)):
  			self.Datos=self.Datos.rename(columns={i:self.df[i]})
		return self.Datos
	def MuestraFila(self, fila):
		return self.rows[fila]
	def MuestraCol(self, fila=0,columna=0):
		return self.rows[fila][columna]
	def Cerrar(self):
		self.con.close()
		print("**Cnx Cerrada **")
print("***************** SQLITE *********************************")
c=Cnx(TIPO="sqlite",DB="Neptuno.sqlite")
c.Conecta()
query='SELECT * FROM proveedores'
c.Consulta(query)
print("Filas:",c.TotalLineas())
print(c.MuestraCol(2,2))
print(c.TotalColumnas())
print(c.CargaFilas())
c.Cerrar()

print("**************** MYSQL **********************************")
c=Cnx(TIPO="mysql",HOST="localhost",DB="Neptuno")
c.Conecta()
query='SELECT * FROM prueba1'
c.Consulta(query)
print("Filas:",c.TotalLineas())
print(c.MuestraCol(2,1))
print(c.TotalColumnas())
print(c.CargaFilas())
c.Cerrar()
print("******************* ODBC *******************************")
database = "Neptuno.mdb"
DSN="Neptunito"
c=Cnx(TIPO="access",DB=DSN)
c.Conecta()
query='SELECT * FROM clientes'
c.Consulta(query)
print("Filas:",c.TotalLineas())
print(c.MuestraCol(2,5))
print(c.TotalColumnas())
print(c.CargaFilas())
c.Cerrar()

