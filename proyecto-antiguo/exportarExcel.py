from openpyxl import Workbook
from db import MatrizQ

obj = MatrizQ.query.all () 
matriz =(obj[-1])

filesheet = "exportarExcel.xlsx"
wb = Workbook()
hoja = wb.active

# primer fila

hoja['B1'] = matriz.Q[0,0,0] #el primer valor es la coordenada en y(fila) de los cuadrados 
hoja['B3'] = matriz.Q[0,0,1] #el segundo valor es la coordenada en x(columna) de los cuadrados
hoja['A2'] = matriz.Q[0,0,2] # tercer valor triangulos (0=arriba,1=abajo,2=izquierda,3=derecha) 
hoja['C2'] = matriz.Q[0,0,3]

hoja['G1'] = matriz.Q[0,1,0]
hoja['G3'] = matriz.Q[0,1,1]
hoja['F2'] = matriz.Q[0,1,2]
hoja['H2'] = matriz.Q[0,1,3]

hoja['L1'] = matriz.Q[0,2,0]
hoja['L3'] = matriz.Q[0,2,1]
hoja['K2'] = matriz.Q[0,2,2]
hoja['M2'] = matriz.Q[0,2,3]

# segunda fila

hoja['B6'] = matriz.Q[1,0,0] #el primer valor es la coordenada en y(fila) de los cuadrados 
hoja['B8'] = matriz.Q[1,0,1] #el segundo valor es la coordenada en x(columna) de los cuadrados
hoja['A7'] = matriz.Q[1,0,2] # tercer valor triangulos (0=arriba,1=abajo,2=izquierda,3=derecha) 
hoja['C7'] = matriz.Q[1,0,3]

hoja['G6'] = matriz.Q[1,1,0]
hoja['G8'] = matriz.Q[1,1,1]
hoja['F7'] = matriz.Q[1,1,2]
hoja['H7'] = matriz.Q[1,1,3]

hoja['L6'] = matriz.Q[1,2,0]
hoja['L8'] = matriz.Q[1,2,1]
hoja['K7'] = matriz.Q[1,2,2]
hoja['M7'] = matriz.Q[1,2,3]

# tercera fila

hoja['B11'] = matriz.Q[2,0,0] #el primer valor es la coordenada en y(fila) de los cuadrados 
hoja['B13'] = matriz.Q[2,0,1] #el segundo valor es la coordenada en x(columna) de los cuadrados
hoja['A12'] = matriz.Q[2,0,2] # tercer valor triangulos (0=arriba,1=abajo,2=izquierda,3=derecha) 
hoja['C12'] = matriz.Q[2,0,3]

hoja['G11'] = matriz.Q[2,1,0]
hoja['G13'] = matriz.Q[2,1,1]
hoja['F12'] = matriz.Q[2,1,2]
hoja['H12'] = matriz.Q[2,1,3]

hoja['L11'] = matriz.Q[2,2,0]
hoja['L13'] = matriz.Q[2,2,1]
hoja['K12'] = matriz.Q[2,2,2]
hoja['M12'] = matriz.Q[2,2,3]




wb.save(filesheet)
