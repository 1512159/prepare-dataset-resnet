import glob
import os
import cv2
import numpy as np
import pickle
from config import cfg
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Merge and shuffle dataset")
    parser.add_argument('--inpdir', dest='inpdir', default= 'output/')
    parser.add_argument('--outfile', dest='outfile', default= 'result.pickle')

    args = parser.parse_args()
    inp_dir = args.inpdir
    out_pickle_file = args.outfile

    imgs_train = []
    imgs_test = []

    X_test = []
    y_test = []
    X_train = []
    y_train = []

    for folder in cfg.train_data_set:
        imgs_train += glob.glob(inp_dir+folder+'/*')
        fo = open(inp_dir+'labels_'+folder+'.txt')
        for line in fo:
            y_train.append(int(line))

    for folder in cfg.test_data_set:
        imgs_test += glob.glob(inp_dir+folder+'/*')
        fo = open(inp_dir+'labels_'+folder+'.txt')
        for line in fo:
            y_test.append(int(line))

    for imgfile in imgs_test:
        img = cv2.imread(imgfile)
        img = cv2.resize(img,(cfg.WIDTH,cfg.HEIGHT))
        X_test.append(img)

    for imgfile in imgs_train:
        img = cv2.imread(imgfile)
        img = cv2.resize(img,(cfg.WIDTH,cfg.HEIGHT))
        X_train.append(img)

    X_test = np.array(X_test)
    y_test = np.array(y_test).reshape((len(y_test),1))
    X_train = np.array(X_train)
    y_train = np.array(y_train).reshape((len(y_train),1)) 
    print('X_test_shape: ',X_test.shape)
    print('y_test_shape: ',y_test.shape)
    print('X_train_shape: ',X_train.shape)
    print('y_train_shape: ',y_train.shape)

    of = open(out_pickle_file,"wb")
    pickle.dump(((X_train,y_train),(X_test,y_test)),of)
    of.close()