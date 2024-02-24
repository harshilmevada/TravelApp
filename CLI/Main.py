import itertools
import json
import random
import time

import location_code

dis = {1:" /",2:" —",3:" \\",4:" |"}
# dis = {1:".",2:"..",3:"...",4:"   "}

cycled_dis = itertools.cycle(dis.values())

def funcationBack():
      for _ in range(15):
            time.sleep(random.uniform(0.04,0.3))
            print(f"Loading{next(cycled_dis)}",end='\r')
      read() # Call this funcation


def read():
      # Open the JSON file
      with open('data.json', 'r') as file:
          data = json.load(file)

      # Now 'data' contains the parsed JSON content
      for place in data["tourist_places"]:
            for key in range(len(place.items())-1):
                  print(f"{list(place.keys())[key]} : {list(place.values())[key]}")
            print()

distanc = 0



if __name__ == "__main__":
      while True:
            print("1. Find distance")
            print("2. Get best tourist place")
            print("3. Exit\n")
            choice = int(input("Please enter 1,2or 3 : "))

            if choice == 1:
                  distanc = location_code.locationMain()
            elif choice == 2:
                  funcationBack()
            elif choice == 3:
                  print(f"get distance from option 1 : {round(distanc,2)}")
                  break
