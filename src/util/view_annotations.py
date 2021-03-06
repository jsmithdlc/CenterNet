from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab


annFile="../../CenterNet/data/thermal_pose/annotations/thermalPose_train.json"
coco=COCO(annFile)

catIds = coco.getCatIds(catNms=['person']);
imgIds = coco.getImgIds(catIds=catIds);
imgIds = coco.getImgIds(imgIds = [300])
img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]

#I = io.imread("/home/javier/Universidad/memoria/repositorios/ThermalPose/CenterNet/data/chen_wang/test/"+img['file_name'])
I = io.imread("../../CenterNet/data/thermal_pose/train/"+img['file_name'])

coco_kps=COCO(annFile)
plt.imshow(I,cmap='gray'); plt.axis('off')
ax = plt.gca()
annIds = coco_kps.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
anns = coco_kps.loadAnns(annIds)
print(anns)
coco_kps.showAnns(anns,draw_bbox=True)
plt.show()