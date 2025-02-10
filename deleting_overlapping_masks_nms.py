import shapely
from shapely.geometry import Polygon, Point, LineString, MultiPolygon

def delete_overlap(bboxes, masks, labels, scores, areas):
    assert len(bboxes)==len(masks) and len(masks)==len(labels) and len(labels)==len(scores)
    
    should_delete = []
    THRESHOLD = 40
    for i in range(0, len(labels)-1):
        for j in range(i+1,len(labels)):
           # print("Intersection between: ", max(Polygon(masks[i]).intersection(Polygon(masks[j])).area/Polygon(masks[i]).area*100,Polygon(masks[i]).intersection(Polygon(masks[j])).area/Polygon(masks[j]).area*100), intersection(bboxes[i], bboxes[j]), labels[i], labels[j])
            if Polygon(masks[i]).intersection(Polygon(masks[j])):
              if max(Polygon(masks[i]).intersection(Polygon(masks[j])).area/Polygon(masks[i]).area*100,Polygon(masks[i]).intersection(Polygon(masks[j])).area/Polygon(masks[j]).area*100)>THRESHOLD:
                if scores[i] > scores[j] and labels[i]!=labels[j]: #labels should not be the same
                    max(Polygon(masks[i]).intersection(Polygon(masks[j])).area/Polygon(masks[i]).area*100,Polygon(masks[i]).intersection(Polygon(masks[j])).area/Polygon(masks[j]).area*100)
                    should_delete.append(j)
                    
                else:
                    should_delete.append(i)
                
    for i in sorted(set(should_delete), reverse = True):
        del bboxes[i]
        del masks[i]
        del labels[i]
        del scores[i]
        del areas[i]
    return  bboxes, masks, labels, scores, areas
