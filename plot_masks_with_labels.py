import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
plt.rcParams["figure.figsize"] = [12,20]

def plot_result(img, bboxes, masks,areas, labels, scores, category_ids, file_name):
    print(labels,'confidence: ', scores)    
    f, ax1 = plt.subplots(1,1,figsize=(12,20))
    
    mask_colors = [np.random.randint(0, 256, (1, 3), dtype=np.uint8) for _ in range(len(labels))]
    temp = img.copy()
    for i,m in enumerate(masks):
        color_mask = mask_colors[i]
        temp[m] = temp[m] * 0.5 + color_mask * 0.5

    ax1.imshow(temp); ax1.axis('off')

    for i,c in enumerate(bboxes):
        rect = patches.Rectangle((c[0],c[1]), c[2]-c[0], c[3]-c[1], linewidth=1, edgecolor='r', facecolor='none')
        ax1.add_patch(rect)
        ax1.text(c[0], c[1], labels[i], horizontalalignment='left',\
                verticalalignment='top', size=8, bbox=dict(facecolor='red', alpha=0.4, edgecolor='black'))

    plt.savefig('temp_folder/'+file_name,bbox_inches='tight')

