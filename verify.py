from PIL import Image
import glob
import argparse
from shutil import copyfile
import os
import cv2
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Verify dataset")
    parser.add_argument('--inpdir', dest='inpdir', default= 'input/')
    parser.add_argument('--outdir', dest='outdir', default= 'dataset_verified/')
    args = parser.parse_args()
    inp_dir = args.inpdir
    out_dir = args.outdir

    if not os.path.exists:
        os.makedirs(out_dir)

    items = glob.glob(inp_dir+'*/*.jpg')
    print('INP_DIR='+inp_dir+'*/*.jpg')
    print('Total file = '+str(len(items)))
    error = 0
    for item in items:
        # img = Image.open(item)
        img = cv2.imread(item)
        
        if img is None:
            print('Cannot load img: '+item)
            error += 1
            continue
        file_out_dir = out_dir+os.path.dirname(item)
        if not (os.path.exists(file_out_dir)):
            os.makedirs(file_out_dir)
        copyfile(item,file_out_dir+os.path.basename(item))

    print('-------------------------------')
    print('Total file = '+str(len(items)))
    print('Cannot load = '+str(error))
