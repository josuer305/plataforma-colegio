import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Agregar columna nivel
try:
    cursor.execute("ALTER TABLE usuarios ADD COLUMN nivel TEXT")
    print("Columna 'nivel' agregada")
except:
    print("La columna 'nivel' ya existe")

# Agregar columna salon
try:
    cursor.execute("ALTER TABLE usuarios ADD COLUMN salon TEXT")
    print("Columna 'salon' agregada")
except:
    print("La columna 'salon' ya existe")

conn.commit()
conn.close()
print("Base de datos actualizada correctamente")