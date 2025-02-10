import shapely
from shapely.geometry import Polygon, Point, LineString, MultiPolygon

def iou(gt, pred):
    x1,y1,x2,y2 = gt
    x3,y3,x4,y4 = pred
    x_inter1 = max(x1,x3)
    y_inter1 = max(y1,y3)
    x_inter2 = min(x2,x4)
    y_inter2 = min(y2,y4)
    width_inter  = abs(x_inter2 - x_inter1)
    height_inter  = abs(y_inter2 - y_inter1)
    area_inter = width_inter*height_inter
    width_box1= abs(x2-x1)
    height_box1 = abs(y2-y1)
    width_box2 = abs(x4-x3)
    height_box2 = abs(y4-y3)
    area_box1 = width_box1*height_box1
    area_box2 = width_box2*height_box2
    area_union = area_box1+area_box2-area_inter
    iou = area_inter/area_union
    return iou