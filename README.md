# prepare-dataset-resnet
1) Shuffle all images/ divide into train-val set
python prepare_dataset_resnet.py
--inpdir [INP DIR]
--outdir [OUT DIR]

2) Create pickle file from train-val folder set
python cvt_to_pickle.py
--inpdir [INP DIR]
--outfile [OUT PICKLE FILE]

config: config.py