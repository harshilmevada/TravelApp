from datetime import datetime

import Api_distance
import Route
from geopy.distance import geodesic
from geopy.exc import GeocoderUnavailable
from geopy.geocoders import Nominatim

toDay = datetime.now().strftime("%d-%m-%Y")

# import distance_find
geolocator = Nominatim(user_agent="my_cli_project")

def getcordinect(fromInput):
    try:
        location = geolocator.geocode(fromInput)
        if location is not None:
            latitude = location.latitude
            longitude = location.longitude
            return (latitude, longitude)
        else:
            print(f"Location not found for input: {fromInput}")
            return (0, 0)  # Return default values
    except GeocoderUnavailable as e:
        print("Geocoding service is unavailable. Please try again later.")
        return (0, 0)  # Return default values


def seleteVehicle(distance):
    getList = Route.findRoot(distance)
    print("\n\nSelect Option\n")
    choice = int(input('selete vehicle : '))
    print(list(getList)[choice-1]['value'])

def getInfo(add):
    print(f"Find Location {add}")
    inp1 = input(f"Enter a Starting Point : ")
    inp2 = input(f"Enter a Ending Point : ")
    
    if not inp1:
        print("Please Enter Starting Location")
        return None
    elif not inp2:
        print("Please Enter Ending Location")
        return None
    elif inp1 and inp2:
        codi1 = getcordinect(inp1)
        codi2 = getcordinect(inp2)
        
        if codi1 == 0 or codi2 == 0:
            print("Invalid coordinates. Unable to calculate distance.")
            return None
        
        distance = geodesic(codi1, codi2).km
        print(f"{toDay}\n")
        print(f"distance {inp1} To {inp2} : {round(distance,2)} km")
        callList = Route.getListOf(distance)
        print(callList)
        vehicle = vehicleSelete(distance)
        return {'distance': round(distance,2),'startLoc': inp1,'endLoc': inp2, 'vehicle' : vehicle}


def vehicleSelete(distance):
    print("\n\nSelect Option\n")
    getList = Route.findRoot(distance)
    choice = int(input('selete vehicle : '))
    vehicle = list(getList)[choice-1]
    print(vehicle['value'])
    return vehicle


def BookTickit(getDistance):
    print("\n\nSelect Option\n")
    print('1.Book Tickit\n2.Renter Location\n3.Exit')
    choise = int(input("selete option : "))
    if(choise == 1):
        if getDistance is not None and getDistance.get('distance') != 0:
            getTickit(getDistance)
        else:
            print("distance is None or  0")
    elif(choise == 2):
        locationMain()
    else:
        return True


def getTickit(getDistance):
    if getDistance is not None and getDistance.get('distance') != 0:
        cost = getDistance['vehicle']['value']
        vehicle_type = getDistance['vehicle']['key']
        veh_type_dis = {
            1 : "Bike",
            2 : "Auto 🛺",
            3 : "Car for 4 People 🚕",
            4 : "Car for 7 People 🚗",
            5 : "Luxurious Car for 4 People 🚙",
            
        }
        vehicle_code = list(veh_type_dis.values())[vehicle_type-1]
        # Find the index of "₹" and "/-"
        start_index = cost.find("₹")
        end_index = cost.find("/-")

        # Extract the value between "₹" and "/-"
        value = cost[start_index :end_index+2]

        print(f"| ————————————————————————————————————————————————————— |")
        print(f"| {f'📅 To Date {toDay}'}")
        print(f'''
    | 🌏 Destination
    | 🏡 Starting Point : {getDistance['startLoc']}
    | 🏞️  Ending Point : {getDistance['endLoc']}
    | 🛣️  Total Distance in km : {getDistance['distance']}km
    | 🚕 Vehicle Type : {vehicle_code}
    | 💸 Total Cost : {value}''')
        print("Your Tickit 🎟️  is Booked Successfully 👍")
        print(f"| ————————————————————————————————————————————————————— |")
    else :
        print("Distance : 0 or None \nRun number 1,2,3" )


dis = {
    1 : "Ip Adderss",
    2 : "Offine",
    3 : "Online",
    4 : "Exit"
}

def locationMain():
    getDistance = {'distance' : 0}
    while True:
      print("\n\nSelect Option\n")
      for i in range(len(dis)-1):
          print(f"{list(dis.keys())[i]}. Find Location With {list(dis.values())[i]}")
      print("4. Exit\n")

      choise = int(input("Enter number (1,2,3,4) : "))

      add = list(dis.values())[choise-1]

      if choise == 1 or choise == 2:
          getDistance = getInfo(add)
          BookTickit(getDistance)
          return True
      elif choise == 3:
          print(f"Find Location {add}")
          start_location = input("Starting location : ")
          end_location = input("Ending location : ")
          code = int(input("Enter Password : "))
          if not start_location:
              print('Enter Starting loacation')
          elif not end_location:
              print('Enter Ending loacation')
          elif not code:
              print('Enter Number only')
          else:   
            getDistance = Api_distance.getApiDistance(start_location,end_location,code)
            if getDistance != 0 :
                print("Total distance ",getDistance)
                Route.getListOf(getDistance)
                vehicle = vehicleSelete(getDistance)
                vehicle
                apiDistance = {'distance': getDistance,'startLoc': start_location,'endLoc': end_location, 'vehicle' : vehicle}
                BookTickit(apiDistance)
            pass
      elif choise == 4:
          break
      else:
          print("enter valide number")
    return getDistance


    

if __name__ == "__main__":
    # getTickit()
    locationMain()
    # Test()

