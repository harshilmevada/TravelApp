from datetime import datetime


def current_time_as_integer():
    current_time = datetime.now().time()
    time_as_integer = current_time.hour * 100 + current_time.minute

    return time_as_integer

cur_time = current_time_as_integer()


def buzyTime():
      # 7:30 to 10:30
      if 730 <= cur_time <= 1030:
            return 33
      elif 1031 <= cur_time <= 1630:
           return -3
      elif 1631 <= cur_time <= 1800:
           return 11
      elif 1801 <= cur_time <= 2100:
           return 33
      else:
           return -33

# print(buzyTime())