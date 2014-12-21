__author__ = 'Joan'
import MySQLdb
import yate
from geopy.geocoders import Nominatim
from mako.template import Template
import sys
import time
geolocator = Nominatim()

class Geocode :

    def get_direction(self,cod,typo=None):

        db = MySQLdb.connect(host= 'localhost',
                     user="matter_app",
                      passwd="m@tt3r",
                      db="matter")
        cur = db.cursor()
        if  typo == 'Warehouse' :
            cur.execute('select Location from  Warehouse where Cod  ="%s"' %(cod))
        elif  typo == None :
            cur.execute('select Direccion from  Client where Nombre  ="%s"' %(cod))
        result = cur.fetchall()
        r =[]
        for a in result :
            r.append(a[0])
        return r

    def get_coordinates(self , cod ,typo = None):
        location = geolocator.geocode(self.get_direction(cod , typo))
        return location.latitude , location.longitude





db = MySQLdb.connect(host= 'localhost',
                     user="matter_app",
                      passwd="m@tt3r",
                      db="matter")
cur = db.cursor()
gc = Geocode()
def get_Warehouse():
    cur.execute('Select Cod from Warehouse')
    result = cur.fetchall()
    Warehouses = {}
    for a in result :
       Warehouses[a[0]]=gc.get_coordinates(a[0],'Warehouse')
    return Warehouses
def get_Clients():
    cur.execute('Select Nombre from Client')
    Clients = {}
    resul = cur.fetchall()
    for a in resul:
        Clients[a[0]] = gc.get_coordinates(a[0],typo=None)
    return Clients




def get_trip():
    cur.execute('Select * ,TripLocation.SequenseOrder FROM Trip left join TripLocation on Trip.Id = TripLocation.Id')
    result  = cur.fetchall()
    na =[]
    for a in result:
        na.append(a[1])
        na.append(a[2])
        na.append(a[3])
        na.append(a[8])
        na.append(a[9])
        na.append(a[11])

    return na


flight=["132131351","46468156","46515135","16654646"]
"""for i in flight :
    sys.stdout.write("\r" +"|coordinates| : "+"|"+i+"|")
    sys.stdout.flush()
    time.sleep(1)"""


class trip :
    def __init__(self,descrption,time,speed,latitude,longitude,sequense):
        self.description = descrption
        self.time = time
        self.speed = speed
        self.letitude = latitude
        self.longitude = longitude
        self.sequense = sequense
    def calculateTime(self):
        distance = 200
        time = distance/self.speed
        return time
    def DisplayContent (self):

        print("\r" +"|Description| : "+"|"+self.description)

        print("\r" +"|speed| : " +str(self.speed)+"km/h")

        print("\r" +"|latitude| : "+"|"+str(+self.letitude))

        print("\r" +"|Longitude| : "+"|"+str(self.longitude))
        tiem = 10
        distance  = tiem/self.speed
        while distance >= 0 :
            sys.stdout.write("\r" +"|Distance| : "+str(distance)+"km" +" "+ " " + "|Flight Time| : " + str(tiem) + "H")
            sys.stdout.flush()

            distance = tiem / self.speed
            tiem = tiem -1
            time.sleep(1)

    def get_points(self):
        destinations  = [self.sequense]
        destin = destinations.pop()
        destin = destin.split(',')
        ala = ['A']
        dir = []
        for a in destin :
            if len(a) >= 4 :
                cur.execute('select Name , Location  from  Warehouse where  Cod  = "%s"' %(a))
                result = cur.fetchall()
            else :
                """results.append(gc.get_coordinates(a))"""
        return result







lista = get_trip()


Trip = trip(lista[0],str(lista[1]),lista[2],lista[3],lista[4],lista[11])

print(Trip.get_points())
print(get_Warehouse())