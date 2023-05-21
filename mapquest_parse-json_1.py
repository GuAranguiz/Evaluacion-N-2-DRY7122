import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "WbcpoMthWSr8p62zAt6E0TKAo46I8g7b"

while True:
   orig = input("Ubicacion inicial: ")
   if orig == "quit" or orig == "q":
        break
   dest = input("Destino: ")
   if dest == "quit" or dest == "q":
        break

   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       print("=============================================")
       print("Direccion desde " + (orig) + " Hacia " + (dest))
       print("Duracion de viaje:   " + (json_data["route"]["formattedTime"]))
       print("Kilometros      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
       print("=============================================")

       for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================")