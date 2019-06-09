from jubilant import Square, Point, Map
import json

class MapRepository:
    def match(self, x, y, squares):
        for s in squares:
            if s['x'] == x and s['y'] == y:
                return s 
        return None

    def find(self, id):
        map = Map(id)
        with open("%s.json" % id) as json_file:  
            data = json.load(json_file)['map']
            for y in range(data['height']):
                for x in range(data['width']):
                    matching_square = self.match(x, y, data['squares'])
                    if matching_square:
                        map.append(Square(Point(x, y), type_name=matching_square['type']))
                    else:
                        map.append(Square(Point(x, y), Square.OPEN))
        return map

    
    def save(self, map):
        data = {}
        m = data['map'] = {}
        m['width'] = map.width
        m['height'] = map.height
        squares = m['squares'] = []
        for square in map.interesting_squares():
            squares.append({
                'x': square.x,
                'y': square.y,
                'type': square.type_name
            })

        with open("%s.json" % map.id, 'w') as outfile:  
            json.dump(data, outfile, indent=4)