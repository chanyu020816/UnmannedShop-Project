from controller.apply_album_aug import apply_aug
from controller.get_album_bb import get_bboxes_list
import cv2
import os
import yaml
import time

with open("contants.yaml", 'r') as stream:
    CONSTANTS = yaml.safe_load(stream)


def run_pipeline():
    imgs = os.listdir(CONSTANTS["inp_img_pth"])   

    for img_file in imgs:   
        file_name = img_file.split('.jpg')[0]
        image = cv2.imread(os.path.join(CONSTANTS["inp_img_pth"], img_file))           
        lab_pth = os.path.join(CONSTANTS["inp_lab_pth"], file_name + '.txt')                                
        album_bboxes = get_bboxes_list(lab_pth, CONSTANTS['CLASSES'])
        for x in range(60):
            aug_file_name = file_name + "_" + CONSTANTS["transformed_file_name"] + str(x)
            apply_aug(image, album_bboxes, CONSTANTS["out_lab_pth"],  CONSTANTS["out_img_pth"], aug_file_name, CONSTANTS['CLASSES'])
        time.sleep(2)
        print(img_file, "Complete")
