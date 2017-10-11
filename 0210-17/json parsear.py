
import json

json_file = open('marvel.json').read()
json_data = json.loads(json_file)
print json_data ['data']

#al menos dos propiedades de cada una

#ej

class Personaje(object):
    def set_data(self, data):
        self.data = data

        pass

class TheData():
    def __init__(self):
        pass

class Results(object):
    def __init__(self, id, name, thumbnail):
        self.id = id
        self.name = name
        self.thumbnail = thumbnail

        pass

class Thumbnail():
    def __init__(self,thumb, path):
        self.thumb = thumb
        self.path = path


personaje = Personaje()
personaje.set_data(json_data['data'])

