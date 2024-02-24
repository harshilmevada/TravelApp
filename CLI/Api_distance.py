import itertools
from datetime import datetime

import database
import requests
from dist_data import error


def isSameDate():
    data = database.getData()
    prevMonth = data['date']
    curMonth = datetime.now().date().strftime("%m-%Y")
    if(prevMonth != curMonth):
        print("Month is not same")
        plusApiCall(curMonth)
    else:
        print("Month is same")
        plusApiCall(curMonth)
    # formater = f"{current_month}/{current_year}"
    print(f'cur {curMonth} pre {prevMonth}')

def ErrorCode(code):
      if code in error:
          print(f"Error : {error[code]}")
          return True
      

def plusApiCall():
    # Max Api Call in one month is 15000
    data = database.getData()
    prevMonth = data['date']
    curMonth = datetime.now().date().strftime("%m-%Y")

    if(prevMonth != curMonth):
        print("New month Call")
        apiCall = database.getData()['apiCall']
        apiCall = 0
        database.updateData(apiCall,curMonth)
        apiCall += 1
        database.updateData(apiCall,curMonth)
        print(f"New Api Call Use {apiCall} Time")
    else:
        apiCall =  database.getData()['apiCall']
        apiCall += 1
        database.updateData(apiCall,curMonth)
        print(f"New Api Call Use {apiCall} Time")

      


    

def getApiDistance(start_location,end_location,password):
    dis = {1:" /",2:" —",3:" \\",4:" |"}
    # dis = {1:".",2:"..",3:"...",4:"   "}

    cycled_dis = itertools.cycle(dis.values())
    try:
    #   The APIKEY from MapQuest.
      code = 3824
      if password == code:
          api_key = 'oygMCCjWja8kH2vCwKYCp49qm9r49Qow'
      else:
          api_key = 'oygMCCjWja8kH2vCwKYCq49qm9r49Qow'

      print(f"Last Api Call Use {database.getData()} Time")
      # Define the URL for the MapQuest Directions API.
      base_url = 'http://www.mapquestapi.com/directions/v2/route'

      # Specify the locations you want to calculate the distance between.
      #   start_location = 'Vejalapur, Ahmedabad, Gujarat'
      #   end_location = 'Mumbai Central, Mumbai, Maharashtra'

      # Make a GET request to the API with the specified parameters.
      params = {
          'key': api_key,
          'from': start_location,
          'to': end_location,
          'unit': 'k'  # 'k' for kilometers
      }

      print(f"Loading{next(cycled_dis)}",end='\r')
      response = requests.get(base_url, params=params)
      if response.status_code == 200:
          data = response.json()
          if data['info']['statuscode'] == 0:
              # Extract the distance in kilometers from the response.
              distance = data['route']['distance']
              maneuvers = data['route']['legs'][0]['maneuvers']
              streets = [maneuver['streets'][0] if maneuver['streets'] else 'N/A' for maneuver in maneuvers]
              print(f'Distance between {start_location} To {end_location} : {distance:.2f} kilometers')
              for i in streets:
                  print(f"{i}")
              plusApiCall()
              return round(distance,2)
          else:
              return 0
      else:
          ErrorCode(response.status_code)
    except requests.ConnectionError:
     print("ConnectionError")
    return 0

# if __name__ == "__main__":
    # plusApiCall()
    # ErrorCode(400)

