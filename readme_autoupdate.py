# update readme

from datetime import date # to get today as 'YYYY-MM-DD'

def read_base_readme(file_name):
	file = open(file_name, "r")
	base_readme = file.read()
	file.close
	return base_readme
	
def get_charts_name(file_name):
	file = open(file_name, "r")
	charts_name = []
	for line in file:
		charts_name.append(line.rstrip("\n"))
	file.close() 
	return charts_name
	
def readme_update(file_name, base_readme, charts_name):
	file = open(file_name, "w")
	file.write(base_readme)
	for i in range (0, len(charts_name)):
		file.write(charts_name[i]+"\n")
		file.write("![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/"+str(date.today())+"/"+str(date.today())+"%20-%20"+str(i)+".png)\n\n")
	file.close
	
def create_readme():
	base_readme = read_base_readme("base_readme.md")
	charts_name = get_charts_name("charts_name.txt")
	readme_update("README.md", base_readme+str(date.today())+".\n\n", charts_name)
	return True