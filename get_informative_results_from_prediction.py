def get_bboxes(prediction_output):
      pred_bbox_raw = prediction_output['instances'].to('cpu').pred_boxes
      bboxes = []
      for b in pred_bbox_raw:
          bboxes.append([int(i) for i in b.numpy().tolist()])
      return bboxes

def get_masks(prediction_output):
    pred_masks = prediction_output['instances'].to('cpu').pred_masks.numpy().tolist()
    return pred_masks

def get_category_ids(prediction_output):
    pred_labels = [i for i in prediction_output['instances'].to('cpu').pred_classes.tolist()]
    return pred_labels

def get_labels(prediction_output):
    pred_map = {0:'first_class',1:'second_class'}
    pred_labels = [pred_map[i] for i in prediction_output['instances'].to('cpu').pred_classes.tolist()]
    return pred_labels

def get_scores(prediction_output):
    pred_scores = [round(100*i) for i in prediction_output['instances'].to('cpu').scores.numpy()]
    return pred_scores

def get_image_size(prediction_output):
    image_size = list(prediction_output['instances'].image_size)
    return image_size
