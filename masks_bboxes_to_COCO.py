import json
def coco_format_instance_segmentation(bbox,masks_segments,areas, labels_segments, scores, category_ids, image_size):
    """Converts model output into COCO format. Refer to official documentation."""
    #Implementation for 1 image only
    total_json = {}
    total_json["categories"]= [
            {"id": 1, "name": "name_1", "supercategory": ""},
            {"id": 2, "name": "name_2", "supercategory": ""},
            #...
    ]

    total_json['info'] = {"contributor": "your_company", 
                          "date_created": "", 
                          "descripton": "", 
                          "url": "", 
                          "version": "",
                          "year": "2022"}
    total_json['images'] = []
    annos = []
    image_id_map = {}
    filename = 'your_image_name.png'

    masks_right_format = [None]*len(masks_segments)
    for i in range(0, len(masks_segments)):
        masks_right_format[i]=[]
        for z in range(0, len(masks_segments[i])):
            masks_right_format[i].append(masks_segments[i][z][0])
            masks_right_format[i].append(masks_segments[i][z][1])
    
    image_id_map[filename] = 0
    
    total_json['images'].append(
        {
            'id': 0,
            'file_name' :filename,
            'width' : int(image_size[0]),
            'height' : int(image_size[1]),
            'license' : 0,
            'flickr_url' : "",
            'coco_url' : "",
            'date_captured' :0
        }
    )

    for i in range(0, len(masks_right_format)):
        b= {}
        b['id'] = len(annos)
        b['image_id'] = image_id_map[filename]
        for op in total_json['categories']:
          if op['name'] == category_ids[i]:
            b['category_id'] = op['id']
            break

        for k in range(0, len(masks_right_format[i])):
            masks_right_format[i][k] = float( masks_right_format[i][k] )
        
        b['segmentation'] = [masks_right_format[i]]
        b['area'] = float(areas[i])
        b['bbox'] = bbox[i]
        b['iscrowd'] = 0
        b['attributes'] = {"occluded": False}
        annos.append(b)

    total_json['annotations'] = annos

    return total_json