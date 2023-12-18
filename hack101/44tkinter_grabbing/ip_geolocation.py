import ipinfo
# import sys


token = "58b7dbcedb5cee"
handler = ipinfo.getHandlerAsync(token)

def ip_geolocation(ip):
  
  details = handler.getDetails(ip)
  