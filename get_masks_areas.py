import shapely
from shapely.geometry import Polygon, Point, LineString, MultiPolygon
import cv2

def get_masks_areas(masks):
    global indices_to_delete
    contours = []
    for i in range(0, len(masks['instances'].pred_masks)):
        mask = masks['instances'].pred_masks[i].cpu().numpy().astype('uint8')
        contour, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        if len(contour)>0:
            if len(contour)>1:
                checker = False
                temp_list_len = []
                for z in range(0, len(contour)):
                    temp_list_len.append(len(contour[z]))
                if max(temp_list_len)>3:
                    checker = True
                    contours.append(contour[temp_list_len.index(max(temp_list_len))])
                if checker == False:
                    indices_to_delete.append(i) 
            elif len(contour)==1 and len(contour[0])>3: contours.append(contour[0])
            else: indices_to_delete.append(i) 
        else: indices_to_delete.append(i)

    bb, total_area = [], []
    for i in contours:
      kk, area = [],[]
      for l in i:
        for k in l:
          b=[]
          for z in k:
            kk.append(z)
            b.append(z)
          area.append(tuple(b))
      bb.append(kk)
      total_area.append(area)
    final_areas = []
      
    for i in range(0,len(total_area)):
        pgon = Polygon(total_area[i])
        final_areas.append(pgon.area)
        
    return total_area, bb, final_areas


