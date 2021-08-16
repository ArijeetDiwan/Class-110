import statistics
import pandas as pd 
import csv 
import plotly.figure_factory as ff
import random 
df=pd.read_csv("./newdata.csv")
data=df["temp"].tolist()
print("population mean ",statistics.mean(data))
print("population standard deviation  ",statistics.stdev(data))
#fig=ff.create_distplot([data],["temp"],show_hist=False)
#fig.show()
#output:
#population mean  3.933977711872023
#population standard deviation   0.350970118315556
#there are data which do not follow normal distribution 

#let us take 100 data points {from the population data }

def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)


    mean=statistics.mean(dataset)
    return mean
    
def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["temp"],show_hist=False)

def setup():
     mean_list=[]
     for i in range (0,1000):
         setofmeans=randomsetofmean(100)
         mean_list.append(setofmeans)
     show_fig(mean_list)
     print("sampling mean",statistics.mean(mean_list))
     print("sampling standard deviation ",statistics.stdev(mean_list))
    

setup()


         