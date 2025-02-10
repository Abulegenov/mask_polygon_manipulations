import shapely
from shapely.geometry import Polygon, Point, LineString, MultiPolygon

def bordering(masks, bbox, final_areas):
    #if two masks are close to each other, this function unites their borders, 
    #so that no gaps are between those masks
    #areas, masks, bboxes are all updated

    for i in range(0, len(masks)):
      masks[i] = Polygon(masks[i])

    area_copy = masks.copy()

    for i in range(0, len(masks)-1):
      for j in range(i+1, len(masks)):

        if masks[i].intersection(masks[j]):
            if final_areas[i]<final_areas[j]:
              temp_poly = bbox[i]
              for z in range(0, len(temp_poly)):
                temp_poly[z] = int(temp_poly[z])
              k = []
              k.append((temp_poly[0], temp_poly[1]))
              k.append((temp_poly[0], temp_poly[3]))
              k.append((temp_poly[2], temp_poly[3]))
              k.append((temp_poly[2], temp_poly[1]))
              temp_poly = Polygon(k)
              try:
                masks[j] = masks[j] - Polygon(masks[i].intersection(masks[j]))
              except:
                 continue
              temp_count = []
              try:
                if len(masks[j])>1:
                  for u in range(0, len(masks[j])):
                    temp_count.append(len(masks[j][u].exterior.coords))
                for u in range(0, len(masks[j])):
                  if len(masks[j][u].exterior.coords)==max(temp_count):
                    masks[j] = masks[j][u]
                    break
              except:
                masks[j] = masks[j]
              
              pgon = masks[j]
              final_areas[j] = pgon.area
              bbox[j] = list(pgon.bounds)
            else:
              
              temp_poly = bbox[j]
              for z in range(0, len(temp_poly)):
                temp_poly[z] = int(temp_poly[z])
              k = []
              k.append((temp_poly[0], temp_poly[1]))
              k.append((temp_poly[0], temp_poly[3]))
              k.append((temp_poly[2], temp_poly[3]))
              k.append((temp_poly[2], temp_poly[1]))
              temp_poly = Polygon(k)
             
              masks[i] = masks[i] - masks[i].intersection(masks[j])
              temp_count = []
              try:
                if len(masks[i])>1:
                  for u in range(0, len(masks[i])):
                    temp_count.append(len(masks[i][u].exterior.coords))
                for u in range(0, len(masks[i])):
                  if len(masks[i][u].exterior.coords)==max(temp_count):
                    masks[i] = masks[i][u]
                    break
              except:
                masks[i] = masks[i]
              pgon = masks[i]
              final_areas[i] = pgon.area
              bbox[i] = list(pgon.bounds)
    for i in range(0, len(masks)):
        try:
            masks[i] = list(masks[i].exterior.coords)
        except:
            if isinstance(masks[i], MultiPolygon): 
              polygons = list(masks[i].geoms)
              areas_of_polygons_here = [i.area for i in polygons]
              for k in range(0, len(polygons)):
                if polygons[k].area == max(areas_of_polygons_here):
                  masks[i] = list(polygons[k].exterior.coords)
            else:
              try:
                masks[i] = list(masks[i][0].exterior.coords)
              except:
                polygons = list(masks[i].geoms)
                areas_of_polygons_here = [i.area for i in polygons]
                for k in range(0, len(polygons)):
                  if polygons[k].area == max(areas_of_polygons_here):
                    masks[i] = list(polygons[k].exterior.coords)
    return masks, bbox, final_areas
