import json
import urllib.parse
import urllib.request

class MapQuest:
    def __init__(self,APIKEY):
        self._key = APIKEY
        self.openDirectionsResourceUrl = 'http://open.mapquestapi.com/directions/v2/route'
        self.geocodingResourceUrl= 'http://www.mapquestapi.com/geocoding/v1/address'
        self.searchResourceUrl= 'http://www.mapquestapi.com/search/v4/place'

    def totalDistance(self,locations:list)->float:
        distance=0
        for i in range(1,len(locations)):
            query_parameters=[('key', self._key),('from',locations[i-1]),('to',locations[i])]
            searchUrl = self.openDirectionsResourceUrl+'?'+urllib.parse.urlencode(query_parameters)
            print(searchUrl)
            response = urllib.request.urlopen(searchUrl)
            print(response)
            jsonFile = json.load(response)
            distance += jsonFile['route']['distance']
        response.close()
        return distance
    
    def totalTime(self,locations:list)->int:
        time=0
        for i in range(1,len(locations)):
            query_parameters=[('key',self._key),('from',locations[i-1]),('to',locations[i])]
            searchUrl = self.openDirectionsResourceUrl+ '?'+urllib.parse.urlencode(query_parameters)
            response = urllib.request.urlopen(searchUrl)
            jsonFile = json.load(response)
            time += jsonFile['route']['time']
        response.close()
        return time

    def directions(self,locations:list)->str:
        directions=''
        for i in range(1,len(locations)):
            query_parameters = [('key', self._key),('from',locations[i - 1]),('to',locations[i])]
            searchUrl=self.openDirectionsResourceUrl+'?'+urllib.parse.urlencode(query_parameters)
            response = urllib.request.urlopen(searchUrl)
            jsonFile = json.load(response)
            for j in jsonFile['route']['legs'][0]['maneuvers']:
                directions += j['narrative']
                directions += '\n'
        response.close()
        return directions
    
    def pointOfInterest(self,locations:str,keyword:str,result:int)->list:
        query_parameters=[('key',self._key),('location',locations)]
        searchUrl = self.geocodingResourceUrl+'?'+urllib.parse.urlencode(query_parameters)
        response1 = urllib.request.urlopen(searchUrl)
        jsonFile = json.load(response1)
        latitude = jsonFile['results'][0]['locations'][0]['latLng']['lat']
        longitude = jsonFile['results'][0]['locations'][0]['latLng']['lng']
        mylist=[]
        query_parameters=[('key',self._key),('location',str(longitude)+','+str(latitude)),('sort','distance'),('limit', result),('q',keyword)]
        searchUrl=self.searchResourceUrl+'?'+urllib.parse.urlencode(query_parameters)
        response2=urllib.request.urlopen(searchUrl)
        jsonFile = json.load(response2)
        for i in jsonFile['results']:
            mylist.append(i['displayString'])
        response1.close()
        response2.close()
        print(searchUrl)
        return mylist

# m = MapQuest('cVFJvqGmXgGBAApVucLyj9ouoeTOuN6d')
# m.pointOfInterest('4143 Campus Dr, Irvine, CA 92612','gas',15)






























