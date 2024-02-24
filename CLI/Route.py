import buzy_time

timeCost = buzy_time.buzyTime()


def findRoot(distance):
      if(distance != 0):
            finalCost = 15 + distance
            dis = {
            1 : f"Go to distnation with Bike = ₹{round((finalCost * 3)+timeCost,2)}/-",
            2 : f"Go to distnation with Auto = ₹{round((finalCost * 4)+timeCost,2)}/-",
            3 : f"Go to distnation with Car 4 People = ₹{round((finalCost * 5.5)+timeCost,2)}/-",
            4 : f"Go to distnation with Car 7 People = ₹{round((finalCost * 6)+timeCost,2)}/-",
            5 : f"Go to distnation with Luxurious Car 4 People = ₹{round((finalCost * 9)+timeCost,2)}/-"
            }

            result = []
            for key, value in dis.items():
                  result.append({'key': key, 'value': value})

            return result
      return 0

def getListOf(distance):
      for item in findRoot(distance):
            print(item['key'],item['value'])

def bestRout(distanc):
      while True:
            print(f"distanc is {distanc}")
            print("Give your draiving rout")
            print("1. Whith car :")
            print("2. Whith auto :")
            print("3. Whith Two wheeler :")
            print("4. Exit\n")

            choice = int(input("Please enter 1,2,3 or 4: "))

            if choice == 1:
                  if distanc <= 10:
                        print(distanc + 2)
                  elif distanc <= 50:
                        print(distanc + 5)
                  elif distanc <=100:
                        print(distanc + 10)
                  elif distanc >= 100:
                        cal = distanc + 50
                        print(cal)

            elif choice == 4:
                  break

if __name__ == "__main__":
      print(list(findRoot(23))[1]['value'])
      # getListOf()



