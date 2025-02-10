import shapely
from shapely.geometry import Polygon, Point, LineString, MultiPolygon

def mask_prolongation(initial_masks,seg_areas, bboxes, masks, labels):
  """prolong masks with same labels located one after another"""
  required_class_list = [] #optional condition
  for i in range(0, len(labels)-1):
    for j in range(i+1, len(labels)):
   
      if labels[i] in required_class_list and labels[j] in required_class_list:
        whole_polygon = ''
        max_buffer = 20
        #use isinstance
        while not isinstance(whole_polygon, Polygon) and max_buffer <25:
          print(max_buffer)
          whole_polygon = MultiPolygon([Polygon(masks[i]), Polygon(masks[j])])
          whole_polygon = whole_polygon.buffer(max_buffer).buffer(-max_buffer)
          max_buffer = max_buffer + 1
        
        if isinstance(whole_polygon, Polygon):
                  print('Polygon found on', i, ' ', labels[i], ' ', j, ' ', labels[j])
        
                  total_merged = whole_polygon
                  whole_polygon = whole_polygon -  whole_polygon.intersection(Polygon(masks[i])) - whole_polygon.intersection(Polygon(masks[j])) 
                  temp_count = []

                  if len(whole_polygon)>1:
                    for u in range(0, len(whole_polygon)):
                      if isinstance(whole_polygon[u], Polygon):
                        temp_count.append(len(whole_polygon[u].exterior.coords))
                  for u in range(0, len(whole_polygon)):
                    if isinstance(whole_polygon[u], Polygon):
                      if len(whole_polygon[u].exterior.coords)==max(temp_count):
                        whole_polygon = whole_polygon[u]
                        break
                  bbox1_input = list(whole_polygon.bounds)
                  bbox1 = []
                  bbox1.append((bbox1_input[0], bbox1_input[1]))
                  bbox1.append((bbox1_input[0], bbox1_input[3]))
                  bbox1.append((bbox1_input[2], bbox1_input[3]))
                  bbox1.append((bbox1_input[2], bbox1_input[1]))
                  bbox1 = Polygon(bbox1)
    
                  new_shape = whole_polygon.boundary.intersection(bbox1.boundary)

                  if seg_areas[i]>seg_areas[j]:
                    initial_masks[j] = total_merged - total_merged.intersection(Polygon(initial_masks[i]).buffer(max_buffer).buffer(-max_buffer))
                    try:
                      temp_count = []
                      for u in range(0, len(initial_masks[j])):
                        temp_count.append(len(initial_masks[j][u].exterior.coords))
                      for u in range(0, len(initial_masks[j])):
                        if len(initial_masks[j][u].exterior.coords)==max(temp_count):
                          initial_masks[j] = initial_masks[j][u]
                          break
                    except: 
                       initial_masks[j] = initial_masks[j]
                    bboxes[j] = list(initial_masks[j].bounds)
                    seg_areas[j] = initial_masks[j].area
                    initial_masks[j] = list(initial_masks[j].exterior.coords)
                  else:
                    initial_masks[i] = total_merged - total_merged.intersection(Polygon(initial_masks[j]).buffer(max_buffer).buffer(-max_buffer))
                    try:
                      temp_count = []
            
                      for u in range(0, len(initial_masks[i])):
                        temp_count.append(len(initial_masks[i][u].exterior.coords))
                      for u in range(0, len(initial_masks[i])):
                        if len(initial_masks[i][u].exterior.coords)==max(temp_count):
                          initial_masks[i] = initial_masks[i][u]
                          break
                    except: 
                       initial_masks[j] = initial_masks[j]
                    bboxes[i] =list(initial_masks[i].bounds)
                    seg_areas[i] = initial_masks[i].area
                    initial_masks[i] = list(initial_masks[i].exterior.coords)
                 
  return initial_masks, bboxes, seg_areas            
