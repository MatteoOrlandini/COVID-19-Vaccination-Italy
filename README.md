# COVID19 Vaccination Italy
This Python script shows and saves some charts that explain how the COVID-19 vaccination in Italy is going. The datasets are available at [italia/covid19-opendata-vaccini](https://github.com/italia/covid19-opendata-vaccini).

# Prereqs
* [Python](https://www.python.org/) 
* [Matplotlib](https://pypi.org/project/matplotlib/)
* [Numpy](https://numpy.org/)
* [URLlib](https://docs.python.org/3/library/urllib.html)
* [CSV](https://docs.python.org/3/library/csv.html)
* [Ctypes](https://docs.python.org/3/library/ctypes.html)
* [Math](https://docs.python.org/3/library/math.html)
* [OS](https://docs.python.org/3/library/os.html)
* [Tweepy](https://docs.tweepy.org/en/latest/)

# How to run 
1. Install matplotlib and numpy

Open a command window and type `python -m pip install -U matplotlib`, then type `pip install numpy`

2. Run

Open a command window and type `python main.py`. 
The charts are saved in [Charts](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/tree/main/Charts) directory and in a folder named as the day the charts refer to.

# Charts
If `SHOW_CHARTS_ENABLED = 1`, the charts are shown in the command window. If `SAVING_CHARTS_ENABLED = 0`, the charts will not be saved.

Here are shown some charts that this script created on 2021-04-17.

Administered doses for each region
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%200.png)

Delivered doses for each region
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%201.png)

Percentage of administration for each region
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%202.png)

Total vaccinations by age group
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%203.png)

Total vaccinations by age group and male gender
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%204.png)

Total vaccinations by age group and female gender
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%205.png)

Total vaccinations for social health workers
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%206.png)

Total vaccinations for social non-health personnel
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%207.png)

Total vaccinations for other people
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%208.png)

Total vaccinations for guests of residential care homes
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%209.png)

Total vaccinations for over 80 years old
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2010.png)

Total vaccinations for armed forces
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2011.png)

Total vaccinations for school personnel
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2012.png)

Total first dose vaccinations
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2013.png)

Total second dose vaccinations
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2014.png)

Comparison between male and female vaccinations
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2015.png)

Comparison between first and second doses
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2016.png)

Total vaccinations for social health workers, non-health personnel and guests of residential care homes
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2017.png)

Total vaccinations for other people, armed forces and school personnel
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2018.png)

Total administered doses over time
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2019.png)

Daily administered doses over time
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2020.png)

Total administered doses for 20-29 years old age group over time
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2021.png)

Total administered doses for 30-39 years old age group over time
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2022.png)

Total administered doses for 40-49 years old age group over time
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2023.png)

Total administered doses for 50-59 years old age group over time
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2024.png)

Total administered doses for 60-69 years old age group over time
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2025.png)

Total administered doses for 70-79 years old age group over time
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2026.png)

Total administered doses for 80-89 years old age group over time
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2027.png)

Total administered doses for 90+ years old age group over time
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2028.png)

Total administered doses for 16-19 years old age group over time
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2029.png)

Total Pfizer/BioNTech administered doses
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2030.png)

Total Moderna administered doses
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2031.png)

Total Vaxzevria (AstraZeneca) administered doses
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2032.png)

Comparison between first and second administered doses over time
![](https://github.com/MatteoOrlandini/COVID-19-Vaccination-Italy/blob/main/Charts/2021-04-17/2021-04-17%20-%2033.png)

