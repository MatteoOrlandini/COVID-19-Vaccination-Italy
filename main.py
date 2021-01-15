import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import csv
import ctypes # to get screen size
from datetime import date # to get today as 'YYYY-MM-DD'

# set SHOW_CHARTS_ENABLED = 1 to show all the charts
SHOW_CHARTS_ENABLED = 0

# set SAVING_ENABLED = 0 if you don't want to save the charts
SAVING_CHARTS_ENABLED = 1

# the folder that contains the saved charts
DESTINATION_FOLDER = "Charts"

# constant for vaccini-summary-latest.csv
INDICE_COLONNA_DOSI_SOMMINISTATE = 1
INDICE_COLONNA_DOSI_CONSEGNATE = 2
INDICE_COLONNA_PERCENTUALE_SOMMINISTRAZIONI = 3

# constant for anagrafica-vaccini-summary-latest.csv
INDICE_COLONNA_TOTALE_VACCINAZIONI_FASCIA_ANAGRAFICA = 1
INDICE_COLONNA_VACCINAZIONI_MASCHI = 2
INDICE_COLONNA_VACCINAZIONI_FEMMINE = 3
INDICE_COLONNA_CATEGORIA_OPERATORI_SANITARI_SOCIOSANITARI = 4
INDICE_COLONNA_CATEGORIA_PERSONALE_NON_SANITARIO = 5
INDICE_COLONNA_CATEGORIA_OSPITI_RSA = 6

def download(fileName, url):	
	print('Downloading CSV dataset from '+url)
	urllib.request.urlretrieve(url, fileName)
	print('CSV dataset \"'+fileName+'\" downloaded')

def csvReader(fileName):	
	with open(fileName, mode='r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		list = []
		for row in csv_reader:
			if line_count == 0:
				# join all items in a tuple into a string, using a ", " character as separator:
				column_names = ", ".join(row)
				columns = column_names.split(", ")
				#print(f'Column names are {", ".join(row)}')
				line_count += 1
				list.append(row)
			else:
				# append row to the list
				list.append(row)
				line_count += 1
		#print(f'Processed {line_count} lines.')
		return list, columns
	
def sumData(list, column, dataType):
	total = 0
	for i in range (0, len (column)-1):
		if (column[i] == dataType):
			index = i
	for i in range (1, len (list)):
		total += int(list[i][index])
	return total

def  getScreenSize():
	user32 = ctypes.windll.user32
	screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
	return screensize

def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def plotData(list, indice_colonna, xlabel, ylabel):
	xdata = []
	ydata = []
	for i in range (1, len (list)):
		xdata.append(list[i][0])
	for i in range (1, len (list)):
		ydata.append(float(list[i][indice_colonna]))
	screenSize = getScreenSize()
	fig = plt.figure(figsize = [screenSize[0]/100, screenSize[1]/100])
	plt.bar(xdata, ydata)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	return fig
	
def plot2Data(list, indice_colonna1, indice_colonna2, xlabel, ylabel, legenda1, legenda2):
	xdata = []
	ydata1 = []
	ydata2 = []
	for i in range (1, len (list)):
		xdata.append(list[i][0])
	for i in range (1, len (list)):
		ydata1.append(float(list[i][indice_colonna1]))
	for i in range (1, len (list)):
		ydata2.append(float(list[i][indice_colonna2]))
		
	larghezza = 0.35  # larghezza delle barre
	screenSize = getScreenSize()
	fig = plt.figure(figsize = [screenSize[0]/100, screenSize[1]/100])
	ax = plt.subplot()
	rect1 = ax.bar(np.arange(len(xdata)) - larghezza/2, ydata1, larghezza, label = legenda1)
	rect2 = ax.bar(np.arange(len(xdata)) + larghezza/2, ydata2, larghezza, label = legenda2)
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	ax.set_xticks(np.arange(len(xdata)))
	ax.set_xticklabels(xdata)
	ax.legend()
	#autolabel(rect1, ax)
	#autolabel(rect2, ax)
	return fig
	
def plot3Data(list, indice_colonna1, indice_colonna2, indice_colonna3, xlabel, ylabel, legenda1, legenda2, legenda3):
	xdata = []
	ydata1 = []
	ydata2 = []
	ydata3 = []
	for i in range (1, len (list)):
		xdata.append(list[i][0])
	for i in range (1, len (list)):
		ydata1.append(float(list[i][indice_colonna1]))
	for i in range (1, len (list)):
		ydata2.append(float(list[i][indice_colonna2]))
	for i in range (1, len (list)):
		ydata3.append(float(list[i][indice_colonna3]))
		
	larghezza = 0.25  # larghezza delle barre
	screenSize = getScreenSize()
	fig = plt.figure(figsize = [screenSize[0]/100, screenSize[1]/100])
	ax = plt.subplot()
	rect1 = ax.bar(np.arange(len(xdata)) - larghezza, ydata1, larghezza, label = legenda1)
	rect2 = ax.bar(np.arange(len(xdata)), ydata2, larghezza, label = legenda2)
	rect3 = ax.bar(np.arange(len(xdata)) + larghezza, ydata3, larghezza, label = legenda3)
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	ax.set_xticks(np.arange(len(xdata)))
	ax.set_xticklabels(xdata)
	ax.legend()
	#autolabel(rect1, ax)
	#autolabel(rect2, ax)
	#autolabel(rect3, ax)
	return fig
	
def saveFigures(date, figures):
	cont = 0
	for figure in figures:
		figManager = plt.get_current_fig_manager()
		figManager.full_screen_toggle()
		figure.savefig(fname = DESTINATION_FOLDER+"/"+str(date)+" - "+str(cont)+".png", format = 'png')
		cont += 1
	
def main():
	today = str(date.today())
	download(fileName = 'vaccini-summary-latest.csv', url = 'https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.csv')
	download(fileName = 'somministrazioni-vaccini-latest.csv', url = 'https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv')
	download(fileName = 'anagrafica-vaccini-summary-latest.csv', url = 'https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/anagrafica-vaccini-summary-latest.csv')
	vaccini_summary_latest, colonne_vaccini_summary_latest = csvReader('vaccini-summary-latest.csv')
	totalData = sumData(vaccini_summary_latest, colonne_vaccini_summary_latest, dataType = 'dosi_somministrate')
	print ('Il totale delle dosi somministrate al', today, 'è:', totalData)
	totalData = sumData(vaccini_summary_latest, colonne_vaccini_summary_latest, dataType = 'dosi_consegnate')
	print ('Il totale delle dosi consegnate al', today, 'è:', totalData)
	figures = []
	figures.append(plotData(vaccini_summary_latest, indice_colonna = INDICE_COLONNA_DOSI_SOMMINISTATE, xlabel = 'Regioni', ylabel = 'Dosi somministrate'))
	figures.append(plotData(vaccini_summary_latest, indice_colonna = INDICE_COLONNA_DOSI_CONSEGNATE, xlabel = 'Regioni', ylabel = 'Dosi consegnate'))
	figures.append(plotData(vaccini_summary_latest, indice_colonna = INDICE_COLONNA_PERCENTUALE_SOMMINISTRAZIONI, xlabel = 'Regioni', ylabel = 'Percentuale somministrazioni'))
	anagrafica_vaccini, colonne_anagrafica_vaccini = csvReader('anagrafica-vaccini-summary-latest.csv')
	figures.append(plotData(anagrafica_vaccini, indice_colonna = INDICE_COLONNA_TOTALE_VACCINAZIONI_FASCIA_ANAGRAFICA, xlabel = 'Fascia anagrafica', ylabel = 'Totale vaccinazioni'))
	figures.append(plot2Data(anagrafica_vaccini, indice_colonna1 = INDICE_COLONNA_VACCINAZIONI_MASCHI, indice_colonna2 = INDICE_COLONNA_VACCINAZIONI_FEMMINE, xlabel = 'Fascia anagrafica', ylabel = 'Totale vaccinazioni', legenda1 = 'Sesso maschile', legenda2 = 'Sesso femminile'))
	figures.append(plot3Data(anagrafica_vaccini, indice_colonna1 = INDICE_COLONNA_CATEGORIA_OPERATORI_SANITARI_SOCIOSANITARI, indice_colonna2 = INDICE_COLONNA_CATEGORIA_PERSONALE_NON_SANITARIO, indice_colonna3 = INDICE_COLONNA_CATEGORIA_OSPITI_RSA, xlabel = 'Fascia anagrafica', ylabel = 'Totale vaccinazioni', legenda1 = 'Operatori sanitari sociosanitari', legenda2 = 'Personale non sanitario', legenda3 = 'Ospiti RSA'))
	if SAVING_CHARTS_ENABLED:
		saveFigures(today, figures)
		print ("Sono stati salvati", len(figures), "grafici nella cartella", DESTINATION_FOLDER)
	if SHOW_CHARTS_ENABLED:
		plt.show()
	
if __name__ == "__main__":
    main()
