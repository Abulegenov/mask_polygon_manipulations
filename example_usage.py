from get_informative_results_from_prediction import *
from plot_masks_with_labels import plot_result
from get_masks_areas import *
from mask_prolongation import *
from bbox_intersection import *
from bbox_iou import *
from masks_borders_regulation import *
from deleting_overlapping_masks_nms import delete_overlap
from masks_bboxes_to_COCO import *

def predict(img):
    """Function to run model inference on given image"""
    #implement code here
    return 'prediction_result'

def process_prediction_result(prediction_result):
    image_size = get_image_size(prediction_result)
    bbox = get_bboxes(prediction_result)
    masks_segments,_, areas= get_masks_areas(prediction_result)
    scores = get_scores(prediction_result)
    labels_segments = get_labels(prediction_result)
    category_ids = get_category_ids(prediction_result)
    bbox, masks_segments, labels_segments, scores, areas = delete_overlap(bbox, masks_segments, labels_segments, scores, areas)
    masks_segments, bbox, areas, labels_segments = bordering(masks_segments, bbox, areas, labels_segments)
    masks_segments, bbox, areas = mask_prolongation(masks_segments,areas, bbox, masks_segments, labels_segments)
    return  bbox,masks_segments,areas, labels_segments, scores, category_ids, image_size

img = 'some image'
file_name = 'save_fig_name'
plot_result(img, *process_prediction_result(predict(img))[:-1], file_name)

coco_formatted_output_json = coco_format_instance_segmentation(*process_prediction_result(predict(img)))

with open(f'coco_format.json', 'w', encoding='ascii') as f:
    json.dump(coco_formatted_output_json,f)
            
