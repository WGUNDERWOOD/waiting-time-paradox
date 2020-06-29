import sys
sys.path.append(".")

import numpy as np
from numpy import random as rd
#from plotnine import ggplot, aes, geom_histogram
import waiting_source as w


n_trials = 10000
start_time = 240
average_interval = 10

waiting_time_info_table = w.get_waiting_time_info_table(average_interval, start_time, n_trials)
print("number of trials")
print(n_trials)

print()

print("average waiting time")
print(np.mean(waiting_time_info_table["waiting_time"]))
print("standard error of average waiting time")
print(np.std(waiting_time_info_table["waiting_time"]) / np.sqrt(n_trials))

print()

print("average difference of elapsed - waiting")
print(np.mean(waiting_time_info_table["difference_elapsed_waiting"]))
print("standard error of average difference of elapsed - waiting")
print(np.std(waiting_time_info_table["difference_elapsed_waiting"]) / np.sqrt(n_trials))

print()

print("average interval")
print(np.mean(rd.exponential(scale = average_interval, size = n_trials)))
print("standard error of average interval")
print(np.std(rd.exponential(scale = average_interval, size = n_trials)) / np.sqrt(n_trials))


#pl = ggplot(
  #waiting_time_info_table,
  #aes(x = "waiting_time")
#)
#pl = pl + geom_histogram(binwidth = 1)
#pl.save("plot1.png", verbose = False)

#pl = ggplot(
  #waiting_time_info_table,
  #aes(x = "proportion_elapsed")
#)
#pl = pl + geom_histogram(binwidth = 0.1)
#pl.save("plot2.png", verbose = False)

#pl = ggplot(
  #waiting_time_info_table,
  #aes(x = "observed_interval")
#)
#pl = pl + geom_histogram(binwidth = 0.1)
#pl.save("plot3.png", verbose = False)
