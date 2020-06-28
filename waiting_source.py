import numpy as np
from numpy import random as rd
import pandas as pd


def get_waiting_time_info(average_interval, start_time):

  arrival_time = 0
  old_arrival_time = 0

  while arrival_time - start_time < 0:

    interval = rd.exponential(scale = average_interval)
    old_arrival_time = arrival_time
    arrival_time += interval

    waiting_time = arrival_time - start_time
    elapsed_time = start_time - old_arrival_time
    observed_interval = arrival_time - old_arrival_time
    proportion_elapsed = elapsed_time / observed_interval

  waiting_time_info = [
    elapsed_time,
    waiting_time,
    observed_interval,
    proportion_elapsed
  ]

  return waiting_time_info


def get_waiting_time_info_table(average_interval, start_time, n_trials):

  waiting_time_info_list = []

  for i in range(n_trials):

    waiting_time_info = get_waiting_time_info(average_interval, start_time)
    waiting_time_info_list.append(waiting_time_info)

  colnames = [
    "waiting_time",
    "elapsed_time",
    "observed_interval",
    "proportion_elapsed"
  ]

  waiting_time_info_table = pd.DataFrame(
    waiting_time_info_list,
    columns = colnames
  )

  return waiting_time_info_table
