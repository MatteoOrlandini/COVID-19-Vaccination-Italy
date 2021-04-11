import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import csv
import ctypes # to get screen size
from datetime import date # to get today as 'YYYY-MM-DD'
import os
import readme_autoupdate

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
		csv_reader = csv.reader(csv_file, delimiter = ',')
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
	for i in range (0, len (metadata)):
		if (metadata[i] == dataType):
			index = i
	for i in range (1, len (list)):
		total += int(list[i][index])
	return total

def getScreenSize():
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

def get_string_list(list, column_index):
	data = [list[1][column_index]] # initialize list
	for i in range (2, len (list)):	
		if list[i][column_index] not in data:
			data.append(list[i][column_index])
	return data
	
def get_data_list(list, column_index):
	data = [] # initialize list
	for i in range (1, len (list)):
		try:
			data.append(float(list[i][column_index]))
		except ValueError as e:
			#print(e)
			return None
	return data

def get_cumulative_data_italy(list, metadata):
	data = []
	day = list[1][get_index_from_column_name(metadata, "data_somministrazione")] # initialize day
	j = 0
	for i in range(1, len(list)):
		if (len(data) == 0):
				data = [float(list[i][get_index_from_column_name(metadata, "sesso_maschile")])\
				+ (float(list[i][get_index_from_column_name(metadata, "sesso_femminile")]))]
				first_date = list[i][get_index_from_column_name(metadata, "data_somministrazione")]
				last_date = first_date
		else:
			if (day == list[i][get_index_from_column_name(metadata, "data_somministrazione")]):
				data[len(data) - 1] += \
				+ float(list[i][get_index_from_column_name(metadata, "sesso_maschile")])\
				+ float(list[i][get_index_from_column_name(metadata, "sesso_femminile")])\
				
			else:
				data.append(data[len(data) - 1]\
				+ float(list[i][get_index_from_column_name(metadata, "sesso_maschile")])\
				+ float(list[i][get_index_from_column_name(metadata, "sesso_femminile")]))
				
				last_date = list[i][get_index_from_column_name(metadata, "data_somministrazione")]
				
				day = list[i][get_index_from_column_name(metadata, "data_somministrazione")] #update day
			
	return data, first_date, last_date
	
def	get_daily_data_italy(list, metadata):
	data = []
	day = list[1][get_index_from_column_name(metadata, "data_somministrazione")] # initialize day
	j = 0
	for i in range(1, len(list)):
		if (len(data) == 0):
				data = [float(list[i][get_index_from_column_name(metadata, "sesso_maschile")])\
				+ (float(list[i][get_index_from_column_name(metadata, "sesso_femminile")]))]
				first_date = list[i][get_index_from_column_name(metadata, "data_somministrazione")]
				last_date = first_date
		else:
			if (day == list[i][get_index_from_column_name(metadata, "data_somministrazione")]):
				data[len(data) - 1] += \
				+ float(list[i][get_index_from_column_name(metadata, "sesso_maschile")])\
				+ float(list[i][get_index_from_column_name(metadata, "sesso_femminile")])\
				
			else:
				data.append(float(list[i][get_index_from_column_name(metadata, "sesso_maschile")])\
				+ float(list[i][get_index_from_column_name(metadata, "sesso_femminile")]))
				
				last_date = list[i][get_index_from_column_name(metadata, "data_somministrazione")]
				
				day = list[i][get_index_from_column_name(metadata, "data_somministrazione")] #update day
			
	return data, first_date, last_date
	
def	get_cumulative_data_italy_by_age_group(list, metadata, fascia_anagrafica):
	data = []
	day = list[1][get_index_from_column_name(metadata, "data_somministrazione")] # initialize day
	j = 0
	for i in range(1, len(list)):
		if(list[i][get_index_from_column_name(metadata, "fascia_anagrafica")]\
		== fascia_anagrafica):
			if (len(data) == 0):
					data = [float(list[i][get_index_from_column_name(metadata, "sesso_maschile")])\
					+ (float(list[i][get_index_from_column_name(metadata, "sesso_femminile")]))]
					first_date = list[i][get_index_from_column_name(metadata, "data_somministrazione")]
					last_date = first_date
			else:
				if (day == list[i][get_index_from_column_name(metadata, "data_somministrazione")]):
					data[len(data) - 1] += \
					+ float(list[i][get_index_from_column_name(metadata, "sesso_maschile")])\
					+ float(list[i][get_index_from_column_name(metadata, "sesso_femminile")])\
					
				else:
					data.append(data[len(data) - 1]\
					+ float(list[i][get_index_from_column_name(metadata, "sesso_maschile")])\
					+ float(list[i][get_index_from_column_name(metadata, "sesso_femminile")]))
					
					last_date = list[i][get_index_from_column_name(metadata, "data_somministrazione")]
					
					day = list[i][get_index_from_column_name(metadata, "data_somministrazione")] #update day
			
	return data, first_date, last_date

def get_cumulative_data_per_area_by_category(list, metadata_list, data_somministrazione, fascia_anagrafica, fornitore, categoria):
	data = []
	j = 0
	for i in range (0, len(list)):
		if (fascia_anagrafica == list[i][get_index_from_column_name(metadata = metadata_list, column_name = "fascia_anagrafica")] \
		and area == list[i][get_index_from_column_name(metadata = metadata_list, column_name = "area")] \
		and fornitore == list[i][get_index_from_column_name(metadata = metadata_list, column_name = "fornitore")]):
			if (len(data) == 0):
				first_date = list[i][get_index_from_column_name(metadata = metadata_list, column_name = "data_somministrazione")]
				last_date = first_date
				data.append(float(list[i][get_index_from_column_name(metadata = metadata_list, column_name = categoria)]))

			else:
				data.append(data[len(data) - 1] + float(list[i][get_index_from_column_name(metadata = metadata_list, column_name = categoria)]))
				last_date = list[i][get_index_from_column_name(metadata = metadata_list, column_name = "data_somministrazione")]
			
			while (data_somministrazione[j] != list[i][get_index_from_column_name(metadata = metadata_list, column_name = "data_somministrazione")]):
				if (len(data) != 0):
					data.append(data[len(data) - 1])
				j += 1			
					
	return data, first_date, last_date
	

def get_cumulative_data_italy_by_category(list, metadata_list, data_somministrazione, fascia_anagrafica, fornitore, categoria):
	data = []
	j = 0
	for i in range (0, len(list)):
		if (fascia_anagrafica == list[i][get_index_from_column_name(metadata = metadata_list, column_name = "fascia_anagrafica")] \
		and fornitore == list[i][get_index_from_column_name(metadata = metadata_list, column_name = "fornitore")]):
			if (data_somministrazione[j] == list[i][get_index_from_column_name(metadata = metadata_list, column_name = "data_somministrazione")]):			
				if (len(data) == 0):
					first_date = list[i][get_index_from_column_name(metadata = metadata_list, column_name = "data_somministrazione")]
					last_date = first_date
					data.append(float(list[i][get_index_from_column_name(metadata = metadata_list, column_name = categoria)]))

				else:
					data.append(data[len(data) - 1] + float(list[i][get_index_from_column_name(metadata = metadata_list, column_name = categoria)]))
					last_date = list[i][get_index_from_column_name(metadata = metadata_list, column_name = "data_somministrazione")]
			
			while (data_somministrazione[j] != list[i][get_index_from_column_name(metadata = metadata_list, column_name = "data_somministrazione")]):
				if (len(data) != 0):
					data.append(data[len(data) - 1])
				j += 1			
					
	return data, first_date, last_date
	
def get_index_from_column_name(metadata, column_name):
	for i in range (0, len(metadata)):
		if (metadata[i] == column_name):
			return i

def plotBar1Data(xlabel, ylabel, xdata, ydata):
	if (ydata == None):
		return None
	else:
		# get screen size to plot graphs full screen
		screenSize = getScreenSize()
		fig = plt.figure(figsize = [screenSize[0]/100, screenSize[1]/100])
		plt.bar(xdata, ydata)
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		return fig
	
def plotBar2Data(xlabel, ylabel1, ylabel2, xdata, ydata1, ydata2):
	if (ydata1 == None or ydata2 == None):
		return None
	else:
		bar_width = 0.35  # width of the bar
		screenSize = getScreenSize()
		fig = plt.figure(figsize = [screenSize[0]/100, screenSize[1]/100])
		ax = plt.subplot()
		rect1 = ax.bar(np.arange(len(xdata)) - bar_width/2, ydata1, bar_width, label = ylabel1)
		rect2 = ax.bar(np.arange(len(xdata)) + bar_width/2, ydata2, bar_width, label = ylabel2)
		ax.set_xlabel(xlabel)
		ax.set_ylabel(ylabel1 + ", " + ylabel2)
		ax.set_xticks(np.arange(len(xdata)))
		ax.set_xticklabels(xdata)
		ax.legend()
		#autolabel(rect1, ax)
		#autolabel(rect2, ax)
		return fig
	
def plotBar3Data(xlabel, ylabel1, ylabel2, ylabel3, xdata, ydata1, ydata2, ydata3):
	if (ydata1 == None or ydata2 == None or ydata3 == None):
		return None
	else:
		bar_width = 0.25  # width of the bar
		screenSize = getScreenSize()
		fig = plt.figure(figsize = [screenSize[0]/100, screenSize[1]/100])
		ax = plt.subplot()
		rect1 = ax.bar(np.arange(len(xdata)) - bar_width, ydata1, bar_width, label = ylabel1)
		rect2 = ax.bar(np.arange(len(xdata)), ydata2, bar_width, label = ylabel2)
		rect3 = ax.bar(np.arange(len(xdata)) + bar_width, ydata3, bar_width, label = ylabel3)
		ax.set_xlabel(xlabel)
		ax.set_ylabel(ylabel1 + ", " + ylabel2 + ", " + ylabel3)
		ax.set_xticks(np.arange(len(xdata)))
		ax.set_xticklabels(xdata)
		ax.legend()
		#autolabel(rect1, ax)
		#autolabel(rect2, ax)
		#autolabel(rect3, ax)
		return fig
		
def plotLine1Data(data, xlimits, xlabel, ylabel):
	screenSize = getScreenSize()
	fig = plt.figure(figsize = [screenSize[0]/100, screenSize[1]/100])
	plt.plot(data)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.xticks([0, len(data)], xlimits)
	plt.text(x = len(data) - 5, y = data[len(data) - 1] + 0.015*data[len(data) - 1], s = str(int(data[len(data) - 1])))
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
	plt.close(figure)
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
			xdata = get_string_list(vaccini_summary_latest, get_index_from_column_name(metadata_vaccini_summary_latest, "area"))
			ydata = get_data_list(vaccini_summary_latest, i)
			figure = plotBar1Data('area', metadata_vaccini_summary_latest[i], xdata, ydata)
			count = saveFigure(str(date.today()), figure, count)
			
	# read anagrafica-vaccini-summary-latest.csv
	anagrafica_vaccini, metadata_anagrafica_vaccini = csvReader('anagrafica-vaccini-summary-latest.csv')
	for i in range (1, len(metadata_anagrafica_vaccini)):
		xdata = get_string_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, "fascia_anagrafica"))
		ydata = get_data_list(anagrafica_vaccini, i)
		figure = (plotBar1Data('fascia_anagrafica', metadata_anagrafica_vaccini[i], xdata, ydata))
		count = saveFigure(str(date.today()), figure, count)
			
	
	xdata = get_string_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'fascia_anagrafica'))	
	ydata1 = get_data_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'sesso_maschile'))
	ydata2 = get_data_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'sesso_femminile'))
	figure = plotBar2Data('fascia_anagrafica', 'sesso_maschile', 'sesso_femminile', xdata, ydata1, ydata2)
	count = saveFigure(str(date.today()), figure, count)
	
	xdata = get_string_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'fascia_anagrafica'))	
	ydata1 = get_data_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'prima_dose'))
	ydata2 = get_data_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'seconda_dose'))
	figure = plotBar2Data('fascia_anagrafica', 'prima_dose', 'seconda_dose', xdata, ydata1, ydata2)
	count = saveFigure(str(date.today()), figure, count)
	
	xdata = get_string_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'fascia_anagrafica'))	
	ydata1 = get_data_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'categoria_operatori_sanitari_sociosanitari'))
	ydata2 = get_data_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'categoria_personale_non_sanitario'))
	ydata3 = get_data_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'categoria_ospiti_rsa'))
	figure = plotBar3Data('fascia_anagrafica', 'categoria_operatori_sanitari_sociosanitari', 'categoria_personale_non_sanitario', 'categoria_ospiti_rsa', xdata, ydata1, ydata2, ydata3)
	count = saveFigure(str(date.today()), figure, count)
	
	xdata = get_string_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'fascia_anagrafica'))	
	ydata1 = get_data_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'categoria_altro'))
	ydata2 = get_data_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'categoria_forze_armate'))
	ydata3 = get_data_list(anagrafica_vaccini, get_index_from_column_name(metadata_anagrafica_vaccini, 'categoria_personale_scolastico'))
	figure = plotBar3Data('fascia_anagrafica', 'categoria_altro', 'categoria_forze_armate', 'categoria_personale_scolastico', xdata, ydata1, ydata2, ydata3)
	count = saveFigure(str(date.today()), figure, count)
	
	# read somministrazioni-vaccini-latest.csv
	somministrazioni_vaccini, metadata_somministrazioni_vaccini = csvReader('somministrazioni-vaccini-latest.csv')
	
	data_somministrazione = get_string_list(somministrazioni_vaccini, get_index_from_column_name(metadata = metadata_somministrazioni_vaccini, column_name = "data_somministrazione"))
	fornitore = get_string_list(somministrazioni_vaccini, get_index_from_column_name(metadata = metadata_somministrazioni_vaccini, column_name = "fornitore"))
	area = get_string_list(somministrazioni_vaccini, get_index_from_column_name(metadata = metadata_somministrazioni_vaccini, column_name = "area"))
	fascia_anagrafica = get_string_list(somministrazioni_vaccini, get_index_from_column_name(metadata = metadata_somministrazioni_vaccini, column_name = "fascia_anagrafica"))

	cumulative_data_italy, first_date, last_date = get_cumulative_data_italy(somministrazioni_vaccini, metadata_somministrazioni_vaccini)
	if (cumulative_data_italy[len(cumulative_data_italy)-1] != 0):
		figure = plotLine1Data(data = cumulative_data_italy, xlimits = [first_date, last_date], xlabel = 'Days', ylabel = "Totale dosi somministrate")
		count = saveFigure(str(date.today()), figure, count)
		
	daily_data_italy, first_date, last_date = get_daily_data_italy(somministrazioni_vaccini, metadata_somministrazioni_vaccini)
	if (daily_data_italy[len(daily_data_italy)-1] != 0):
		figure = plotLine1Data(data = daily_data_italy, xlimits = [first_date, last_date], xlabel = 'Days', ylabel = "Dosi somministrate quotidianamente")
		count = saveFigure(str(date.today()), figure, count)
	
	for i in range (0, len(fascia_anagrafica)):
		cumulative_data_italy_by_age_group, first_date, last_date = get_cumulative_data_italy_by_age_group(somministrazioni_vaccini, metadata_somministrazioni_vaccini, fascia_anagrafica[i])
		if (cumulative_data_italy_by_age_group[len(cumulative_data_italy_by_age_group)-1] != 0):
			figure = plotLine1Data(data = cumulative_data_italy_by_age_group, xlimits = [first_date, last_date], xlabel = 'Days', ylabel = "Fascia anagrafica " + fascia_anagrafica[i])
			count = saveFigure(str(date.today()), figure, count)
			
	# for i in range (0, len(fascia_anagrafica)):
		# for j in range (0, len(area)):
			# for k in range (0, len(fornitore)):
				# for l in range(1, len(metadata_somministrazioni_vaccini)):
					# if (metadata_somministrazioni_vaccini[l] != "data_somministrazione" \
					# and metadata_somministrazioni_vaccini[l] != "fornitore"\
					# and metadata_somministrazioni_vaccini[l] != "area"\
					# and metadata_somministrazioni_vaccini[l] != "codice_NUTS1"\
					# and metadata_somministrazioni_vaccini[l] != "codice_NUTS2"\
					# and metadata_somministrazioni_vaccini[l] != "codice_regione_ISTAT"\
					# and metadata_somministrazioni_vaccini[l] != "nome_area"):
						# cumulative_data_per_area_by_category, first_date, last_date = get_cumulative_data_per_area_by_category(somministrazioni_vaccini, metadata_somministrazioni_vaccini, data_somministrazione, fascia_anagrafica[i], area[j], fornitore[k], metadata_somministrazioni_vaccini[l])
						# if (cumulative_data_per_area_by_category[len(cumulative_data_per_area_by_category)-1] != 0):
							# figure = plotLine1Data(data = cumulative_data_per_area_by_category, xlimits = [first_date, last_date], xlabel = 'Days', ylabel = fornitore[k] + " " + area[j] + " " + metadata_somministrazioni_vaccini[l] + " fascia anagrafica " + fascia_anagrafica[i])
							# count = saveFigure(str(date.today()), figure, count)
					
	# for i in range (0, len(fascia_anagrafica)):
		# for k in range (0, len(fornitore)):
			# for l in range(1, len(metadata_somministrazioni_vaccini)):
				# if (metadata_somministrazioni_vaccini[l] != "data_somministrazione" \
				# and metadata_somministrazioni_vaccini[l] != "fornitore"\
				# and metadata_somministrazioni_vaccini[l] != "area"\
				# and metadata_somministrazioni_vaccini[l] != "fascia_anagrafica"\
				# and metadata_somministrazioni_vaccini[l] != "codice_NUTS1"\
				# and metadata_somministrazioni_vaccini[l] != "codice_NUTS2"\
				# and metadata_somministrazioni_vaccini[l] != "codice_regione_ISTAT"\
				# and metadata_somministrazioni_vaccini[l] != "nome_area"):
					# cumulative_data_italy_by_category, first_date, last_date = get_cumulative_data_italy_by_category(somministrazioni_vaccini, metadata_somministrazioni_vaccini, data_somministrazione, fascia_anagrafica[i], fornitore[k], metadata_somministrazioni_vaccini[l])
					# if (cumulative_data_italy_by_category[len(cumulative_data_italy_by_category)-1] != 0):
						# figure = plotLine1Data(data = cumulative_data_italy_by_category, xlimits = [first_date, last_date], xlabel = 'Days', ylabel = fornitore[k] + " Italy " + metadata_somministrazioni_vaccini[l] + " fascia anagrafica " + fascia_anagrafica[i])
						# count = saveFigure(str(date.today()), figure, count)
		
	if SAVING_CHARTS_ENABLED:
		print (count, "graphs saved in", DESTINATION_FOLDER+"/"+str(date.today()))
	if SHOW_CHARTS_ENABLED:
		plt.show()
		
	if (readme_autoupdate.create_readme() == True):
		print("README.md updated")
	
if __name__ == "__main__":
    main()
