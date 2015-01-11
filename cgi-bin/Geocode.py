__author__ = 'Joan'
import MySQLdb
import yate
from geopy.geocoders import Nominatim
from mako.template import Template
import sys
import time
from math import radians, cos, sin, asin, sqrt


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

    def Get_Distance(self):
        lon1 , lat1 = self.longitude ,self.letitude

        end = self.get_points()
        adresses = []
        for a in end :
            adresses.append(end[a])
        points = adresses.pop()
        location = geolocator.geocode(points)
        lon2 ,lat2 = location.longitude , location.longitude

        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))

        # 6367 km is the radius of the Earth
        km = 6367 * c
        return km

    def get_points(self):
        destinations  = [self.sequense]
        destin = destinations.pop()
        destin = destin.split(',')
        dir = {}
        for a in destin :
            if len(a) >= 4 :
                cur.execute('select   Name ,Location  from  Warehouse where  Cod  = "%s"' %(a))
                result = cur.fetchall()
                for a in result :
                    dir[a[0]] = a[1]

            else :
                cur.execute('select  Nombre , Direccion from  Client where Id = "%s"' %(a))
                result = cur.fetchall()
                for a in result :
                    dir[a[0]] = a[1]
        return dir

    def DisplayContent (self):


        print("| Trip Description| : "+"|"+self.description)

        print( "|speed| : " +str(self.speed)+"km/h")


        dire = self.get_points()
        diro =[]
        for a in dire :
            diro.append(dire[a])
        loc = diro[0]
        latitude = self.letitude
        longitude = self.longitude
        cur.execute ('UPDATE  Drone SET Latitude = %d, Longitude = %d  where  Id = 1234' %(latitude , longitude))
        tiem = 10
        distance  = tiem/self.speed
        while distance >= 0 :
            sys.stdout.write( "\r" "|Distance| : "+str(distance)+ "km"+
                             " " + "|Time Left| : " + str(tiem) + "H"+ " "+ " " + "|Location | : " + loc + " " + "|Latitude| : " + str(latitude)+ " " + "|Longitude| :"+ str(longitude))
            sys.stdout.flush()
            distance = tiem / self.speed

            if tiem <= 7.5 :
                loc = diro[1]
                location = geolocator.geocode(loc)
                latitude = location.latitude
                longitude =  location.longitude
                cur.execute ('UPDATE  Drone SET Latitude = %d, Longitude = %d  where  Id = 1234' %(latitude , longitude))
                db.commit()
            if tiem <= 5 :
                loc = diro[2]
                location = geolocator.geocode(loc)
                latitude = location.latitude
                longitude =  location.longitude
                cur.execute ('UPDATE  Drone SET Latitude = %d, Longitude = %d  where  Id = 1234' %(latitude , longitude))
                db.commit()
            if tiem <= 2.5 :
                loc = diro[3]
                location = geolocator.geocode(loc)
                latitude = location.latitude
                longitude =  location.longitude
                cur.execute ('UPDATE  Drone SET Latitude = %d, Longitude = %d  where  Id = 1234 ' %(latitude , longitude))
                db.commit()
            tiem = tiem - 1
            time.sleep(1)








lista = get_trip()


Trip = trip(lista[0],str(lista[1]),lista[2],lista[3],lista[4],lista[11])
Trip.DisplayContent()
print(Trip.Get_Distance())


"""letters =[1,2,3,4,5,6,78,9]
flight=["132131351","46468156","46515135","16654646"]
for i , e in zip(flight,letters) :
    sys.stdout.write("\r" +"|coordinates| : "+"|"+i+"|" + " " + str(e))
    sys.stdout.flush()
    time.sleep(1)"""




warehouse = get_Warehouse()
b =[]
for a in warehouse:
    b.append(warehouse[a])


coor1= b.pop()
coor2 = b.pop()
points=[]
for a in coor1 :
    points.append(a)
for a in coor2:
    points.append(a)

