# COVID19 Vaccination Italy
This Python script shown and save some charts that explain how the COVID-19 vaccination in Italy is going. The datasets are available at [italia/covid19-opendata-vaccini](https://github.com/italia/covid19-opendata-vaccini).

# Prereqs
* [Python](https://www.python.org/) 
* [Matplotlib](https://pypi.org/project/matplotlib/)
* [Numpy](https://numpy.org/)
* [URLlib](https://docs.python.org/3/library/urllib.html)
* [CSV](https://docs.python.org/3/library/csv.html)
* [Ctypes](https://docs.python.org/3/library/ctypes.html)
* [Datetime](https://docs.python.org/3/library/datetime.html)
* [OS](https://docs.python.org/3/library/os.html)

# How to run 
1. Install matplotlib and numpy

Open a command window and type `python -m pip install -U matplotlib`, then type `pip install numpy`

2. Run

Open a command window and type `python main.py`. 
The charts are saved in "Charts" directory and in a folder named as the day the charts refer to.

# Charts

Here are shown some charts that this script created on 20/01/2021. If `SHOW_CHARTS_ENABLED = 1`, the charts are shown in the command windows. If `SAVING_CHARTS_ENABLED = 0`, the charts will not be saved.

Doses administered for each region
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-01-20/2021-01-20%20-%200.png)

Doses delivered for each region
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-01-20/2021-01-20%20-%201.png)

Percentage of administration for each region
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-01-20/2021-01-20%20-%202.png)

Total vaccinations by age group
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-01-20/2021-01-20%20-%203.png)

Total vaccinations by age group and gender
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-01-20/2021-01-20%20-%204.png)

Totale vaccinazioni per operatori socio sanitari, personale non sanitario, guests of esidential care homes
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-01-20/2021-01-20%20-%205.png)
