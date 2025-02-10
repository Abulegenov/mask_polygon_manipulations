import shapely
from shapely.geometry import Polygon, Point, LineString, MultiPolygon

def intersection(bbox1_input, bbox2_input):
  bbox1 = []
  bbox1.append((bbox1_input[0], bbox1_input[1]))
  bbox1.append((bbox1_input[0], bbox1_input[3]))
  bbox1.append((bbox1_input[2], bbox1_input[3]))
  bbox1.append((bbox1_input[2], bbox1_input[1]))
  bbox1 = Polygon(bbox1)
  bbox2 = []
  bbox2.append((bbox2_input[0], bbox2_input[1]))
  bbox2.append((bbox2_input[0], bbox2_input[3]))
  bbox2.append((bbox2_input[2], bbox2_input[3]))
  bbox2.append((bbox2_input[2], bbox2_input[1]))
  bbox2 = Polygon(bbox2)
  intersection_area = bbox1.intersection(bbox2).area
  total_area = bbox1.area + bbox2.area
  intersection = max(intersection_area/bbox1.area*100,intersection_area/bbox2.area*100)
  return intersection