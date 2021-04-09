from openpyxl import load_workbook

ws = load_workbook('DATA.xlsx') #ARCHIVO XLSX DATOS

hoja = ws.active


contador = 1

for x in range(2,10627): #CANTIDAD DE CELDAS Y HASTA QUE PUNTO N* VAN
	Celda1 = 'B'+str(x) #NOMBRE DE LA CELDA
	Celda2 = 'B'+str(x+1)
	Celda3 = 'C'+str(x)



	if hoja[Celda1].value == hoja[Celda2].value:


		hoja[Celda3].value = contador
	else:
		hoja[Celda3].value = contador
		contador = contador + 1




ws.save('DATA.xlsx') #ARCHIVO DE SALIDA
#Renta_2021_SII_V1