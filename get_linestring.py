import shapely
from shapely.geometry import Polygon, Point, LineString, MultiPolygon

def get_linestring(list_of_points):
  point_A = Point((list(n)[0] for n in list_of_points[0]))
  point_B = Point((list(n)[0] for n in list_of_points[1]))
  point_C = Point((list(n)[0] for n in list_of_points[2]))#lb
  point_D = Point((list(n)[0] for n in list_of_points[3]))#rb
  mid_point_up= Point(((point_A.x+point_B.x)/2, (point_A.y+point_B.y)/2,))
  mid_point_bottom = Point(((point_C.x+point_D.x)/2, (point_C.y+point_D.y)/2,))
  AB = LineString([mid_point_up, mid_point_bottom])
  return AB