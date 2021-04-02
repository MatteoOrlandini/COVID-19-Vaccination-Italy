import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import csv
import ctypes # to get screen size
from datetime import date # to get today as 'YYYY-MM-DD'
import os

# set SHOW_CHARTS_ENABLED = 1 to show all the charts
SHOW_CHARTS_ENABLED = 0

# set SAVING_ENABLED = 0 if you don't want to save the charts
SAVING_CHARTS_ENABLED = 1

# the folder that contains the saved charts
DESTINATION_FOLDER = "Charts"

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
				metadata = column_names.split(", ")
				#print(f'Column names are {", ".join(row)}')
				line_count += 1
				list.append(row)
			else:
				# append row to the list
				list.append(row)
				line_count += 1
		#print(f'Processed {line_count} lines.')
		return list, metadata
	
def sumData(list, metadata, dataType):
	total = 0
	for i in range (0, len (metadata)-1):
		if (metadata[i] == dataType):
			index = i
	for i in range (1, len (list)):
		total += int(list[i][index])
	return total

def  getScreenSize():
	user32 = ctypes.windll.user32
	screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
	return screensize

def autolabel(rects, ax):
    # Attach a text label above each bar in *rects*, displaying its height.
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def fill_list_with_string(list, column_index):
	data = []
	for i in range (1, len (list)):
		data.append(list[i][column_index])
	return data
	
def fill_list_with_column_data(list, column_index):
	data = []
	for i in range (1, len (list)):
		try:
			data.append(float(list[i][column_index]))
		except ValueError as e:
			#print(e)
			return None
	return data
		
def get_index_from_column_name(metadata, column_name):
	for i in range (1, len(metadata)):
		if (metadata[i] == column_name):
			return i

def plotData(list, column_index):
	xdata = fill_list_with_string(list, 0)
	ydata = fill_list_with_column_data(list, column_index)
	if (ydata == None):
		return None
	else:
		# get screen size to plot graphs full screen
		screenSize = getScreenSize()
		fig = plt.figure(figsize = [screenSize[0]/100, screenSize[1]/100])
		plt.bar(xdata, ydata)
		plt.xlabel(list[0][0])
		plt.ylabel(list[0][column_index])
		return fig
	
def plot2Data(list, metadata, column1_name, column2_name):
	xdata = fill_list_with_string(list, 0)
		
	column1_index = get_index_from_column_name(metadata, column1_name)
	column2_index = get_index_from_column_name(metadata, column2_name)		
	
	ydata1 = fill_list_with_column_data(list, column1_index)
	ydata2 = fill_list_with_column_data(list, column2_index)
	
	if (ydata1 == None or ydata2 == None):
		return None
	else:
		bar_width = 0.35  # width of the bar
		screenSize = getScreenSize()
		fig = plt.figure(figsize = [screenSize[0]/100, screenSize[1]/100])
		ax = plt.subplot()
		rect1 = ax.bar(np.arange(len(xdata)) - bar_width/2, ydata1, bar_width, label = column1_name)
		rect2 = ax.bar(np.arange(len(xdata)) + bar_width/2, ydata2, bar_width, label = column2_name)
		ax.set_xlabel(list[0][0])
		ax.set_ylabel(column1_name + ", " + column2_name)
		ax.set_xticks(np.arange(len(xdata)))
		ax.set_xticklabels(xdata)
		ax.legend()
		#autolabel(rect1, ax)
		#autolabel(rect2, ax)
		return fig
	
def plot3Data(list, metadata, column1_name, column2_name, column3_name):
	xdata = fill_list_with_string(list, 0)
		
	column1_index = get_index_from_column_name(metadata, column1_name)
	column2_index = get_index_from_column_name(metadata, column2_name)		
	column3_index = get_index_from_column_name(metadata, column3_name)		
	
	ydata1 = fill_list_with_column_data(list, column1_index)
	ydata2 = fill_list_with_column_data(list, column2_index)
	ydata3 = fill_list_with_column_data(list, column3_index)
	
	if (ydata1 == None or ydata2 == None or ydata3 == None):
		return None
	else:
		bar_width = 0.25  # width of the bar
		screenSize = getScreenSize()
		fig = plt.figure(figsize = [screenSize[0]/100, screenSize[1]/100])
		ax = plt.subplot()
		rect1 = ax.bar(np.arange(len(xdata)) - bar_width, ydata1, bar_width, label = column1_name)
		rect2 = ax.bar(np.arange(len(xdata)), ydata2, bar_width, label = column2_name)
		rect3 = ax.bar(np.arange(len(xdata)) + bar_width, ydata3, bar_width, label = column3_name)
		ax.set_xlabel(list[0][0])
		ax.set_ylabel(column1_name + ", " + column2_name + ", " + column3_name)
		ax.set_xticks(np.arange(len(xdata)))
		ax.set_xticklabels(xdata)
		ax.legend()
		#autolabel(rect1, ax)
		#autolabel(rect2, ax)
		#autolabel(rect3, ax)
		return fig
	
def	create_destination_folder(folder_name):
	# create destination folder to save figures
	try:
		os.mkdir(DESTINATION_FOLDER+"/"+folder_name)
	except FileExistsError:
		print("Folder", DESTINATION_FOLDER+"/"+folder_name,"already exists")
		
def saveFigure(date, figure, count):
	if (figure != None and SAVING_CHARTS_ENABLED):
		figManager = plt.get_current_fig_manager()
		figManager.full_screen_toggle()
		figure.savefig(fname = DESTINATION_FOLDER+"/"+str(date)+"/"+str(date)+" - "+str(count)+".png", format = 'png')
		count += 1
	return count
	
def main():
	download(fileName = 'vaccini-summary-latest.csv', url = 'https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.csv')
	download(fileName = 'somministrazioni-vaccini-latest.csv', url = 'https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv')
	download(fileName = 'anagrafica-vaccini-summary-latest.csv', url = 'https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/anagrafica-vaccini-summary-latest.csv')
	
	# read vaccini-summary-latest.csv
	vaccini_summary_latest, metadata_vaccini_summary_latest = csvReader('vaccini-summary-latest.csv')	
	totalData = sumData(vaccini_summary_latest, metadata_vaccini_summary_latest, dataType = 'dosi_somministrate')
	print ('Total doses administered:', totalData)
	totalData = sumData(vaccini_summary_latest, metadata_vaccini_summary_latest, dataType = 'dosi_consegnate')
	print ('Total doses delivered:', totalData)
	
	create_destination_folder(folder_name = str(date.today()))
	count = 0
	
	for i in range (1, len(metadata_vaccini_summary_latest)):
		if (metadata_vaccini_summary_latest[i] != "codice_regione_ISTAT"):
			figure = plotData(vaccini_summary_latest, column_index = i)
			count = saveFigure(str(date.today()), figure, count)
			
	# read anagrafica-vaccini-summary-latest.csv
	anagrafica_vaccini, metadata_anagrafica_vaccini = csvReader('anagrafica-vaccini-summary-latest.csv')
	for i in range (1, len(metadata_anagrafica_vaccini)):
		figure = (plotData(anagrafica_vaccini, column_index = i))
		count = saveFigure(str(date.today()), figure, count)
			
	figure = plot2Data(anagrafica_vaccini, metadata_anagrafica_vaccini, column1_name = 'sesso_maschile', column2_name = 'sesso_femminile')
	count = saveFigure(str(date.today()), figure, count)
	figure = plot2Data(anagrafica_vaccini, metadata_anagrafica_vaccini, column1_name = 'prima_dose', column2_name = 'seconda_dose')
	count = saveFigure(str(date.today()), figure, count)
	
	figure = plot3Data(anagrafica_vaccini, metadata_anagrafica_vaccini, column1_name = 'categoria_operatori_sanitari_sociosanitari', column2_name = 'categoria_personale_non_sanitario', column3_name = 'categoria_ospiti_rsa')
	count = saveFigure(str(date.today()), figure, count)
	figure = plot3Data(anagrafica_vaccini, metadata_anagrafica_vaccini, column1_name = 'categoria_altro', column2_name = 'categoria_forze_armate', column3_name = 'categoria_personale_scolastico')
	count = saveFigure(str(date.today()), figure, count)
	
	if SAVING_CHARTS_ENABLED:
		print (count, "graphs saved in", DESTINATION_FOLDER+"/"+str(date.today()))
	if SHOW_CHARTS_ENABLED:
		plt.show()
	
if __name__ == "__main__":
    main()
