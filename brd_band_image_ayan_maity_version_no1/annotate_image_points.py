import numpy as np
import skimage.io as io
import cv2
import pandas as pd
import matplotlib.pyplot as plt 

def draw_point(event, x, y, flags, param):
    """Take one point"""
    global points_pos, count_points
    
    if event == cv2.EVENT_LBUTTONDBLCLK:   
        cv2.drawMarker(img_copy, (x, y), color=(255,255,255), markerType=cv2.MARKER_CROSS, markerSize=5)
        points_pos.append((y, x))
        count_points += 1
        print('Position of {}-th point: ({}, {})'.format(count_points, x, y))
        
        
if __name__ == '__main__':
    
    # IMAGE FILE NAME YOU WANT TO READ
    image_path = './data/'  # Change your dataset path
    img_filename = 'band4.gif'

    img = plt.imread(''.join([image_path, img_filename]))
    img_copy = img.copy()  # Make a copy of the image array
    print('Input image size:', img.shape)

    # TO STORE ANNOTATED POINTS
    points_pos = []
    count_points = 0

    num_points = int(input('How many points would you like to annotate? '))

    cv2.namedWindow('Move mouse pointer and double click to locate the position')
    cv2.setMouseCallback('Move mouse pointer and double click to locate the position', draw_point)

    while True:
        cv2.imshow('Move mouse pointer and double click to locate the position', img_copy)
        k = cv2.waitKey(20) & 0xFF
        if k == 27 or count_points == num_points:
            # WRITE ANNOTATED IMAGE
            img_save_filename = ''.join([
                image_path, 
                'annotated_', img_filename.split('.')[0], 
                '_np_', str(len(points_pos)), 
                '.gif'
            ])
            plt.imsave(img_save_filename, img_copy)
            
            # SAVE ANNOTATED POINTS AS CSV FILE
            pd.DataFrame(
                data=np.asarray(points_pos), 
                columns=['row', 'column']
            ).to_csv(''.join([
                image_path, 
                'annotated_points_', img_filename.split('.')[0], 
                '_np_', str(len(points_pos)), 
                '.csv'
            ]), index=False)
            
            break

    cv2.destroyAllWindows()
