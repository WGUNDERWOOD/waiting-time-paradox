import sys
sys.path.append(".")

import numpy as np
from plotnine import ggplot, aes, geom_histogram
import waiting_source as w


n_trials = 10000
start_time = 240
average_interval = 10

waiting_time_info_table = w.get_waiting_time_info_table(average_interval, start_time, n_trials)
print(np.mean(waiting_time_info_table["waiting_time"]))

pl = ggplot(
  waiting_time_info_table,
  aes(x = "waiting_time")
)
pl = pl + geom_histogram(binwidth = 1)
pl.save("plot1.png", verbose = False)

pl = ggplot(
  waiting_time_info_table,
  aes(x = "proportion_elapsed")
)
pl = pl + geom_histogram(binwidth = 0.1)
pl.save("plot2.png", verbose = False)

pl = ggplot(
  waiting_time_info_table,
  aes(x = "observed_interval")
)
pl = pl + geom_histogram(binwidth = 0.1)
pl.save("plot3.png", verbose = False)
