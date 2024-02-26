from datetime import datetime


def current_time_as_integer():
    current_time = datetime.now().time()
    time_as_integer = current_time.hour * 100 + current_time.minute

    return time_as_integer

cur_time = current_time_as_integer()


def buzyTime():
      # 7:30 to 10:30(am)
      if 730 <= cur_time <= 1030:
            return 33
      # 10:31 to 4:30(am:pm)
      elif 1031 <= cur_time <= 1630:
           return -3
      # 4:31 to 6:00(pm)
      elif 1631 <= cur_time <= 1800:
           return 11
      # 6:01 to 9:00(pm)
      elif 1801 <= cur_time <= 2100:
           return 33
      # 9:01 to 7:29(pm:am)
      else:
           return -33

# print(buzyTime())